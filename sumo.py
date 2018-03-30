#!/usr/bin/python3

from time import sleep
import sys, os

from ev3dev.ev3 import *

#========================= MOTOR =========================#

rightMotor = LargeMotor(OUTPUT_B)
leftMotor  = LargeMotor(OUTPUT_C)

#======================== SENSORS ========================#

ts1 = TouchSensor(INPUT_1);	    assert ts1.connected
ts4 = TouchSensor(INPUT_4);	    assert ts4.connected
cs  = ColorSensor();             assert cs.connected
us  = UltrasonicSensor();       assert us.connected
gs  = GyroSensor();		        assert gs.connected

gs.mode = 'GYRO-RATE'	# Changing the mode resets the gyro
gs.mode = 'GYRO-ANG'	# Set mode to return compass angle

cs.mode = "COL-REFLECT" # Set to sense reflected light

#========================= BUTTON ========================#
# EV3 Button State

btn = Button()

#===================== Move Straight =====================#
# Move Betsie straight forward

def moveStraight():
    leftMotor.duty_cycle_sp = 75
    rightMotor.duty_cycle_sp = 75

#========================= Stop ==========================#
# Stop Betsie

def stop():
    rightMotor.stop(stop_action='brake')
    leftMotor.stop(stop_action='brake')

#======================== Backup =========================#
# Back up Betsie for 2 seconds

def backup():
    rightMotor.run_timed(speed_sp=-500, time_sp=2000)
    leftMotor.run_timed(speed_sp=-500, time_sp=2000)
    rightMotor.wait_while('running')
    leftMotor.wait_while('running')

#======================== Detect =========================#
# Turn until Betsie detects something close in front of it

def initDetect(LR):
    distance = us.value();
    print("Distance: " + str(distance))
    while distance > 370:

        '''
        if LR == "left":
            dir = -1
        elif LR == "right":
            dir = 1
        '''

        leftMotor.duty_cycle_sp = 50 * dir
        rightMotor.duty_cycle_sp = -50 * dir
        distance = us.value();
        print("Distance: " + str(distance))

#===================== Detect Colour =====================#
# Stop and backup Betsie if the black line is detected

def detectColour():
    print("Color: " + str(cs.value()))
    if cs.value() < 30:
        stop()
        backup()
        #initDetect()

#===================== Left or Right =====================#
# Determine which direction to turn based on which button
# is pressed (left/right)

def checkLR():
    print("Choose left or right")
    while not btn.any():
        if btn.left:
            print("Left")
            return "left"
        elif btn.right:
            print("Right")
            return "right"


#===================== Initial / Main =====================#

print("Starting")
Sound.speak("Starting").wait()

while not btn.any():    # Wait for a button press then sleep
    time.sleep(0.5)     # for 3 seconds

print("Sleeping")
time.sleep(3)
print("Finished sleeping")

rightMotor.run_direct(duty_cycle_sp=0)
leftMotor.run_direct(duty_cycle_sp=0)


#LR = checkLR()     # Check to turn left or right
LR = "right"

initDetect(LR)

while not btn.any():
    detectColour()
    moveStraight()