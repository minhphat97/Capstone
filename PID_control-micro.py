import numpy as np
import time
import math
from adafruit_servokit import ServoKit
import keyboard
import board
import busio
import time
import adafruit_ds3502
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Laptop IP address (localhost)
nano_ip = '192.168.1.100'
nano_port = 12345

# Connect to the laptop's IP address and port
sock.connect((nano_ip, nano_port))
print("Connected to laptop at", (nano_ip, nano_port))

# ******DECLARE i2c FOR POT AND SETUP SERVO AND OpenCV******

servo_pin = 4
i2c=board.I2C()
ds3502 = adafruit_ds3502.DS3502(i2c) # this is i2c 1
i2c=busio.I2C(board.SCL_1,board.SDA_1) # this is i2c 0
kit = ServoKit(channels=16,i2c=i2c)


ds3502.wiper = 10 
rot_angle = 90
kit.servo[servo_pin].angle=rot_angle
print("ANGLE IS 90")
# print("SLEEPING FOR  S")
time.sleep(2)
ds3502.wiper = 20
time.sleep(2)

print("STARTING SERVO AND TRACKING COMPONENTS")
while(True):
    data_received = sock.recv(1024).decode()
    if not data_received:
        ds3502.wiper = 0
        print("ERROR: BALL LAUNCHER TURNING OFF")
        break
    distance, rot_angle, wiper, launch_ball= map(float, data_received.split(','))
    ds3502.wiper = wiper

    if launch_ball == 2:
        ds3502.wiper = 0
        print("BALL LAUNCHER TURNING OFF")
        break