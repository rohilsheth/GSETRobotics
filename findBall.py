
#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

motorLeft = LargeMotor('outC')
motorRight = LargeMotor('outB')

#if color = red then boolean = true

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

align()

goTillTarget(70, "left")

sleep(0.5)

goTillTarget(70, "right")

sleep(0.5)

findIRBall()





