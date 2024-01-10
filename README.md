# Acknowledgement
This is a fork of https://github.com/ckarrie/ckw-ha-gs108e with reduced number of ports and some changes to the html parser

# lb3-ha-gs105e
HomeAssistant Netgear Switch Integration

## What it does
Grabs statistical network data from your Netgear GS105Ev2

## How it works
1. Connects to the Switch and asks for a cookie (`http://IP_OF_SWITCH/login.cgi`)
2. HTTP-Request send to the Switch twice (`http://IP_OF_SWITCH/portStatistics.cgi`)

## Which statistics
- overall Switch statistics as attributes
  - `switch_ip` - IP of the Switch
  - `response_time_s` - Response time of two requests send to the Switch to calculate the traffic speed
  - `sum_port_traffic_rx` - Received traffic (sum all ports)
  - `sum_port_traffic_tx` - Transferred traffic (sum all ports)
  - `sum_port_traffic_crc_err` - CRC Errors (sum all ports)
  - `sum_port_speed_bps_rx` - Received traffic speed (bit/s)
  - `sum_port_speed_bps_rx` - Transferred traffic speed (bit/s)
  - `sum_port_speed_bps_io` - Received and transferred traffic speed 
  - `ports` - List of statistics for each Switch port
- statistics for each Port (5 Ports for GS105Ev2) as attributes
  - `port_{port}_traffic_rx_mbytes` - Megabytes received during `response_time_s`
  - `port_{port}_traffic_tx_mbytes` - Megabytes transferred during `response_time_s`
  - `port_{port}_speed_rx_mbytes` - Megabytes received per 1 second
  - `port_{port}_speed_tx_mbytes` - Megabytes transferred per 1 second
  - `port_{port}_speed_io_mbytes` - Megabytes throughput per 1 second
  - `port_{port}_sum_rx_mbytes` - Megabytes totally received since Switch reboot
  - `port_{port}_sum_tx_mbytes` - Megabytes totally transferred since Switch reboot
  - ~~`crc_errors` - CRC counter~~


## How to integrate in your HomeAssistant

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Lulubelle3&repository=lb3-ha-gs105e&category=integration)

1. Goto [HACS > Integrations](http://homeassistant.lan/redirect/hacs/integrations)
2. Click on the right corner on the vertical dots and select "Custom Repositories"
3. Add "https://github.com/Lulubelle3/lb3-ha-gs105e" as Integration

After adding the integration go to [Add Integration](https://my.home-assistant.io/redirect/integrations/) and select **Netgear GS105e Integration**.


![image](https://user-images.githubusercontent.com/4140156/118571964-9ac0fa80-b77f-11eb-951e-a5e393157bd0.png)

## GS105e library

```python3
import gs105e
import time
sw = gs105e.GS105Switch("192.168.178.8", "password")
sw.get_login_cookie()

while True:
    sw.get_switch_infos()["port_1_sum_rx_mbytes"]
    time.sleep(1)




```


