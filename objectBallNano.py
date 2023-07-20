import cv2
import numpy as np
import math
from csv import writer
import config
import PID_control

position_launcher_x_direction = 5 #m REMEMBER TO DETERMINE THE DISTANCE OF BALLL LAUNCHER

radius = 0
x_ball = 0
y_ball = 0

lower_range_green = np.array([30, 50, 50]) #GREEN
upper_range_green = np.array([80, 255, 255])

lower_range_white = np.array([0,0,255]) #WHITE
upper_range_white = np.array([179,62,255])

kernel = np.ones((5, 5), np.uint8)
cap2 = cv2.VideoCapture(0)
cap2.set(3, 640)
cap2.set(4, 480)
# cap2.set(3, 760)
# cap2.set(4, 532)
while True:
    ret2, frame2 = cap2.read()
    hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)

    mask_green = cv2.inRange(hsv, lower_range_green, upper_range_green)
    mask_green = cv2.erode(mask_green, kernel, iterations=2)
    mask_green = cv2.dilate(mask_green, kernel, iterations=2)

    mask_white = cv2.inRange(hsv, lower_range_white, upper_range_white)
    mask_white = cv2.erode(mask_white, kernel, iterations=2)
    mask_white = cv2.dilate(mask_white, kernel, iterations=2)

    contours_white, _ = cv2.findContours(mask_white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours_white) > 0:
        contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours_white]
        largest_contour = max(contour_sizes, key=lambda x: x[0])[1]
        (x_ball, y_ball), radius = cv2.minEnclosingCircle(largest_contour)
        center = (int(x_ball), int(y_ball))
        radius = int(radius)
        cv2.circle(frame2, center, radius, (0, 255, 0), 2)
    elif len(contours_green) > 0:
        contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours_green]
        largest_contour = max(contour_sizes, key=lambda x: x[0])[1]
        (x_ball, y_ball), radius = cv2.minEnclosingCircle(largest_contour)
        center = (int(x_ball), int(y_ball))
        radius = int(radius)
        cv2.circle(frame2, center, radius, (0, 255, 0), 2)

    cv2.imshow("frame", frame2)
    if cv2.waitKey(1) & 0xFF == ord('0'):
        break
    
    if radius >= 30.00 and radius <= 50.00:
        result, image = cap2.read()
        #print("result: ", result)
        if result == True:
            if config.second_angle < 90:
                new_angle = abs(config.second_angle - 90)
                position_player_x_direction = ((math.sin(math.radian(new_angle)) * config.distance) + position_launcher_x_direction) * 100
                position_player_y_direction = (math.cos(math.radian(new_angle)) * (config.distance)) * 100
        
            else:
                new_angle = abs(90 - config.second_angle)
                position_player_x_direction = (position_launcher_x_direction - (math.sin(math.radian(new_angle)) * config.distance)) * 100 
                position_player_y_direction = (math.cos(math.radian(new_angle)) * (config.distance))*100
            
            cv2.imshow("Ball", image)
            # print ("X: ", x_ball)
            # print ("Y: ", y_ball)
            # print ("X_player: ", position_player_x_direction)
            # print ("Y_player: ", position_player_y_direction)
            x_ball_new = (760/640) * x_ball
            y_ball_new = (532/480) * y_ball 
            List = [x_ball_new, y_ball_new, position_player_x_direction, position_player_y_direction]
            with open("outputtest.csv", 'a', newline='') as csvfile:
                writer_object = writer(csvfile)
                writer_object.writerow(List)
                csvfile.close()
            
cap2.release()
cv2.destroyAllWindows()
