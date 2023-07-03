import numpy as np
import cv2
import time
import math
from csv import writer
#from adafruit_servokit import ServoKit
import keyboard

position_laucnher_x_direction = 30
DECLARED_LEN = 1.5 #m
DECLARED_WID = 0.6 #m
focal_length_found = (800 * DECLARED_LEN) / DECLARED_WID
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

soccer_ball_distance = 1.5
soccer_ball_diameter = 0.22
radius = 0

servo_pin = 0
#kit = ServoKit(channels=16)
def distance_finder(focal_length, real_face_width, face_width_in_frame):  
    distance = (real_face_width * focal_length) / face_width_in_frame  
    return distance





def distance_to_camera(known_width, focal_length, pixel_width):
    return (known_width * focal_length) / pixel_width
def calculate_focal_length(image_width, focal_length_mm):
    return (image_width * focal_length_mm) / DECLARED_WID
cap = cv2.VideoCapture(0)

# Get the image width from the captured frame
_, frame = cap.read()
image_width = frame.shape[1]

# Calculate the focal length based on the image width and a known focal length in millimeters
focal_length_mm = 50  
focal_length = calculate_focal_length(image_width, focal_length_mm)


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
wiper = 0 
rot_angle = 90
#kit.servo[servo_pin].angle=rot_angle
print("ANGLE IS 90")


flag = 2

while(True):
    ret, frame = cap.read()
    height, width, _ = frame.shape
    center = int(width/2)
    boxes, weights = hog.detectMultiScale(frame,winStride=(8, 8), padding=(4, 4),scale=1.05)
    
    if keyboard.is_pressed("a"):
        flag = 1
        print("a is pressed")
    elif keyboard.is_pressed("s"):
        flag = 2
        print("s is pressed")
    elif keyboard.is_pressed("d"):
        flag = 3
        print("d is pressed")
    for (x, y, w, h) in boxes:
        if flag == 1:
            x_medium = int((x + x + w) / 2) - 80
            y_medium = int((y + y + h) / 2)
        elif flag == 2:
            x_medium = int((x + x + w) / 2) 
            y_medium = int((y + y + h) / 2)
        elif flag == 3:
            x_medium = int((x + x + w) / 2) + 80
            y_medium = int((y + y + h) / 2)  
        break
    cv2.line(frame, (x_medium, 0), (x_medium, 480), (255, 255, 0), 2)
    #cv2.line(frame, (0, y_medium), (640, y_medium), (255, 255, 0), 2)
    # focal_length_found = (180 * DECLARED_LEN) / DECLARED_WID
    # Distance = (DECLARED_WID * focal_length_found) / w

    distance = distance_to_camera(DECLARED_WID, focal_length, w)
    if distance >= 50 and distance <= 170:
        wiper = 5
    elif distance > 170 and distance <= 190:
        wiper = 11
    elif distance > 190 and distance <= 200:
        wiper = 18
    elif distance > 200 and distance <= 230:
        wiper = 26
    elif distance > 230 and distance <= 250:
        wiper = 31
    elif distance > 250 and distance <= 270:
        wiper = 36
    elif distance > 270 and distance <= 290:
        wiper = 40
    else:
        wiper = 40
    #DECLARED_LEN = Distance
    print("Distance: ", distance)
    print("Wiper: ", wiper)
    # DECLARED_WID * w * DECLARED_LEN / (w*DECLARED_WID)
    # if x_medium < center - 90:
    #     rot_angle = rot_angle + 2
    #     kit.servo[servo_pin].angle=rot_angle    
    # elif x_medium > center + 90:
    #     rot_angle = rot_angle - 2
    #     kit.servo[servo_pin].angle=rot_angle
    # else:
    #     rot_angle = rot_angle
    #     kit.servo[servo_pin].angle=rot_angle







    
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
