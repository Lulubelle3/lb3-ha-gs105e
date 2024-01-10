from datetime import timedelta
from homeassistant.const import Platform


DOMAIN = 'lb3_hass_gs105e'

PLATFORMS = [
    Platform.SENSOR,
]

DEFAULT_NAME = "Netgear GS105E Switch"
SCAN_INTERVAL = 10
DEFAULT_CONF_TIMEOUT = timedelta(seconds=15)
DEFAULT_HOST = "192.168.178.5"
DEFAULT_USER = "admin"
DEFAULT_PASSWORD = 'password'
KEY_COORDINATOR_SWITCH_INFOS = 'coordinator_switch_infos'
KEY_SWITCH = "switch"
