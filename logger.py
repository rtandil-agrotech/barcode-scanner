# -------------------------- Setting logging basics -------------------------- #
import logging

def modbus_logger():
    f = open('logs/modbus_tcp.log', 'w').close() # clear file on first start

    _logger = logging.getLogger('modbus')
    _logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler('logs/modbus_tcp.log')
    fh.setLevel(logging.DEBUG)
    fh.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    fh.setFormatter(formatter)

    _logger.addHandler(fh)

    return _logger

def mqtt_logger():
    f = open('logs/mqtt.log', 'w').close() # clear file on first start

    _logger = logging.getLogger('mqtt')
    _logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler('logs/mqtt.log')
    fh.setLevel(logging.DEBUG)
    fh.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    fh.setFormatter(formatter)

    _logger.addHandler(fh)

    return _logger