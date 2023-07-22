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
socket.bind((ip, port))
socket.listen(1)  # Listen for incoming connections, with a backlog of 1 connection
conn, addr = socket.accept()  # Accept an incoming connection

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

conn.close()
socket.close()