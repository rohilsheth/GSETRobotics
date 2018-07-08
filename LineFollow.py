#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

lightSensor = LightSensor() 
#lightSensor.mode = 'REFLECT'
lineEdgeVal = 470 #wanted area
motorLeft = LargeMotor('outB')
motorRight = LargeMotor('outC')
LeftToRight = False

lineTolerance = 20 #+- 20
commonSpeed = 350
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
    counterAdderLeft = 4
    counterAdderRight = 4
    sensorVal = lightSensor.value()
    changeScalarRight = 11
    changeScalarLeft = 11
    leftCounter = 1
    rightCounter = 1
    global onLeft
    global commonSpeed
    global leftSpeed
    global rightSpeed
    global lineEdgeVal

    if  sensorVal > (lineEdgeVal + lineTolerance):
        LeftToRight = True
        rightSpeed += int((((abs(lineEdgeVal - sensorVal))/changeScalarRight))/rightCounter)
        # rightSpeed = 450
        print("right speed: " + str(rightSpeed))
        leftSpeed = -20#100
        rightCounter += counterAdderRight
        leftCounter = 1
        

    # turn right?
    elif sensorVal < (lineEdgeVal - lineTolerance):
    # turn left?
        # leftSpeed = 450
        LeftToRight = False
        onLeft = False
        leftSpeed += int((((abs(lineEdgeVal - sensorVal))/changeScalarLeft))/leftCounter)
        print("left speed: " + str(leftSpeed))
        rightSpeed = -20
        leftCounter += counterAdderLeft
        rightCounter = 1
    else:
        LeftToRight = False
        onLeft = True
        leftSpeed = commonSpeed
        rightSpeed = commonSpeed
        leftCounter = 1
        rightCounter = 1

    runMotor(leftSpeed, rightSpeed)




def main(shutoff):
    while True:
        lcd.draw.text((48,13), str(leftSpeed) + ", " + str(rightSpeed))
        lcd.update()
        lcd.clear()
        followLine()
        sleep(.01)
main(1000)