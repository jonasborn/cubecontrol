import board

"""

       + PWR-Button
       |
       |         + TH-Sensor - (BROWN)
       |         |
       +         +
   5 5 0 X X | X 0 X X 0 X | X X . 0 X | 0 X X X
   3 X X X 0 | X X X 3 X X | X 0 . X X | X X X 0
   + + +   +   +     +
   | | |   |   |     ++L-Sensor + (RED)
   | | |   |   |
   | | |   |   ++ L-Sensor D (GREEN)
   | | |   |
   | | |   ++ L-Sensor -
   | | |
   | | + PWR-Button
   | |
   | + TH-Sensor D (YELLOW)
   |
   + TH-Sensor + (RED)


"""

th_sensor_pin = board.D2
light_port = 1
printer_port = 2
filter_port = 3
heater_port = 4

button_pin = 21

printer_url = "http://localhost"
printer_key = "4274A18266554871A9DE91D4CF98BA0A"

alarm_device = "USB Device 0x46d:0x81b: Audio (hw:1,0)"
alarm_sampling_rate = 48000
