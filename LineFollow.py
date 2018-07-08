#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

lightSensor = LightSensor() 
#lightSensor.mode = 'REFLECT'
lineEdgeVal = 470 #wanted area
motorLeft = LargeMotor('outB')
motorRight = LargeMotor('outC')


lineTolerance = 40 #+- 20
commonSpeed = 200
rightSpeed = commonSpeed
leftSpeed = commonSpeed
lcd = Screen()


Leds.set_color(Leds.LEFT, Leds.GREEN)
sleep(0.1)
Leds.set_color(Leds.LEFT, Leds.ORANGE)
sleep(0.5)
Leds.set_color(Leds.LEFT, Leds.GREEN)


def runMotor(speedLeft, speedRight):
    motorLeft.run_forever(speed_sp = min(int(speedLeft), 900))
    motorRight.run_forever(speed_sp= min(int(speedRight), 900))
    
def followLine():
    sensorVal = lightSensor.value()
    changeScalarRight = .5
    changeScalarLeft = 1
    global commonSpeed
    global leftSpeed
    global rightSpeed
    global lineEdgeVal

    if  sensorVal > (lineEdgeVal + lineTolerance):
        rightSpeed += int((abs(lineEdgeVal - sensorVal))/changeScalarRight)
        print(rightSpeed)
        leftSpeed = commonSpeed
    # turn right?
    elif sensorVal < (lineEdgeVal - lineTolerance):
    # turn left?
        leftSpeed += int((abs(lineEdgeVal - sensorVal))/changeScalarLeft)
        print(leftSpeed)
        rightSpeed = commonSpeed
    else:
        leftSpeed = commonSpeed
        rightSpeed = commonSpeed

    runMotor(leftSpeed, rightSpeed)




def main(shutoff):
    while True:
        lcd.draw.text((48,13), str(lightSensor.value()))
        lcd.update()
        lcd.clear()
        followLine()
        sleep(.1)
        i += 1
    motorLeft.stop(stop_action = "coast")
    motorRight.stop(stop_action = "coast")
main(1000)