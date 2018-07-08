#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

motorLeft = LargeMotor('outC')
motorRight = LargeMotor('outB')

#hello

def getBall():
    sleep(1)

def findBall():
    sleep(1)
def turn90Right():
    motorLeft.run_to_rel_pos(position_sp=460, speed_sp=900, stop_action="hold")
def turn90Left():
    motorRight.run_to_rel_pos(position_sp=460, speed_sp=900, stop_action="hold")

target = 450
us = UltrasonicSensor()
us.mode='US-DIST-CM'

while True:
  dist=us.value()
  if abs(dist-target) <= 30:
     motorLeft.stop(stop_action='hold')
     motorRight.stop(stop_action='hold')
     turn90Right()
     break
  elif dist > target:
     motorRight.run_forever(speed_sp=min(300,3*(dist-target)))
     motorLeft.run_forever(speed_sp=min(300,3*(dist-target)))
  else:
     motorRight.run_forever(speed_sp=max(-300,3*(dist-target)))
     motorLeft.run_forever(speed_sp=max(-300,3*(dist-target)))

sleep(0.5)

target = 100

while True:
  dist=us.value()
  if abs(dist-target) <= 30:
     motorLeft.stop(stop_action='hold')
     motorRight.stop(stop_action='hold')
     turn90Right()
     break
  elif dist > target:
     motorRight.run_forever(speed_sp=min(300,3*(dist-target)))
     motorLeft.run_forever(speed_sp=min(300,3*(dist-target)))
  else:
     motorRight.run_forever(speed_sp=max(-300,3*(dist-target)))
     motorLeft.run_forever(speed_sp=max(-300,3*(dist-target)))

sleep(0.5)

#room2 IR scan

motorRight.run_forever(speed_sp=300)
motorLeft.run_forever(speed_sp=300)

motorLeft.stop(stop_action="break")
motorRight.stop(stop_action="break")

ir = InfraredSensor()
ir.mode = 'IR-PROX'

target = 20

while True:
    distance = ir.value()
    if abs(distance-target) <= 5:
        Sound.beep()

