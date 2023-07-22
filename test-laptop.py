import numpy as np
import cv2
import time
import math
from csv import writer
import socket
import keyboard
import pickle

# RUN $ hostname -I
# to detect ip adress of this device

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Replace 'ip address' with the actual IP address of the nano
ip = '192.168.1.74'
port = 12345

# Bind the socket to the nano's IP address and port
sock.connect((ip, port))

# Listen for ## three incoming connections: PID_control-micro.py, objectBallNano-laptop.py, objectBallFeeder-micro.py
# sock.listen(6)

# # Accept the first connection
# conn1, addr1 = sock.accept()
# print("Connected to the first client at", addr1)

# Accept the second connection
# conn2, addr2 = sock.accept()                    
# print("Connected to the second client at", addr2)

# Accept the third connection
# conn3, addr3 = sock.accept()
# print("Connected to the third client at", addr3)

distance = 2 #m
Px, Ix, Dx = -1/160, 0, 0
integral_x = 0
differential_x = 0
prev_x = 0

position_laucnher_x_direction = 30
Known_distance = 300 #cm
Known_width = 90 #cm

cap = cv2.VideoCapture(0)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap.set(3, 640)
cap.set(4, 480)
x_medium = 0
y_medium = 0
x = 0
y = 0
w = 0
h = 0
distance = 0
wiper = 0
print("ANGLE IS 90")
rot_angle = 90
# print("SLEEPING FOR  S")
wiper = 10
time.sleep(2)
wiper = 20
# GPIO.setmode(GPIO.BOARD)
# InPin = 15
# GPIO.setup(InPin, GPIO.IN)
# InPin2 = 16
# GPIO.setup(InPin2, GPIO.IN)

flag = 2
# wiper = 0
distance = 0
launch_ball=0
rot_angle2 = 0
temp = 0
print("STARTING BALL DETECTOR")
print("STARTING BALL LAUNCHER")
print("STARTING BALL FEEDER")
while(True):
    ret, frame = cap.read()
    height, width, _ = frame.shape
    center = int(width/2)
    boxes, weights = hog.detectMultiScale(frame,winStride=(8, 8), padding=(4, 4),scale=1.05)

    launch_ball = 0 # this will be 0 every time unless 4 is pressed in the keyboard
    
    # if x == 1 and y == 0:
    if keyboard.is_pressed("1"):
        flag = 1
        # print("a is pressed")
    # elif x == 1 and y == 1:
    elif keyboard.is_pressed("2"):
        flag = 2
        # print("s is pressed")
    # elif x == 0 and y == 1:
    elif keyboard.is_pressed("3"):
        flag = 3
        # print("d is pressed")
    if keyboard.is_pressed("4"):
        print("THREE (3) SECOND DELAY FOR NEXT LAUNCH BALL")
        launch_ball = 1  
    
    # ******SERVO ROTATING LAZY SUSAN******
    for (x, y, w, h) in boxes:
        temp = rot_angle
        if flag == 1:
            x_medium = int((x + x + w) / 2) - 200
            face_centre_x = x+w/2 - 200
            y_medium = int((y + y + h) / 2)
        elif flag == 2:
            x_medium = int((x + x + w) / 2) 
            face_centre_x = x+w/2 
            y_medium = int((y + y + h) / 2)
        elif flag == 3:
            x_medium = int((x + x + w) / 2) + 200
            face_centre_x = x+w/2 + 200
            y_medium = int((y + y + h) / 2)  

        cv2.line(frame, (x_medium, 0), (x_medium, 480), (255, 255, 0), 2)
        # face_centre_x = x+w/2 
        error_x = face_centre_x - 320
        if abs(error_x) > 15:
            rot_angle = rot_angle - error_x/43
        
        if rot_angle < 43:
            rot_angle = 43
            print("Servo out of range")
        
        if rot_angle > 137:
            rot_angle = 137
            print("Servo out of range")

        # kit.servo[servo_pin].angle = rot_angle  
        break

    # determine second_angle passed to objectBallFeeder.py
    # second_angle = rot_angle # NOT NEEDED, rot_angle already passed in connection
    # if rot_angle is NULL:


    # ******POT PERCENTAGE******

    if h > 350:
        wiper = 24
        distance = 2.7
    elif h > 330 and h <= 350:
        wiper = 28
        distance = 3.1
    elif h > 300 and h <= 330:
        wiper = 33
        distance = 3.6
    elif h > 280 and h <= 300:
        wiper = 38
        distance = 4.0
    elif h > 250 and h <= 280:
        wiper = 44
        distance = 4.4
    elif h > 220 and h <= 250:
        wiper = 50
        distance = 4.9
    elif h > 200 and h <= 220:
        wiper = 56
        distance = 5.3
    elif h > 190 and h <= 200:
        wiper = 61
        distance = 5.8
    elif h > 180 and h <= 190:
        wiper = 65
        distance = 6.4
    elif h <= 180:
        wiper = 70
        distance = 6.8
    # elif h > 164 and h <= 172:
    #     ds3502.wiper = 75
    #     config.distance = 7.3
    # elif h > 158 and h <= 164:
    #     ds3502.wiper = 78
    #     config.distance = 8
    # elif h > 152 and h <= 158:
    #     ds3502.wiper = 83 
    #     config.distance = 10
    # elif h > 145 and h <= 155:
    #     ds3502.wiper = 87
    #     config.distance = 12
    # elif h <= 145:
    #     ds3502.wiper = 90
    #     config.distance = 13

    # print("Height in image: ", h)
    # print("Wiper: ", ds3502.wiper)
    if rot_angle is not None and wiper is not None and launch_ball is not None and distance is not None:
        data_to_send = f"{distance},{rot_angle},{wiper},{launch_ball}" #
        sock.sendall(data_to_send.encode())
    # conn2.sendall(data_to_send.encode())
    # conn3.sendall(data_to_send.encode())

    cv2.imshow("Human", frame)
    #if keyboard.is_pressed("5"):
    if cv2.waitKey(1) & keyboard.is_pressed("0"):
        wiper = 0
        launch_ball = 2
        data_to_send = f"{distance},{rot_angle},{wiper},{launch_ball}"
        sock.sendall(data_to_send.encode())
        # conn2.sendall(data_to_send.encode())
        # conn3.sendall(data_to_send.encode())
        print("BALL LAUNCHER TURNING OFF")
        print("BALL DETECTOR TURNING OFF")
        print("BALL FEEDER TURNING OFF")
        break
    rot_angle = temp
cap.release()
cv2.destroyAllWindows()
sock.close()