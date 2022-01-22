import time
import RPi.GPIO as GPIO
import _thread

dark: bool = False
light: bool = True


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN)
    _thread.start_new_thread(__main_loop, ())


def __main_loop():
    global dark
    global light
    while True:
        if GPIO.input(17) == 1:
            dark = True
            light = False
        else:
            dark = False
            light = True
        time.sleep(1)
