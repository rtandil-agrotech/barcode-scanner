from configparser import ConfigParser
from datetime import datetime
import paho.mqtt.client as mqtt
from logger import mqtt_logger
import json

# ------------------------------- Setup Logger ------------------------------- #
_logger = mqtt_logger()

# --------------------------- Setting Config Parser -------------------------- #
config = ConfigParser()
config.read('mqtt.ini')

host = config.get('DEFAULT', 'host')
port = int(config.get('DEFAULT', 'port'))

baseTopic = config.get('DEFAULT', 'topic')

# ---------------------------- On Connect Handler ---------------------------- #


def on_connect(client, userdata, flags, reason_code):
    _logger.debug(f"Connected with result code {reason_code}")


def on_disconnect(client, userdata, rc):
    _logger.debug(f"Disconnect with result code {rc}")

# ------------------------------ On Log Handler ------------------------------ #


def on_log(client, userdata, paho_log_level, messages):
    if paho_log_level == mqtt.LogLevel.MQTT_LOG_ERR:
        _logger.error(messages)

# ---------------------------- Message Constructor --------------------------- #


def mqtt_message_constructor(barcode: str):
    now = datetime.now()

    # Split barcode, check first character
    if barcode.startswith('!'):
        barcode_stripped = barcode[1:]
        source = 'Loading'
    elif barcode.startswith('@'):
        barcode_stripped = barcode[1:]
        source = 'Unloading'
    elif barcode.startswith('#'):
        barcode_stripped = barcode[1:]
        source = 'Assembly'
    else:
        barcode_stripped = barcode
        source = 'Unknown'

    data = {
        "barcodeScanned": barcode_stripped,
        "source": source,
        "time": int(datetime.timestamp(now)),
        "addTime": now.strftime('%Y-%m-%d %H:%M:%S'),
    }

    return json.dumps(data)

# ----------------------------------- Start ---------------------------------- #


def setup_mqtt():
    mqtt_con = mqtt.Client()
    mqtt_con.enable_logger()

    mqtt_con.on_connect = on_connect
    mqtt_con.on_disconnect = on_disconnect
    mqtt_con.on_log = on_log

    mqtt_con.connect(host, port=port, keepalive=60)

    return mqtt_con
