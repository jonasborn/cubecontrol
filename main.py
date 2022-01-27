import time
import tools.Rules

from sensors import THSensor
from sensors import LightSensor
from sensors import ToneSensor
from sensors import PMSensor
from sensors import PrinterSensor
from sensors import ButtonSensor


THSensor.init()
LightSensor.init()
ToneSensor.init()
PMSensor.init()
ButtonSensor.init()
PrinterSensor.init()

tools.Rules.load("decisions.csv")

while True:
    print(
        tools.Rules.find(
            THSensor.temperature,
            ToneSensor.tone,
            THSensor.humidity,
            PMSensor.pm25,
            PMSensor.pm10,
            ButtonSensor.active,
            PrinterSensor.state
        )
    )
    time.sleep(.5)
