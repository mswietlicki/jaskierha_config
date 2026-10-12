# Jaskier Home Assistant config

Configuration repo for the Jaskier Home Assistant instance (HAOS, `/config`).

## Home Assistant MCP (live instance access)

- The live HA instance is reachable through an **ha-mcp** server. Its URL is in the `HA_MCP` environment variable.
- **The URL's path is a secret token that grants full control of HA.** Never write the URL into files, commits, logs or chat output. Reference `$env:HA_MCP` / `${HA_MCP}` only.
- Claude Code loads it from [.mcp.json](.mcp.json) as the `home-assistant` server (`${HA_MCP}` is expanded at load time). Approve the project server when prompted. Its tools then show up as `mcp__home-assistant__ha_*`.
- If the server didn't load in a session, use [test-ha-mcp.ps1](test-ha-mcp.ps1) as a fallback client:
  - `./test-ha-mcp.ps1` lists the tools
  - `./test-ha-mcp.ps1 -Tool ha_get_system_health` calls a tool
  - `./test-ha-mcp.ps1 -Tool ha_eval_template -Arguments '{"template":"{{ states | count }}"}'` calls a tool with arguments
- Server details: ha-mcp runs in-process inside HA through [custom_components/ha_mcp_tools](custom_components/ha_mcp_tools) (the "HA-MCP Server" config entry). It uses streamable HTTP and is stateless (no `Mcp-Session-Id`). It exposes about 80 tools: state and history reads, automation/script/helper/dashboard config, YAML and file editing, backups and restarts. The feature flags are in [.ha_mcp/feature_flags.json](.ha_mcp/feature_flags.json).
- Before ha-mcp modifies an automation, helper, dashboard or YAML file, it writes the previous version to [.ha_mcp/backups/](.ha_mcp/backups/).
- Many tools write to the live system (`ha_call_service`, `ha_config_set_*`, `ha_write_file`, `ha_restart`, `ha_remove_*`). Prefer read tools (`ha_get_*`, `ha_search`, `ha_eval_template`) unless a change was asked for.
- Last verified 2026-10-12: ha-mcp 8.6.0, HA core 2026.10.1, HAOS 18.3, 83 tools.
