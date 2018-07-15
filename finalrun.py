#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
import time

colorHit = 0

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
commonSpeed = 380
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
def getBall():
    sleep(1)

def findBall():
    sleep(1)
def turn90Right():
    motorLeft.run_to_rel_pos(position_sp=550, speed_sp=900, stop_action="hold")
def turn90Left():
    motorRight.run_to_rel_pos(position_sp=550, speed_sp=900, stop_action="hold")
def goTillTarget(targetinput, leftOrRight):
    target = targetinput
    us = UltrasonicSensor()
    us.mode = 'US-DIST-CM'
    while True:
        dist = us.value()
        if abs(dist - target) <= 30:
            motorLeft.stop(stop_action='hold')
            motorRight.stop(stop_action='hold')
            if leftOrRight == "left":
                turn90Left()
            if leftOrRight == "right":
                turn90Right()
            break
        elif dist > target:
            motorRight.run_forever(speed_sp=min(300, 3 * (dist - target)))
            motorLeft.run_forever(speed_sp=min(300, 3 * (dist - target)))
        else:
            motorRight.run_forever(speed_sp=max(-300, 3 * (dist - target)))
            motorLeft.run_forever(speed_sp=max(-300, 3 * (dist - target)))
def findIRBall()
    ir = Sensor(address='in3:i2c8', driver_name='ht-nxt-ir-seek-v2')
    ir.mode = 'AC'
    direction = ir.value()
    if (direction == 5) or (direction == 4) or (direction == 6):
        # play around with this value
        target = 40
        while True:
            dist = us.value()
            if abs(dist - target) <= 30:
                motorLeft.stop(stop_action='hold')
                motorRight.stop(stop_action='hold')
                sleep(0.5)
                break
            elif dist > target:
                motorRight.run_forever(speed_sp=min(300, 3 * (dist - target)))
                motorLeft.run_forever(speed_sp=min(300, 3 * (dist - target)))
            else:
                motorRight.run_forever(speed_sp=max(-300, 3 * (dist - target)))
                motorLeft.run_forever(speed_sp=max(-300, 3 * (dist - target)))

def align():
    motorRight.run_to_rel_pos(position_sp=600, speed_sp=200, stop_action="hold")
    motorLeft.run_to_rel_pos(position_sp=600, speed_sp=200, stop_action="hold")
    sleep(0.5)

    motorRight.run_to_rel_pos(position_sp=-2000, speed_sp=700, stop_action="hold")
    motorLeft.run_to_rel_pos(position_sp=-2000, speed_sp=700, stop_action="hold")
    sleep(0.5)

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
        # print("right speed: " + str(rightSpeed))
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
        # print("left speed: " + str(leftSpeed))
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

def goAround():
#CHANGE THIS SHIZZ
    # motorLeft.run_forever(speed_sp = -300)
    # motorRight.run_forever(speed_sp = -300)
    # sleep(.5)
    motorLeft.stop(stop_action='hold')
    motorRight.stop(stop_action='hold')
    motorRight.run_to_rel_pos(position_sp=420, speed_sp=900, stop_action="hold") # RIGHT

    sleep(1.5)
    motorLeft.run_forever(speed_sp = 300)
    motorRight.run_forever(speed_sp = 300)
    sleep(.6)
    motorLeft.stop(stop_action='hold')
    motorRight.stop(stop_action='hold')
    sleep(1)
    motorLeft.run_to_rel_pos(position_sp=420, speed_sp=900, stop_action="hold") #LEFT
    sleep(1.5)
    motorLeft.run_forever(speed_sp = 300)
    motorRight.run_forever(speed_sp = 300)
    sleep(1)
    motorLeft.stop(stop_action='hold')
    motorRight.stop(stop_action='hold')
    motorLeft.run_to_rel_pos(position_sp=350, speed_sp=900, stop_action="hold") #LEFT
    sleep(1.5)
    motorLeft.run_forever(speed_sp = 300)
    motorRight.run_forever(speed_sp = 300)
    sleep(.8)
    motorLeft.stop(stop_action='hold')
    motorRight.stop(stop_action='hold')
    motorRight.run_to_rel_pos(position_sp=420, speed_sp=900, stop_action="hold") #RIGHT
    sleep(1)

def avoidence():
    dist = us.value()
    # print("distance: " + str(dist))
    if dist <= 100 and obsticalHit == False:
        print("HEY WATER BTL")
        motorLeft.stop(stop_action='hold')
        motorRight.stop(stop_action='hold')
        goAround()
                # obsticalHit == True
def colorsense():
    global colorHit
    colorname=colors[cl.value()]
    print("COLOR VALUE: " + str(colorname))
    if(time.time() - colorHit > 1.5):
    if(colorname=="green" or colorname=="yellow"):
        Sound.beep()
        colorHit = time.time()
    if(colorname=="red")
        inHouse=True

def main():
    while True:
                # lcd.draw.text((48,13), str(leftSpeed) + ", " + str(rightSpeed))
                # lcd.update()
                # lcd.clear()

    if inHouse == False:
        followLine()
        colorsense()
        avoidence()
    if inHouse == True:
        align()
        goTillTarget(70, "left")
        sleep(0.5)
        goTillTarget(70, "right")
        sleep(0.5)
        findIRBall()
        sleep(.01)
main()
