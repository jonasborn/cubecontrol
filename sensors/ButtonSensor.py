import _thread
import time

from RPi import GPIO

active = False

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    _thread.start_new_thread(__main_loop, ())
    time.sleep(.5)

def __main_loop():
    global active
    while True:
        active = (GPIO.input(21) == 0)
        time.sleep(.5)
