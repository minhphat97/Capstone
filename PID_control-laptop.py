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
print("STARTING CONNECTIONS")
# ******************************************

# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Replace 'ip address' with the actual IP address of the nano
# ip = '192.168.1.74'
# port = 12345

# # Bind the socket to the nano's IP address and port
# sock.connect((ip, port))

# ****************************************

# List of server IP addresses and corresponding ports
servers = [
    ('207.23.178.64', 12346),  # Replace with the actual IP and port of server 1
    # ('207.23.178.64', 12347),  # May need to connect to the nano twice
    # ('127.0.0.1', 12345),  # IP address of local connection
    # Add more server IP addresses and ports as needed
]

# Create a list to store the connections
connections = []

# Connect to each server
for server_ip, server_port in servers:
    try:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the server
        sock.connect((server_ip, server_port))
        
        # Append the connection to the list
        connections.append((sock, (server_ip, server_port)))
        
        print("Connected to server at", (server_ip, server_port))
    except Exception as e:
        print(f"Failed to connect to server at {server_ip}:{server_port}: {e}")


distance = 2 #m
Px, Ix, Dx = -1/160, 0, 0
integral_x = 0
differential_x = 0
prev_x = 0
count = 0

position_laucnher_x_direction = 30
Known_distance = 300 #cm
Known_width = 90 #cm

# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("/dev/v4l/by-id/usb-GENERAL_GENERAL_WEBCAM_JH0319_20200710_v012-video-index0")
cap = cv2.VideoCapture("/dev/v4l/by-id/usb-046d_0825_EC51DD20-video-index0")

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
print("STARTING BALL DETECTOR")
print("STARTING BALL LAUNCHER")
print("STARTING BALL FEEDER")
while(True):
    count = count + 1
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
        print("ONE (1) SECOND DELAY FOR NEXT LAUNCH BALL")
        launch_ball = 1  
    
    # ******SERVO ROTATING LAZY SUSAN******
    for (x, y, w, h) in boxes:
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

        if boxes.any():
            # print(rot_angle)
            if abs(error_x) > 15:
                rot_angle = rot_angle - error_x/120
            
            if rot_angle < 43:
                rot_angle = 43
                print("Servo out of range: ", rot_angle)
            
            if rot_angle > 137:
                rot_angle = 137
                print("Servo out of range: ", rot_angle)

        # kit.servo[servo_pin].angle = rot_angle  
        break

    # determine second_angle passed to objectBallFeeder.py
    # second_angle = rot_angle # NOT NEEDED, rot_angle already passed in connection
    # if rot_angle is NULL:


    # ******POT PERCENTAGE******

    # if h > 250:
    #     wiper = 25
    #     distance = 4.4
    # elif h > 200 and h <= 250:
    #     wiper = 32
    #     distance = 4.9
    # elif h > 190 and h <= 200:
    #     wiper = 40
    #     distance = 5.8
    # elif h > 180 and h <= 190:
    #     wiper = 45
    #     distance = 6.4
    # elif h > 172 and h <= 180:
    #     wiper = 50
    #     distance = 6.8
    # elif h > 164 and h <= 172:
    #     wiper = 55
    #     distance = 7.3
    # elif h > 155 and h <= 164:
    #     wiper = 60
    #     distance = 8
    # elif h > 146 and h <= 155:
    #     wiper = 65
    #     distance = 10
    # elif h > 140 and h <= 146:
    #     wiper = 70
    #     distance = 12
    # elif h <= 140:
    #     wiper = 72
    #     distance = 13
    
    if h > 320:
        wiper = 39
        distance = 4.4
    elif h > 250 and h <= 320:
        wiper = 51
        distance = 4.9
    elif h > 180 and h <= 250:
        wiper = 65
        distance = 5.8
    elif h > 140 and h <= 180:
        wiper = 75
        distance = 6.4
    elif h <= 140:
        wiper = 89
        distance = 13
    # print("Height in image: ", h)
    # print("Wiper: ", wiper)

    if count == 200:
        count = 0
        if rot_angle >= 90:
            player_x = (20 + (math.sin(math.radians(rot_angle - 90)) * distance)) * (760/40)
            player_y = (math.cos(math.radians(rot_angle - 90)) * distance) * (532/16)
        else:
            player_x = (20 - (math.sin(math.radians(90 - rot_angle)) * distance)) * (760/40)
            player_y = (math.cos(math.radians(rot_angle - 90)) * distance) * (532/16)

        List = [player_x, player_y]
        with open("outputtestPlayer.csv", 'a', newline='') as csvfile:
            writer_object = writer(csvfile)
            writer_object.writerow(List)
            csvfile.close()

    # cv2.imshow("Human", frame)

    if rot_angle is not None and wiper is not None and launch_ball is not None and distance is not None:
        for conn, addr in connections:
            data_to_send = f"{distance},{rot_angle},{wiper},{launch_ball}"
            sock.sendall(data_to_send.encode())
            # print(f"Sent data to server at {addr}")

    # conn2.sendall(data_to_send.encode())
    # conn3.sendall(data_to_send.encode())

    cv2.imshow("Human", frame)
    #if keyboard.is_pressed("5"):
    if cv2.waitKey(1) & keyboard.is_pressed("0"):
        wiper = 0
        launch_ball = 2

        for conn, addr in connections:
            data_to_send = f"{distance},{rot_angle},{int(wiper)},{launch_ball}"
            sock.sendall(data_to_send.encode())
            # print(f"Sent data to server at {addr}")

        # conn2.sendall(data_to_send.encode())
        # conn3.sendall(data_to_send.encode())
        print("BALL LAUNCHER TURNING OFF")
        print("BALL DETECTOR TURNING OFF")
        print("BALL FEEDER TURNING OFF")
        break
cap.release()
cv2.destroyAllWindows()
sock.close()