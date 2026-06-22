#!/usr/bin/env bash
# setup-secrets.sh
# Generates secrets.yaml from environment variables.
# Usage: SAMBA_PASSWORD=... WIFI_SSID=... WIFI_PASSWORD=... ./setup-secrets.sh

set -euo pipefail

: "${SAMBA_PASSWORD:?SAMBA_PASSWORD environment variable is required}"
: "${WIFI_SSID:?WIFI_SSID environment variable is required}"
: "${WIFI_PASSWORD:?WIFI_PASSWORD environment variable is required}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cat > "${SCRIPT_DIR}/secrets.yaml" <<EOF
samba_password: ${SAMBA_PASSWORD}
wifi_ssid: ${WIFI_SSID}
wifi_password: ${WIFI_PASSWORD}
EOF

echo "secrets.yaml written."
