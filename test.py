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

#====================== Stop =======================#

def stop():
    rightMotor.stop(stop_action='brake')
    leftMotor.stop(stop_action='brake')

