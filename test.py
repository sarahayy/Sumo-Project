#!/usr/bin/python3

from time import sleep
import sys, os

from ev3dev.ev3 import *

#====================== MOTOR ======================#

rightMotor = LargeMotor(OUTPUT_B)
leftMotor  = LargeMotor(OUTPUT_C)

#================== Move Straight ==================#

def moveStraight():
    leftMotor.duty_cycle_sp = 75
    rightMotor.duty_cycle_sp = 75

def moveStraightAlt():
    leftMotor.run_forever(speed_sp=900)
    rightMotor.run_forever(speed_sp=900)

#====================== Stop =======================#

def stop():
    rightMotor.stop(stop_action='brake')
    leftMotor.stop(stop_action='brake')

#====================== Left =======================#

def left():
    leftMotor.duty_cycle_sp = -75
    rightMotor.duty_cycle_sp = 75

#===================== Right =======================#

def right():
    leftMotor.duty_cycle_sp = 75
    rightMotor.duty_cycle_sp = -75

#===================== Button ======================#

def testButton():
    while not btn.any():
        if btn.left:
            print("Left")
        elif btn.right:
            print("Right")

    '''
    print(btn.buttons_pressed)
    
    while not btn.check_buttons(buttons=['left','right']):
        if btn.left:
            print("Left")
        elif btn.right:
            print("Right")
         
    '''
    
#====================== Main =======================#

btn = Button()
clicked = False
while (clicked == False):
    if btn.left:
        print("Left")
        clicked = True
    elif btn.right:
        print("Right")
        clicked = True
    print("waiting")
    time.sleep(0.1)


print("End")