import numpy as np
import cv2
import time
import math
from csv import writer
# from adafruit_servokit import ServoKit
import keyboard
# import Jetson.GPIO as GPIO
import time

# GPIO.setmode(GPIO.BOARD)
# inPin = 15
# GPIO.setup(inPin, GPIO.IN)
# inPin2 = 16
# GPIO.setup(inPin2, GPIO.IN)

position_laucnher_x_direction = 30
DECLARED_LEN = 60
DECLARED_WID = 14.3
focal_length_found = (140 * DECLARED_LEN) / DECLARED_WID
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

soccer_ball_distance = 1.5
soccer_ball_diameter = 0.22
radius = 0

servo_pin = 0
# kit = ServoKit(channels=16)
def distance_finder(focal_length, real_face_width, face_width_in_frame):  
    distance = (real_face_width * focal_length) / face_width_in_frame  
    return distance

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
flag = 2
previous_x_medium = None  # Store previous frame's x_medium to calculate velocity

rot_angle = 90
# kit.servo[servo_pin].angle=rot_angle
print("ANGLE IS 90")
print("SLEEPING FOR 1 S")
time.sleep(1)
#GPIO.setmode(GPIO.BOARD)
# inPin = 15
# GPIO.setup(inPin, GPIO.IN)
# inPin2 = 16
# GPIO.setup(inPin2, GPIO.IN)
flag = 2

while(True):
    ret, frame = cap.read()
    # ret2, frame2 = cap2.read()
    height, width, _ = frame.shape
    center = int(width/2)
    boxes, weights = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.8)
    # boxes, weights = hog.detectMultiScale(frame, scale=1.1, minNeighbors=5, minSize=(30, 30)) 

    for (x, y, w, h) in boxes:
        x_medium = int((x + x + w) / 2)
        y_medium = int((y + y + h) / 2)

        # Calculate velocity and update flag
        if previous_x_medium is not None:
            velocity = x_medium - previous_x_medium
            if velocity < 30:
                flag = 3  # Positive velocity (if wrong, swap with flag 1)
            elif velocity > -30:
                flag = 1  # Negative velocity
            else:
                flag = 2  # No velocity

        previous_x_medium = x_medium  # Update previous_x_medium for next iteration

        if flag == 1:
            x_medium = x_medium - 150
            print("left (line on video)")
        elif flag == 3:
            x_medium = x_medium + 150
            print("right (line on video)")

        break

    cv2.line(frame, (x_medium, 0), (x_medium, 480), (255, 255, 0), 2)
    # cv2.line(frame, (0, y_medium), (640, y_medium), (255, 255, 0), 2)
    # if x_medium < center - 50:
    #     rot_angle = rot_angle + 2
    #     if rot_angle >= 180:
    #         rot_angle = 180
    #     kit.servo[servo_pin].angle=rot_angle    
    # elif x_medium > center + 50:
    #     rot_angle = rot_angle - 2
    #     if rot_angle <=0:
    #         rot_angle = 0
    #     kit.servo[servo_pin].angle=rot_angle
    # else:
    #     rot_angle = rot_angle
    #     kit.servo[servo_pin].angle=rot_angle







    # Distance = distance_finder(focal_length_found, DECLARED_WID, w)
 
    # mask = cv2.inRange(hsv, lower_range, upper_range)
    # mask = cv2.erode(mask, kernel, iterations=2)
    # mask = cv2.dilate(mask, kernel, iterations=2)
    # contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # if len(contours) > 0:
    #     contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    #     largest_contour = max(contour_sizes, key=lambda x: x[0])[1]
    #     (x_ball, y_ball), radius = cv2.minEnclosingCircle(largest_contour)
    #     radius = int(radius)
    
    
    # if radius >= 30.00 and radius <= 50.00:
    #     result, image = cap.read()
    #     if result == True:
    #         Distance = distance_finder(focal_length_found, DECLARED_WID, w)
    #         if rot_angle >= 90:
    #             new_angle = abs(rot_angle - 90)
    #             position_player_x_direction = (math.sin(math.radian(new_angle)) * Distance) + position_laucnher_x_direction
    #             position_player_y_direction = math.cos(math.radian(new_angle)) * Distance
    #         else:
    #             new_angle = abs(90 - rot_angle)
    #             position_player_x_direction = position_laucnher_x_direction - (math.sin(math.radian(new_angle)) * Distance) 
    #             position_player_y_direction = math.cos(math.radian(new_angle)) * Distance

    #         cv2.imshow("Ball", image)
    #         print ("X: ", x_ball)
    #         print ("Y: ", y_ball)
    #         List = [x_ball, y_ball, position_player_x_direction, position_player_y_direction]
    #         with open("outputtest.csv", 'a', newline='') as csvfile:
    #             writer_object = writer(csvfile)
    #             writer_object.writerow(List)
    #             csvfile.close()


    cv2.imshow("Human", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
