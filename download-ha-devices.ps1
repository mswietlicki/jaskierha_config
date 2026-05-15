[CmdletBinding()]
param(
    [string]$HaUrl = "https://jaskierha.swietlicki.net/",
    [string]$OutFile = "DEVICES.md"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($env:HA_TOKEN)) {
    throw "HA_TOKEN environment variable is required."
}

if ([string]::IsNullOrWhiteSpace($HaUrl)) {
    $HaUrl = "http://homeassistant.local:8123"
}

function Write-Log {
    param(
        [Parameter(Mandatory = $true)][string]$Message,
        [ValidateSet("INFO", "WARN", "ERROR", "DEBUG")][string]$Level = "INFO"
    )

    $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss.fff")
    Write-Host "[$timestamp][$Level] $Message"
}

function Convert-ToWebSocketUrl {
    param([Parameter(Mandatory = $true)][string]$BaseUrl)

    $trimmed = $BaseUrl.TrimEnd("/")

    if ($trimmed.StartsWith("https://", [System.StringComparison]::OrdinalIgnoreCase)) {
        return "wss://" + $trimmed.Substring(8) + "/api/websocket"
    }

    if ($trimmed.StartsWith("http://", [System.StringComparison]::OrdinalIgnoreCase)) {
        return "ws://" + $trimmed.Substring(7) + "/api/websocket"
    }

    throw "Unsupported HA URL scheme in '$BaseUrl'. Use http:// or https://"
}

function Receive-JsonMessage {
    param([Parameter(Mandatory = $true)][System.Net.WebSockets.ClientWebSocket]$Socket)

    $buffer = New-Object byte[] 65536
    $segment = [System.ArraySegment[byte]]::new($buffer)
    $builder = [System.Text.StringBuilder]::new()

    while ($true) {
        $result = $Socket.ReceiveAsync($segment, [System.Threading.CancellationToken]::None).GetAwaiter().GetResult()

        if ($result.MessageType -eq [System.Net.WebSockets.WebSocketMessageType]::Close) {
            throw "WebSocket closed by server while waiting for a response."
        }

        $builder.Append([System.Text.Encoding]::UTF8.GetString($buffer, 0, $result.Count)) | Out-Null

        if ($result.EndOfMessage) {
            break
        }
    }

    return ($builder.ToString() | ConvertFrom-Json)
}

function Send-JsonMessage {
    param(
        [Parameter(Mandatory = $true)][System.Net.WebSockets.ClientWebSocket]$Socket,
        [Parameter(Mandatory = $true)][object]$Payload
    )

    $json = $Payload | ConvertTo-Json -Depth 20 -Compress
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($json)
    $segment = [System.ArraySegment[byte]]::new($bytes)
    $Socket.SendAsync($segment, [System.Net.WebSockets.WebSocketMessageType]::Text, $true, [System.Threading.CancellationToken]::None).GetAwaiter().GetResult()
}

function Invoke-HaWsCommand {
    param(
        [Parameter(Mandatory = $true)][System.Net.WebSockets.ClientWebSocket]$Socket,
        [Parameter(Mandatory = $true)][int]$Id,
        [Parameter(Mandatory = $true)][string]$Type
    )

        Write-Log -Level "DEBUG" -Message "Sending HA command '$Type' (id=$Id)."
    Send-JsonMessage -Socket $Socket -Payload @{ id = $Id; type = $Type }

    while ($true) {
        $response = Receive-JsonMessage -Socket $Socket

        $responseType = if ($null -ne $response.PSObject.Properties["type"]) { [string]$response.type } else { "" }
        $hasId = $null -ne $response.PSObject.Properties["id"]
        $responseId = if ($hasId) { [int]$response.id } else { -1 }

        if ($responseType -eq "result" -and (-not $hasId)) {
            Write-Log -Level "DEBUG" -Message "Received result message without id, skipping."
            continue
        }

        if ($responseType -eq "result" -and $responseId -ne $Id) {
            Write-Log -Level "DEBUG" -Message "Received result for another command id=$responseId, waiting for id=$Id."
            continue
        }

        if ($responseType -eq "result" -and $responseId -eq $Id) {
            if (-not $response.success) {
                $errorMessage = if ($response.error -and $response.error.message) { $response.error.message } else { "Unknown error" }
                throw "HA command '$Type' failed: $errorMessage"
            }

                $resultCount = if ($null -ne $response.result -and $response.result.Count -ge 0) { $response.result.Count } else { 0 }
                Write-Log -Level "DEBUG" -Message "HA command '$Type' succeeded with $resultCount item(s)."
            return $response.result
        }

            Write-Log -Level "DEBUG" -Message "Ignoring websocket message type '$responseType' while waiting for '$Type'."
    }
}

function Get-StringValue {
    param([object]$Value, [string]$Fallback = "-")

    if ($null -eq $Value -or [string]::IsNullOrWhiteSpace([string]$Value)) {
        return $Fallback
    }

    return [string]$Value
}

function Get-ObjectPropertyValue {
    param(
        [Parameter(Mandatory = $true)][object]$InputObject,
        [Parameter(Mandatory = $true)][string]$PropertyName,
        [object]$Fallback = $null
    )

    if ($null -eq $InputObject) {
        return $Fallback
    }

    $property = $InputObject.PSObject.Properties[$PropertyName]
    if ($null -eq $property) {
        return $Fallback
    }

    return $property.Value
}

function Get-DeviceKey {
    param([Parameter(Mandatory = $true)][object]$Device)

    $id = Get-ObjectPropertyValue -InputObject $Device -PropertyName "id"
    if (-not [string]::IsNullOrWhiteSpace([string]$id)) {
        return [string]$id
    }

    $deviceId = Get-ObjectPropertyValue -InputObject $Device -PropertyName "device_id"
    if (-not [string]::IsNullOrWhiteSpace([string]$deviceId)) {
        return [string]$deviceId
    }

    return $null
}

$wsUrl = Convert-ToWebSocketUrl -BaseUrl $HaUrl
$uri = [System.Uri]::new($wsUrl)
$socket = [System.Net.WebSockets.ClientWebSocket]::new()

try {
    Write-Log -Message "Starting Home Assistant device/entity export."
    Write-Log -Message "Home Assistant URL: $HaUrl"
    Write-Log -Message "WebSocket endpoint: $wsUrl"
    Write-Log -Message "Output file: $OutFile"

    $tokenLength = $env:HA_TOKEN.Length
    Write-Log -Message "Using HA token from environment (length: $tokenLength)."

    Write-Log -Message "Connecting to Home Assistant WebSocket..."
    $socket.ConnectAsync($uri, [System.Threading.CancellationToken]::None).GetAwaiter().GetResult()
    Write-Log -Message "WebSocket connection established."

    Write-Log -Level "DEBUG" -Message "Waiting for auth_required handshake..."
    $hello = Receive-JsonMessage -Socket $socket
    if ($hello.type -ne "auth_required") {
        throw "Unexpected auth handshake response: $($hello | ConvertTo-Json -Compress)"
    }
    Write-Log -Message "Received auth_required from Home Assistant."

    Write-Log -Message "Sending authentication request..."
    Send-JsonMessage -Socket $socket -Payload @{ type = "auth"; access_token = $env:HA_TOKEN }

    Write-Log -Level "DEBUG" -Message "Waiting for auth response..."
    $authResult = Receive-JsonMessage -Socket $socket
    if ($authResult.type -ne "auth_ok") {
        $raw = $authResult | ConvertTo-Json -Compress
        throw "Authentication failed. Response: $raw"
    }
    Write-Log -Message "Authentication successful."

    Write-Log -Message "Downloading device registry..."
    $devices = Invoke-HaWsCommand -Socket $socket -Id 1 -Type "config/device_registry/list"
    Write-Log -Message "Downloaded $($devices.Count) device(s)."

    Write-Log -Message "Downloading entity registry..."
    $entities = Invoke-HaWsCommand -Socket $socket -Id 2 -Type "config/entity_registry/list"
    Write-Log -Message "Downloaded $($entities.Count) entity(s)."

    $deviceMap = @{}
    foreach ($device in $devices) {
        $deviceKey = Get-DeviceKey -Device $device
        if ([string]::IsNullOrWhiteSpace($deviceKey)) {
            $deviceRaw = $device | ConvertTo-Json -Compress -Depth 5
            Write-Log -Level "WARN" -Message "Skipping device row without id/device_id: $deviceRaw"
            continue
        }

        $deviceMap[$deviceKey] = $device
    }
    Write-Log -Level "DEBUG" -Message "Built device lookup map with $($deviceMap.Count) entries."

    $entitiesByDeviceId = @{}
    foreach ($entity in $entities) {
        $deviceId = [string](Get-ObjectPropertyValue -InputObject $entity -PropertyName "device_id" -Fallback "")
        if ([string]::IsNullOrWhiteSpace([string]$deviceId)) {
            continue
        }

        if (-not $entitiesByDeviceId.ContainsKey($deviceId)) {
            $entitiesByDeviceId[$deviceId] = [System.Collections.Generic.List[object]]::new()
        }

        $entitiesByDeviceId[$deviceId].Add($entity)
    }
    Write-Log -Level "DEBUG" -Message "Grouped entities for $($entitiesByDeviceId.Count) device(s)."

    $lines = [System.Collections.Generic.List[string]]::new()
    $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss zzz")

    $lines.Add("# Home Assistant Devices and Entities")
    $lines.Add("")
    $lines.Add("Generated: $timestamp")
    $lines.Add("Home Assistant URL: $HaUrl")
    $lines.Add("")
    $lines.Add("- Devices: $($devices.Count)")
    $lines.Add("- Entities: $($entities.Count)")
    $lines.Add("")

    foreach ($device in ($devices | Sort-Object @{ Expression = { Get-StringValue (Get-ObjectPropertyValue -InputObject $_ -PropertyName "name_by_user") } }, @{ Expression = { Get-StringValue (Get-ObjectPropertyValue -InputObject $_ -PropertyName "name") } })) {
        $deviceId = Get-DeviceKey -Device $device
        if ([string]::IsNullOrWhiteSpace($deviceId)) {
            Write-Log -Level "WARN" -Message "Skipping markdown section for device without id/device_id."
            continue
        }

        $nameByUser = [string](Get-ObjectPropertyValue -InputObject $device -PropertyName "name_by_user" -Fallback "")
        $name = [string](Get-ObjectPropertyValue -InputObject $device -PropertyName "name" -Fallback "")
        $friendlyName = if (-not [string]::IsNullOrWhiteSpace($nameByUser)) { $nameByUser } elseif (-not [string]::IsNullOrWhiteSpace($name)) { $name } else { $deviceId }
        $manufacturer = Get-StringValue -Value (Get-ObjectPropertyValue -InputObject $device -PropertyName "manufacturer")
        $model = Get-StringValue -Value (Get-ObjectPropertyValue -InputObject $device -PropertyName "model")
        $swVersion = Get-StringValue -Value (Get-ObjectPropertyValue -InputObject $device -PropertyName "sw_version")
        $hwVersion = Get-StringValue -Value (Get-ObjectPropertyValue -InputObject $device -PropertyName "hw_version")
        $areaId = Get-StringValue -Value (Get-ObjectPropertyValue -InputObject $device -PropertyName "area_id")

        $lines.Add("## $friendlyName")
        $lines.Add("")
        $lines.Add("- Device ID: $deviceId")
        $lines.Add("- Manufacturer: $manufacturer")
        $lines.Add("- Model: $model")
        $lines.Add("- Software Version: $swVersion")
        $lines.Add("- Hardware Version: $hwVersion")
        $lines.Add("- Area ID: $areaId")
        $lines.Add("")
        $lines.Add("### Entities")

        if ($entitiesByDeviceId.ContainsKey($deviceId) -and $entitiesByDeviceId[$deviceId].Count -gt 0) {
            $lines.Add("")
            $lines.Add("| Entity ID | Name | Platform | Disabled |")
            $lines.Add("|---|---|---|---|")

            foreach ($entity in ($entitiesByDeviceId[$deviceId] | Sort-Object { Get-ObjectPropertyValue -InputObject $_ -PropertyName "entity_id" })) {
                $entityId = Get-StringValue -Value (Get-ObjectPropertyValue -InputObject $entity -PropertyName "entity_id")
                $entityNameRaw = [string](Get-ObjectPropertyValue -InputObject $entity -PropertyName "name" -Fallback "")
                $entityOriginalName = [string](Get-ObjectPropertyValue -InputObject $entity -PropertyName "original_name" -Fallback "")
                $entityName = if (-not [string]::IsNullOrWhiteSpace($entityNameRaw)) { $entityNameRaw } elseif (-not [string]::IsNullOrWhiteSpace($entityOriginalName)) { $entityOriginalName } else { "-" }
                $platform = Get-StringValue -Value (Get-ObjectPropertyValue -InputObject $entity -PropertyName "platform")
                $disabledBy = Get-ObjectPropertyValue -InputObject $entity -PropertyName "disabled_by"
                $disabled = if ($null -ne $disabledBy) { "yes ($disabledBy)" } else { "no" }

                # Escape markdown table separators in text fields.
                $entityNameSafe = $entityName.Replace("|", "\\|")
                $platformSafe = $platform.Replace("|", "\\|")

                $lines.Add("| $entityId | $entityNameSafe | $platformSafe | $disabled |")
            }
        }
        else {
            $lines.Add("")
            $lines.Add("No entities linked to this device.")
        }

        $lines.Add("")
    }

    Write-Log -Level "DEBUG" -Message "Rendered markdown for all devices."

    $orphanEntities = @($entities | Where-Object { [string]::IsNullOrWhiteSpace([string](Get-ObjectPropertyValue -InputObject $_ -PropertyName "device_id" -Fallback "")) } | Sort-Object { Get-ObjectPropertyValue -InputObject $_ -PropertyName "entity_id" })
    if ($orphanEntities.Count -gt 0) {
        Write-Log -Message "Found $($orphanEntities.Count) orphan entity(s) without a device."
        $lines.Add("## Entities Without Device")
        $lines.Add("")
        $lines.Add("| Entity ID | Name | Platform |")
        $lines.Add("|---|---|---|")

        foreach ($entity in $orphanEntities) {
            $entityId = Get-StringValue -Value (Get-ObjectPropertyValue -InputObject $entity -PropertyName "entity_id")
            $entityNameRaw = [string](Get-ObjectPropertyValue -InputObject $entity -PropertyName "name" -Fallback "")
            $entityOriginalName = [string](Get-ObjectPropertyValue -InputObject $entity -PropertyName "original_name" -Fallback "")
            $entityName = if (-not [string]::IsNullOrWhiteSpace($entityNameRaw)) { $entityNameRaw } elseif (-not [string]::IsNullOrWhiteSpace($entityOriginalName)) { $entityOriginalName } else { "-" }
            $platform = Get-StringValue -Value (Get-ObjectPropertyValue -InputObject $entity -PropertyName "platform")

            $entityNameSafe = $entityName.Replace("|", "\\|")
            $platformSafe = $platform.Replace("|", "\\|")

            $lines.Add("| $entityId | $entityNameSafe | $platformSafe |")
        }

        $lines.Add("")
    }
    else {
        Write-Log -Level "DEBUG" -Message "No orphan entities found."
    }

    $resolvedOutPath = [System.IO.Path]::GetFullPath((Join-Path -Path (Resolve-Path -LiteralPath ".").Path -ChildPath $OutFile))
    Write-Log -Message "Writing report to $resolvedOutPath"

    $outputDirectory = [System.IO.Path]::GetDirectoryName($resolvedOutPath)
    if (-not [string]::IsNullOrWhiteSpace($outputDirectory) -and -not (Test-Path -LiteralPath $outputDirectory)) {
        Write-Log -Message "Creating output directory: $outputDirectory"
        New-Item -Path $outputDirectory -ItemType Directory -Force | Out-Null
    }

    [System.IO.File]::WriteAllLines($resolvedOutPath, $lines, [System.Text.Encoding]::UTF8)
    Write-Log -Message "Finished. Wrote $OutFile with $($devices.Count) devices and $($entities.Count) entities."
}
catch {
    $exception = $_.Exception
    Write-Log -Level "ERROR" -Message "Export failed: $($exception.Message)"

    if ($null -ne $exception.InnerException) {
        Write-Log -Level "ERROR" -Message "Inner exception: $($exception.InnerException.Message)"
    }

    throw
}
finally {
    Write-Log -Level "DEBUG" -Message "Cleaning up WebSocket connection (state: $($socket.State))."
    if ($socket.State -eq [System.Net.WebSockets.WebSocketState]::Open) {
        Write-Log -Level "DEBUG" -Message "Closing WebSocket connection."
        $socket.CloseAsync([System.Net.WebSockets.WebSocketCloseStatus]::NormalClosure, "Done", [System.Threading.CancellationToken]::None).GetAwaiter().GetResult()
    }

    $socket.Dispose()
    Write-Log -Level "DEBUG" -Message "WebSocket disposed."
}