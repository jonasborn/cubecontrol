import time
import adafruit_dht
import _thread

import Config

temperature: float
humidity: float
__last_errors: int
listeners: list = []


def init():
    _thread.start_new_thread(__main_loop, ())


def add_listener(listener):
    global listeners
    listeners.append(listener)


def __main_loop():
    global temperature
    global humidity
    global __last_errors
    global listeners

    dht_device = adafruit_dht.DHT22(Config.th_sensor_pin)
    while True:
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity
            __last_errors = 0
            for listener in listeners:
                listener(temperature, humidity)
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            __last_errors += 1
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dht_device.exit()
            raise error
        time.sleep(2.0)

