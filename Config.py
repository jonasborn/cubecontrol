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