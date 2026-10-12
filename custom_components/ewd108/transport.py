"""Connection parameters and guards for HA's shared Modbus API."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any
from urllib.parse import urlsplit

if TYPE_CHECKING:
    from collections.abc import Mapping

from modbus_connection import ModbusSerialParams, ModbusTcpParams

from .const import CONNECTION_TYPE_RTU_OVER_TCP, CONNECTION_TYPE_SERIAL


class LegacyHubConflictError(ValueError):
    """A legacy YAML poller would compete with the shared connection."""


def connection_params(config: dict[str, Any]) -> ModbusSerialParams | ModbusTcpParams:
    """Build transport settings without opening a connection."""
    if config["connection_type"] == CONNECTION_TYPE_SERIAL:
        return ModbusSerialParams(
            device=config["serial_port"],
            baudrate=config["baudrate"],
            bytesize=config["bytesize"],
            parity=config["parity"],
            stopbits=config["stopbits"],
        )
    if config["connection_type"] == CONNECTION_TYPE_RTU_OVER_TCP:
        host = config["host"].strip().lower()
        host = f"[{host}]" if ":" in host else host
        return ModbusSerialParams(
            device=f"socket://{host}:{int(config['port'])}", baudrate=115200
        )
    return ModbusTcpParams(host=config["host"].strip(), port=int(config["port"]))


def check_legacy_hubs(config: dict[str, Any], hubs: list[dict[str, Any]]) -> None:
    """Require migration of a YAML hub before opening its endpoint again."""
    for hub in hubs:
        if config["connection_type"] == CONNECTION_TYPE_SERIAL:
            same_endpoint = hub.get("type") == "serial" and hub.get(
                "port"
            ) == config.get("serial_port")
        else:
            same_endpoint = (
                hub.get("type") in {"tcp", "rtuovertcp"}
                and str(hub.get("host", "")).strip().lower()
                == config["host"].strip().lower()
                and int(hub.get("port", 502)) == int(config["port"])
            )
        if same_endpoint:
            msg = (
                f"Remove and reload legacy Modbus hub {hub.get('name', '')!r} "
                "before using this connection"
            )
            raise LegacyHubConflictError(msg)


def physical_endpoint(params: ModbusSerialParams | ModbusTcpParams) -> tuple:
    """Compare socket-carried RTU with the same endpoint in YAML hubs."""
    if isinstance(params, ModbusTcpParams):
        return ("tcp", params.host.lower(), params.port)
    if params.device.startswith("socket://"):
        endpoint = urlsplit(params.device)
        return ("tcp", endpoint.hostname, endpoint.port)
    return ("serial", params.device)


def check_running_legacy_hubs(config: dict[str, Any], hubs: Mapping[str, Any]) -> None:
    """Also catch hubs still running after YAML removal but before reload."""
    endpoint = physical_endpoint(connection_params(config))
    for name, hub in hubs.items():
        hub_endpoint = hub.endpoint
        if hub_endpoint[0] == "serial" and hub_endpoint[1].startswith("socket://"):
            url = urlsplit(hub_endpoint[1])
            hub_endpoint = ("tcp", url.hostname, url.port)
        if endpoint == hub_endpoint:
            msg = f"Reload Modbus to remove legacy hub {name!r} before continuing"
            raise LegacyHubConflictError(msg)
