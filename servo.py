# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 180):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(1)
    for angle in range(180, 0, -180):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(1)