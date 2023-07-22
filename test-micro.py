import numpy as np
import time
import math

import time

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
        if launch_ball == 2:
            print("TEST TURNING OFF")
            break
    except ValueError as e:
        print("Error while parsing data:", e)

conn.close()
sock.close()