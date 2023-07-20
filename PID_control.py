import numpy as np
import config
import cv2
import time
import math
from csv import writer
from adafruit_servokit import ServoKit
import keyboard
import board
import busio
import time
import adafruit_ds3502
import keyboard

distance = 2 #m
Px, Ix, Dx = -1/160, 0, 0
integral_x = 0
differential_x = 0
prev_x = 0
# ******DECLARE i2c FOR POT AND SETUP SERVO AND OpenCV******

servo_pin = 4
i2c=board.I2C()
ds3502 = adafruit_ds3502.DS3502(i2c) # this is i2c 1
i2c=busio.I2C(board.SCL_1,board.SDA_1) # this is i2c 0
kit = ServoKit(channels=16,i2c=i2c)

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
w = 1
h = 0
ds3502.wiper = 10 
rot_angle = 90
kit.servo[servo_pin].angle=rot_angle
print("ANGLE IS 90")
#print("SLEEPING FOR 2 S")
time.sleep(2)
ds3502.wiper = 20
time.sleep(2)
flag = 2

while(True):
    ret, frame = cap.read()
    height, width, _ = frame.shape
    center = int(width/2)
    boxes, weights = hog.detectMultiScale(frame,winStride=(8, 8), padding=(4, 4),scale=1.05)
    
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
        if abs(error_x) > 15:
            rot_angle = rot_angle - error_x/43
        
        if rot_angle < 43:
            rot_angle = 43
            print("Servo out of range")
        
        if rot_angle > 137:
            rot_angle = 137
            print("Servo out of range")

        kit.servo[servo_pin].angle = rot_angle  
        break

    # determine second_angle passed to objectBallFeeder.py
    config.second_angle = rot_angle 

    # ******POT PERCENTAGE******

    if h > 350:
        ds3502.wiper = 24
        config.distance = 2.7
    elif h > 330 and h <= 350:
        ds3502.wiper = 28
        config.distance = 3.1
    elif h > 300 and h <= 330:
        ds3502.wiper = 33
        config.distance = 3.6
    elif h > 280 and h <= 300:
        ds3502.wiper = 38
        config.distance = 4.0
    elif h > 250 and h <= 280:
        ds3502.wiper = 44
        config.distance = 4.4
    elif h > 220 and h <= 250:
        ds3502.wiper = 50
        config.distance = 4.9
    elif h > 200 and h <= 220:
        ds3502.wiper = 56
        config.distance = 5.3
    elif h > 190 and h <= 200:
        ds3502.wiper = 61
        config.distance = 5.8
    elif h > 180 and h <= 190:
        ds3502.wiper = 65
        config.distance = 6.4
    elif h > 172 and h <= 180:
        ds3502.wiper = 70
        config.distance = 6.8
    elif h > 164 and h <= 172:
        ds3502.wiper = 75
        config.distance = 7.3
    elif h > 158 and h <= 164:
        ds3502.wiper = 78
        config.distance = 8
    elif h > 152 and h <= 158:
        ds3502.wiper = 83 
        config.distance = 10
    elif h > 145 and h <= 155:
        ds3502.wiper = 87
        config.distance = 12
    elif h <= 145:
        ds3502.wiper = 90
        config.distance = 13

    print("Height in image: ", h)
    print("Wiper: ", ds3502.wiper)

    cv2.imshow("Human", frame)
    #if keyboard.is_pressed("5"):
    if cv2.waitKey(1) & keyboard.is_pressed("0"):
        

        ds3502.wiper = 0
        print("BALL LAUNCHER TURNING OFF")
        break
cap.release()
cv2.destroyAllWindows()