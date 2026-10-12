[CmdletBinding()]
param(
    # Tool to call; omit to list all tools.
    [string]$Tool = "",
    # Tool arguments as a JSON object string.
    [string]$Arguments = "{}"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# The URL path is a secret token - never print or log $env:HA_MCP.
if ([string]::IsNullOrWhiteSpace($env:HA_MCP)) {
    throw "HA_MCP environment variable is required."
}
$McpUrl = $env:HA_MCP

function Invoke-Mcp {
    param(
        [Parameter(Mandatory = $true)][hashtable]$Message,
        [Parameter(Mandatory = $true)][hashtable]$Headers
    )

    $body = $Message | ConvertTo-Json -Depth 20 -Compress
    $resp = Invoke-WebRequest -Uri $McpUrl -Method Post -Headers $Headers -ContentType "application/json" -Body $body -UseBasicParsing
    $text = [System.Text.Encoding]::UTF8.GetString($resp.RawContentStream.ToArray())

    # Streamable HTTP may answer with plain JSON or a single-event SSE stream.
    if ("$($resp.Headers['Content-Type'])" -like "*text/event-stream*") {
        $text = ($text -split "`n" | Where-Object { $_ -like "data:*" } | ForEach-Object { $_.Substring(5).Trim() }) -join ""
    }
    if ([string]::IsNullOrWhiteSpace($text)) {
        return [pscustomobject]@{ Response = $resp; Body = $null }
    }

    $parsed = $text | ConvertFrom-Json
    if ($parsed.PSObject.Properties["error"]) {
        throw "MCP error: $($parsed.error | ConvertTo-Json -Depth 10 -Compress)"
    }
    return [pscustomobject]@{ Response = $resp; Body = $parsed }
}

$headers = @{ Accept = "application/json, text/event-stream" }

$init = Invoke-Mcp -Headers $headers -Message @{
    jsonrpc = "2.0"; id = 1; method = "initialize"
    params  = @{
        protocolVersion = "2025-06-18"
        capabilities    = @{}
        clientInfo      = @{ name = "test-ha-mcp"; version = "1.0" }
    }
}
$server = $init.Body.result.serverInfo
Write-Host "Connected: $($server.name) $($server.version) (protocol $($init.Body.result.protocolVersion))"

$sessionId = "$($init.Response.Headers['Mcp-Session-Id'])"
if ($sessionId) { $headers["Mcp-Session-Id"] = $sessionId }
$headers["MCP-Protocol-Version"] = $init.Body.result.protocolVersion
Invoke-Mcp -Headers $headers -Message @{ jsonrpc = "2.0"; method = "notifications/initialized" } | Out-Null

if (-not $Tool) {
    $tools = (Invoke-Mcp -Headers $headers -Message @{ jsonrpc = "2.0"; id = 2; method = "tools/list" }).Body.result.tools
    Write-Host "Tools: $(@($tools).Count)"
    $tools | ForEach-Object { $_.name } | Sort-Object
    return
}

$toolArgs = @{}
($Arguments | ConvertFrom-Json).PSObject.Properties | ForEach-Object { $toolArgs[$_.Name] = $_.Value }

$result = (Invoke-Mcp -Headers $headers -Message @{
    jsonrpc = "2.0"; id = 3; method = "tools/call"
    params  = @{ name = $Tool; arguments = $toolArgs }
}).Body.result

if ($result.PSObject.Properties["isError"] -and $result.isError) {
    Write-Warning "Tool '$Tool' reported an error."
}
$result.content | Where-Object { $_.type -eq "text" } | ForEach-Object { $_.text }
