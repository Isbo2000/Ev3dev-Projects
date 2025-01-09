#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *

#set up inputs
irSensor = InfraredSensor(INPUT_1)
colorSensor = ColorSensor(INPUT_4)

#set up outputs
leftMotor = LargeMotor(OUTPUT_B)
rightMotor = LargeMotor(OUTPUT_A)
#set up tank controls
tankDrive = MoveTank(OUTPUT_B, OUTPUT_A)

while True:
    if (irSensor.top_left(1)):
        leftMotor.on(100)
    elif (irSensor.bottom_left(1)):
        leftMotor.on(-100)
    else:
        leftMotor.off()
    
    if (irSensor.top_right(1)):
        rightMotor.on(100)
    elif (irSensor.bottom_right(1)):
        rightMotor.on(-100)
    else:
        rightMotor.off()