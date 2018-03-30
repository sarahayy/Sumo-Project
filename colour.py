#!/usr/bin/python3

from time import sleep
import sys, os

from ev3dev.ev3 import *

cl = ColorSensor();            assert cl.connected
cl.mode = "COL-REFLECT"

while True:
    print(cl.value())
    time.sleep(1)