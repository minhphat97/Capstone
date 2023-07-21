import numpy as np
import time
import math

import time

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Jetson Nano IP address (localhost)
nano_ip = '127.0.0.1'
nano_port = 12345

# Connect to the laptop's IP address and port
sock.connect((nano_ip, nano_port))
print("Connected to laptop at", (nano_ip, nano_port))

print("STARTING TEST")
while(True):
    data_received = sock.recv(1024).decode()
    if not data_received:
        print("ERROR: TEST TURNING OFF")
        break

    distance, rot_angle, wiper, launch_ball= map(float, data_received.split(','))
    print("Distance is ", distance)
    print

    if launch_ball == 2:
        print("TEST TURNING OFF")
        break