import numpy as np
import cv2
import time
import math
from csv import writer
from adafruit_servokit import ServoKit
import keyboard
import board
import busio
import time
import Jetson.GPIO as GPIO
import adafruit_ds3502

Px, Ix, Dx = -1/160, 0, 0
integral_x = 0
differential_x = 0
prev_x = 0
# ******DECLARE i2c FOR POT AND SETUP SERVO AND OpenCV******

servo_pin = 0
i2c=board.I2C()
ds3502 = adafruit_ds3502.DS3502(i2c)
i2c=busio.I2C(board.SCL_1,board.SDA_1)
kit = ServoKit(channels=16,i2c=i2c)

position_laucnher_x_direction = 30
Known_distance = 300 #cm
Known_width = 90 #cm

cap = cv2.VideoCapture(0)

def Focal_length_finder(measured_distance, real_width, width_in_rf_image):
    focal_length = (width_in_rf_image*measured_distance)/real_width
    return focal_length

def Distance_finder(Focal_length, real_face_width, face_width_in_frame):
    distance = (real_face_width * Focal_length)/face_width_in_frame
    return distance

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
print("SLEEPING FOR 1 S")
time.sleep(1)
ds3502.wiper = 20
# GPIO.setmode(GPIO.BOARD)
# InPin = 15
# GPIO.setup(InPin, GPIO.IN)
# InPin2 = 16
# GPIO.setup(InPin2, GPIO.IN)

flag = 2

while(True):
    ret, frame = cap.read()
    # x = GPIO.input(InPin)
    # y = GPIO.input(InPin2)
    height, width, _ = frame.shape
    center = int(width/2)
    boxes, weights = hog.detectMultiScale(frame,winStride=(8, 8), padding=(4, 4),scale=1.05)
    
    # if x == 1 and y == 0:
    if keyboard.is_pressed("a"):
        flag = 1
        print("a is pressed")
    # elif x == 1 and y == 1:
    elif keyboard.is_pressed("s"):
        flag = 2
        print("s is pressed")
    # elif x == 0 and y == 1:
    elif keyboard.is_pressed("d"):
        flag = 3
        print("d is pressed")
    
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
        
        if rot_angle < 30:
            rot_angle = 30
            print("Servo out of range")
        
        if rot_angle > 170:
            rot_angle = 170
            print("Servo out of range")

        kit.servo[servo_pin].angle = rot_angle  
        break
  




   







    # cv2.line(frame, (x_medium, 0), (x_medium, 480), (255, 255, 0), 2)

    # if x_medium < center - 80:
    #     rot_angle = rot_angle + 4
    #     if rot_angle >= 180:
    #         rot_angle = 180
    #     kit.servo[servo_pin].angle = rot_angle
    # elif x_medium > center + 80:
    #     rot_angle = rot_angle - 4
    #     if rot_angle <= 30:
    #         roeight_angle = 30
    #     kit.servo[servo_pin].angle = rot_angle 
    # else:
    #     rot_angle = rot_angle
    #     kit.servo[servo_pin].angle = rot_angle      

    # ******POT PERCENTAGE******

    if h >= 400:
        ds3502.wiper = 20
    elif h > 350 and h < 400:
        ds3502.wiper = 24
    elif h > 330 and h <= 350:
        ds3502.wiper = 28
    elif h > 300 and h <= 330:
        ds3502.wiper = 33
    elif h > 280 and h <= 300:
        ds3502.wiper = 38
    elif h > 250 and h <= 280:
        ds3502.wiper = 44
    elif h > 220 and h <= 250:
        ds3502.wiper = 50
    elif h > 200 and h <= 220:
        ds3502.wiper = 56
    elif h > 190 and h <= 200:
        ds3502.wiper = 61
    elif h <= 190:
        ds3502.wiper = 65
    print("Height in image: ", h)
    print("Wiper: ", ds3502.wiper)

    cv2.imshow("Human", frame)
    if cv2.waitKey(1) == ord("q"):
        ds3502.wiper = 0
        break
cap.release()
cv2.destroyAllWindows()