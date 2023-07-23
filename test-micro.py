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

# Accept connections from any port
ip = ""
port = 12345

# Connect to the laptop's IP address and port
# sock.bind((ip, port))
print("Connected to laptop at", (ip, port))
sock.bind((ip, port))
sock.listen(1)  # Listen for incoming connections, with a backlog of 1 connection
conn, addr = sock.accept()  # Accept an incoming connection

servo_pin = 4 # pins are 4 & 12
i2c=busio.I2C(board.SCL_1,board.SDA_1)
kit = ServoKit(channels=16,i2c=i2c)


print("STARTING TEST")
while(True):
    data_received = conn.recv(4096)
    data_received = data_received.decode()
    if not data_received:
        print("ERROR: TEST TURNING OFF")
        break

    try:
        distance, rot_angle, wiper, launch_ball = map(float, data_received.split(','))
        print("Distance is ", distance)
        print("Rotational Angle:", rot_angle)
        print("Wiper:", wiper)
        print("Launch Ball:", launch_ball)
        kit.servo[servo_pin].angle = rot_angle
        if launch_ball == 2:
            print("TEST TURNING OFF")
            kit.servo[servo_pin].angle = rot_angle
            break
    except ValueError as e:
        print("Error while parsing data:", e)

conn.close()
sock.close()
