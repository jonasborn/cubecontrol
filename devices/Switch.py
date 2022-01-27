import logging
import time

import serial

from config import Config

com: serial.Serial


def init():
    print("Inited")
    global com
    if com is not None:  # Return, if already initialized
        return
    com = serial.Serial()
    com.port = '/dev/ttyUSB0'
    com.baudrate = 9600
    com.parity = serial.PARITY_NONE
    com.bytesize = serial.EIGHTBITS
    com.open()
    logging.debug("Requesting return to menu")
    com.write(";;;;;\r".encode('ascii'))
    com.flush()
    time.sleep(1)
    logging.debug("Requesting submenu 5")
    com.write("5\r".encode('ascii'))
    com.flush()
    time.sleep(.5)
    time.sleep(3)


def change(port: int, state: bool):
    global com
    init()
    if state:
        logging.debug("Sending \"On\" request for outlet " + str(port))
        com.write(("On " + str(port) + "\r").encode('ascii'))
    else:
        logging.debug("Sending \"Off\" request for outlet " + str(port))
        com.write(("Off " + str(port) + "\r").encode('ascii'))
    com.flush()
    time.sleep(0.5)
    com.write("Y\r".encode('ascii'))
    time.sleep(0.3)
    com.flush()


def light_on():
    change(Config.light_port, True)


def light_off():
    change(Config.light_port, False)


def printer_on():
    change(Config.printer_port, True)


def printer_off():
    change(Config.printer_port, False)


def heater_on():
    change(Config.heater_port, True)


def heater_off():
    change(Config.heater_port, False)


def close():
    global com
    com.close()
    com = None

