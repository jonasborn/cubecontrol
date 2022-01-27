import devices.Switch
import sensors.THSensor
import time

last_change: int
last_value: bool = False
upper = 22.7
lower = 22.5


def init():
    global last_change
    last_change = time.time()
    sensors.THSensor.init()
    sensors.THSensor.add_listener(listen)
    print("added listener")


def listen(t, h):
    global last_change
    global last_value

    current_time = time.time()
    print("Current temperature: " + str(t))
    if current_time - last_change < 2:
        print("Lower than threshold: " + str(current_time - last_change))
        return

    if t < lower:
        if not last_value:
            print("Header on")
            devices.Switch.heater_on()
            last_change = time.time()
            last_value = True
        else:
            print("Heater on, no change")
    elif t > upper:
        if last_value:
            print("Heater off")
            devices.Switch.heater_off()
            last_change = time.time()
            last_value = False
        else:
            print("Heater off, no change")
    else:
        print("Between values, no change")
