import numpy as np
import cv2
import time
import math
from csv import writer
from cvzone.HandTrackingModule import HandDetector
from adafruit_servokit import ServoKit

position_laucnher_x_direction = 30
DECLARED_LEN = 60
DECLARED_WID = 14.3
focal_length_found = (140 * DECLARED_LEN) / DECLARED_WID
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
fonts = cv2.FONT_HERSHEY_COMPLEX
soccer_ball_distance = 1.5
soccer_ball_diameter = 0.22
radius = 0

servo_pin = 0
kit = ServoKit(channels=16)
def distance_finder(focal_length, real_face_width, face_width_in_frame):  
    distance = (real_face_width * focal_length) / face_width_in_frame  
    return distance

cap = cv2.VideoCapture(0)
# cap2 = cv2.VideoCapture(1)
detector = HandDetector(maxHands=1, detectionCon=0.8)
fgbg = cv2.createBackgroundSubtractorMOG2()
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
x_ball = 0
y_ball = 0
rot_angle = 90
kit.servo[servo_pin].angle=rot_angle
print("ANGLE IS 90")
print("SLEEPING FOR 5 S")
time.sleep(5)

lower_range = np.array([30, 50, 50])
upper_range = np.array([80, 255, 255])
object_detector = cv2.createBackgroundSubtractorMOG2(history=10, varThreshold=5)
flag = 3
kernel = np.ones((5, 5), np.uint8)
while(True):
    ret, frame = cap.read()
    #ret2, frame2 = cap2.read()
    height, width, _ = frame.shape
    center = int(width/2)
    boxes, weights = hog.detectMultiScale(frame,winStride=(8, 8), padding=(4, 4),scale=1.05)
    frame = cv2.flip(frame, 1)
    hand = detector.findHands(frame, draw=False)
    # hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
        x_medium = int((x + x + w) / 2)
        y_medium = int((y + y + h) / 2)
        break

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
    if hand:
        imlist = hand[0]
        if imlist:
            fingerup = detector.fingersUp(imlist)
            if fingerup == [1, 1, 0, 0, 1]:
                flag = 1
                print("detect 1")
            elif fingerup == [0, 1, 1, 0, 0]:
                flag = 2
                print("detect 2")
            elif fingerup == [0, 1, 1, 1, 0]:
                flag = 3
                print("detect 3")

    if flag == 1:
        x_medium = x_medium + 20
    elif flag == 2:
        x_medium = x_medium - 20
    elif flag == 3:
        x_medium = x_medium

    if x_medium < center - 90:
        if rot_angle >=180:
            rot_angle = 178
        elif rot_angle <= 0:
            rot_angle = 2
        rot_angle = rot_angle + 2
        kit.servo[servo_pin].angle=rot_angle    
    elif x_medium > center + 90:
        if rot_angle >=180:
            rot_angle = 178
        elif rot_angle <= 0:
            rot_angle = 2
        rot_angle = rot_angle - 2
        kit.servo[servo_pin].angle=rot_angle
    else:
        rot_angle = rot_angle
        kit.servo[servo_pin].angle=rot_angle


    
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
    # cv2.imshow("Ball", frame2)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
