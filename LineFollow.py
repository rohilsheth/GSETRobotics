#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

lightSensor = LightSensor() 
#lightSensor.mode = 'REFLECT'
lineEdgeVal = 470 #wanted area

lineTolerance = 20 #+- 20

lcd = Screen()


Leds.set_color(Leds.LEFT, Leds.GREEN)
sleep(0.1)
Leds.set_color(Leds.LEFT, Leds.ORANGE)
sleep(0.5)
Leds.set_color(Leds.LEFT, Leds.GREEN)


while True:
    lcd.draw.text((48,13), str(lightSensor.value()))
    lcd.update()
    lcd.clear()
    sleep(.1)
    
    if lightSensor.value() > lineEdgeVal + lineTolerance:
        	
    # turn right?
    elif lightSensor.value() < lineEdgeVal - lineTolerance:
    # turn left?
