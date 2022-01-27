import _thread

from sds011 import SDS011
import time
from art import *

pm25: float = 0
pm10: float = 0

__sensor: SDS011


def init():
    global __sensor
    __sensor = SDS011("/dev/ttyUSB0", use_query_mode=True)
    _thread.start_new_thread(__main_loop, ())
    time.sleep(1)


def __main_loop():
    global pm25, pm10
    while True:
        query = __sensor.query()
        pm25 = query[0]
        pm10 = query[1]
        time.sleep(15)  # Allow time for the sensor to measure properly
