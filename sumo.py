#!/usr/bin/python3

from time import sleep
import sys, os

from ev3dev.ev3 import *

#========================= MOTOR =========================#

rightMotor = LargeMotor(OUTPUT_B)
leftMotor  = LargeMotor(OUTPUT_C)

#======================== SENSORS ========================#

#ts1 = TouchSensor(INPUT_1);	    assert ts1.connected
#ts4 = TouchSensor(INPUT_4);	    assert ts4.connected
cs  = ColorSensor();                assert cs.connected
us  = UltrasonicSensor();           assert us.connected
#gs  = GyroSensor();		        assert gs.connected

#gs.mode = 'GYRO-RATE'	# Changing the mode resets the gyro
#gs.mode = 'GYRO-ANG'	# Set mode to return compass angle

cs.mode = "COL-REFLECT" # Set to sense reflected light

#========================= BUTTON ========================#
# EV3 Button State

btn = Button()

#===================== Move Straight =====================#
# Move Betsie straight forward

def moveStraight():
    rightMotor.run_direct(duty_cycle_sp=75)
    leftMotor.run_direct(duty_cycle_sp=75)

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


        if LR == "left":
            dir = 1
            print("Left")
        elif LR == "right":
            dir = -1
            print("Right")

        rightMotor.run_direct(duty_cycle_sp=-50*dir)
        leftMotor.run_direct(duty_cycle_sp=50*dir)

        distance = us.value();
        print("Distance: " + str(distance))

#===================== Detect Colour =====================#
# Stop and backup Betsie if the black line is detected

def detectColour():
    print("Detecting Colour")
    print("Color: " + str(cs.value()))
    if cs.value() < 30:
        stop()
        backup()
        moveStraight()

#===================== Left or Right =====================#
# Determine which direction to turn based on which button
# is pressed (left/right)

def checkLR():
    clicked = False
    while (clicked == False):
        if btn.left:
            print("Left")
            clicked = True
            return "left"
        elif btn.right:
            print("Right")
            clicked = True
            return "right"
        time.sleep(0.1)
        print("Waiting for input. Choose left or right.")


#===================== Initial / Main =====================#

print("Starting")
Sound.speak("Starting bitches").wait()


LR = checkLR()     # Check to turn left or right

print("Sleeping")
time.sleep(3)
print("Finished sleeping")

rightMotor.run_direct(duty_cycle_sp=0)
leftMotor.run_direct(duty_cycle_sp=0)


while not btn.any():
    detectColour()
    initDetect(LR)
    moveStraight()