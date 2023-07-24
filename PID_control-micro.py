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
port = 12347

# Connect to the laptop's IP address and port
# sock.bind((ip, port))
print("Connected to laptop at", (ip, port))
sock.bind((ip, port))
sock.listen(1)  # Listen for incoming connections, with a backlog of 1 connection
conn, addr = sock.accept()  # Accept an incoming connection)

# ******DECLARE i2c FOR POT AND SETUP SERVO AND OpenCV******

servo_pin = 4
i2c=board.I2C()
ds3502 = adafruit_ds3502.DS3502(i2c) # this is i2c 1
i2c=busio.I2C(board.SCL_1,board.SDA_1) # this is i2c 0
kit = ServoKit(channels=16,i2c=i2c)


ds3502.wiper = 20 
rot_angle = 90
kit.servo[servo_pin].angle=rot_angle
print("ANGLE IS 90")
# print("SLEEPING FOR  S")
time.sleep(2)
ds3502.wiper = 29
time.sleep(2)

print("STARTING SERVO AND TRACKING COMPONENTS")
while(True):
    print("inside loop ")
    data_received = conn.recv(4096)
    data_received = data_received.decode()
    if not data_received:
        ds3502.wiper = 0
        print("ERROR: BALL LAUNCHER TURNING OFF")
        break
    try:
            
        distance, rot_angle, wiper, launch_ball= map(float, data_received.split(','))
        ds3502.wiper = int(wiper)
        kit.servo[servo_pin].angle = rot_angle
        print("ROTATING ANGLE RECEIVED: ",rot_angle)

    # if launch_ball == 2:
    #     ds3502.wiper = 0
    #     kit.servo[servo_pin].angle = rot_angle
    #     print("BALL LAUNCHER TURNING OFF")
    #     break
    except ValueError as e:
        print("Error while parsing data:", e)


conn.close()
sock.close()
