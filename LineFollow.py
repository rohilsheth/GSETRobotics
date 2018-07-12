#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

lightSensor = LightSensor()
#lightSensor.mode = 'REFLECT'
lineEdgeVal = 470 #wanted area
motorLeft = LargeMotor('outB')
motorRight = LargeMotor('outC')
LeftToRight = False
cl = ColorSensor();
cl.mode = 'COL-COLOR'
colors=('unknown','black','blue','green','yellow','red','white','brown')
obsticalHit = False

lineTolerance = 20 #+- 20
commonSpeed = 450
rightSpeed = commonSpeed
leftSpeed = commonSpeed
lcd = Screen()

us = UltrasonicSensor()
us.mode='US-DIST-CM'

Leds.set_color(Leds.LEFT, Leds.GREEN)
sleep(0.1)
Leds.set_color(Leds.LEFT, Leds.ORANGE)
sleep(0.5)
Leds.set_color(Leds.LEFT, Leds.GREEN)

inHouse = False

def runMotor(speedLeft, speedRight):
    motorLeft.run_forever(speed_sp = min(int(speedLeft), 900))
    motorRight.run_forever(speed_sp= min(int(speedRight), 900))

def followLine():
    counterAdderLeft = 8
    counterAdderRight = 8
    sensorVal = lightSensor.value()
    changeScalarRight = 4
    changeScalarLeft = 4
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
        leftSpeed = -30#100
        rightCounter += counterAdderRight
        leftCounter = 2


    # turn right?
    elif sensorVal < (lineEdgeVal - lineTolerance):
    # turn left?
        # leftSpeed = 450
        LeftToRight = False
        onLeft = False
        leftSpeed += int((((abs(lineEdgeVal - sensorVal))/changeScalarLeft))/leftCounter)
        print("left speed: " + str(leftSpeed))
        rightSpeed = -30
        leftCounter += counterAdderLeft
        rightCounter = 2
    else:
        LeftToRight = False
        onLeft = True
        leftSpeed = commonSpeed
        rightSpeed = commonSpeed
        leftCounter = 1
        rightCounter = 1

    runMotor(leftSpeed, rightSpeed)

def semiCircle():

    motorLeft.run_forever(speed_sp = 500)
    motorLeft.run_forever(speed_sp = 300)
    sleep(5)

    motorLeft.run_forever(speed_sp = 300)
    motorLeft.run_forever(speed_sp = -300)
    sleep(2)

    motorLeft.stop(stop_action='hold')
    motorRight.stop(stop_action='hold')

def avoidence():
    if abs(us.value) <= 18 and obsticalHit == False:
        motorLeft.stop(stop_action='hold')
        motorRight.stop(stop_action='hold')
        semiCircle()
        obsticalHit == True
def colorsense():
    colorname=colors[cl.value()]
    if(colorname=="green"):
        Sound.beep()

def main():
    while True:
        # lcd.draw.text((48,13), str(leftSpeed) + ", " + str(rightSpeed))
        # lcd.update()
        # lcd.clear()
        colorsense()
        if inHouse == False:
            followLine()
            avoidence()

        sleep(.01)
main(1000)
