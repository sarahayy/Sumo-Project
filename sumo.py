#!/usr/bin/python3

from time import sleep
import sys, os

from ev3dev.ev3 import *

#Connect motors
rightMotor = LargeMotor(OUTPUT_B)
leftMotor  = LargeMotor(OUTPUT_C)

# Connect touch sensors.
#ts1 = TouchSensor(INPUT_1);	assert ts1.connected
#ts4 = TouchSensor(INPUT_4);	assert ts4.connected
us  = UltrasonicSensor();	assert us.connected
"""
gs  = GyroSensor();		assert gs.connected

gs.mode = 'GYRO-RATE'	# Changing the mode resets the gyro
gs.mode = 'GYRO-ANG'	# Set gyro mode to return compass angle


cs = ColorSensor();     assert cs.connected
"""

# EV3 Button State
btn = Button()

print("Starting")

'''
while not btn.any():
    time.sleep(0.5)
'''

print("Sleeping")
ev3.Sound.speak('ha ha').wait()

time.sleep(3)

print("Finished sleeping")

def check():

    distance = us.value();

    if distance <= 600:
        return True
    else:
        return False

def moveStraight():

    rightMotor.run_direct(duty_cycle_sp=75)
    leftMotor.run_direct(duty_cycle_sp=75)

def detect():

    distance = us.value();
    print(distance)
    while distance > 10:
        rightMotor.run_direct(duty_cycle_sp=10)

def stop():
    rightMotor.stop(stop_action='brake')
    leftMotor.stop(stop_action='brake')


while not btn.any():
        detect()
        moveStraight()


