import cv2
import numpy as np
import math
from csv import writer
# import config
# import PID_control

position_launcher_x_direction = 5 #m REMEMBER TO DETERMINE THE DISTANCE OF BALLL LAUNCHER

radius = 0
x_ball = 0
y_ball = 0

lower_range_green = np.array([30, 50, 50]) #GREEN
upper_range_green = np.array([80, 255, 255])

lower_range_blue = np.array([98,50,50]) #BLUE
upper_range_blue = np.array([139,255,255])

lower_range_yellow = np.array([0,50,50]) #BLUE
upper_range_yellow = np.array([30,255,255])

kernel = np.ones((5, 5), np.uint8)
cap2 = cv2.VideoCapture(0)
cap2.set(3, 640)
cap2.set(4, 480)

while True:
    ret2, frame2 = cap2.read()
    hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)

    mask_green = cv2.inRange(hsv, lower_range_green, upper_range_green)
    mask_green = cv2.erode(mask_green, kernel, iterations=2)
    mask_green = cv2.dilate(mask_green, kernel, iterations=2)

    mask_blue = cv2.inRange(hsv, lower_range_blue, upper_range_blue)
    mask_blue = cv2.erode(mask_blue, kernel, iterations=2)
    mask_blue = cv2.dilate(mask_blue, kernel, iterations=2)

    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours_blue) > 0:
        contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours_blue]
        largest_contour = max(contour_sizes, key=lambda x: x[0])[1]
        (x_ball, y_ball), radius = cv2.minEnclosingCircle(largest_contour)
        center = (int(x_ball), int(y_ball))
        radius = int(radius)
        cv2.circle(frame2, center, radius, (0, 255, 0), 2)
    if len(contours_green) > 0:
        contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours_green]
        largest_contour = max(contour_sizes, key=lambda x: x[0])[1]
        (x_ball, y_ball), radius = cv2.minEnclosingCircle(largest_contour)
        center = (int(x_ball), int(y_ball))
        radius = int(radius)
        cv2.circle(frame2, center, radius, (0, 255, 0), 2)

    cv2.imshow("frame", frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    if radius >= 30.00 and radius <= 50.00:
        result, image = cap2.read()
        #print("result: ", result)
        if result == True:
        #     if config.second_angle >= 90:
        #         new_angle = abs(config.second_angle - 90)
        #         position_player_x_direction = (math.sin(math.radian(new_angle)) * config.distance) + position_launcher_x_direction
        #         position_player_y_direction = math.cos(math.radian(new_angle)) * (config.distance)
        #     else:
        #         new_angle = abs(90 - config.second_angle)
        #         position_player_x_direction = position_launcher_x_direction - (math.sin(math.radian(new_angle)) * config.distance) 
        #         position_player_y_direction = math.cos(math.radian(new_angle)) * (config.distance)
                
            cv2.imshow("Ball", image)
            # print ("X: ", x_ball)
            # print ("Y: ", y_ball)
            # print ("X_player: ", position_player_x_direction)
            # print ("Y_player: ", position_player_y_direction)
            # List = [x_ball, y_ball, position_player_x_direction, position_player_y_direction]
            # with open("outputtest.csv", 'a', newline='') as csvfile:
            #     writer_object = writer(csvfile)
            #     writer_object.writerow(List)
            #     csvfile.close()
            
cap2.release()
cv2.destroyAllWindows()
