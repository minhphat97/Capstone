import cv2
import numpy as np
import math
from csv import writer
import keyboard
import time
import socket
# import PID_control

# ***************************************************************
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Laptop IP address (localhost)
# laptop_ip = '127.0.0.1'
# laptop_port = 12345

# # Connect to the laptop's IP address and port for the PID_control.py data (distance, second_angle)
# sock.connect((laptop_ip, laptop_port))
# print("Connected to laptop at", (laptop_ip, laptop_port))
# ****************************************************************

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Accept connections from any port
ip = "127.0.0.1"
port = 12345

# Connect to the laptop's IP address and port
# sock.bind((ip, port))
print("Connected to laptop at", (ip, port))
sock.bind((ip, port))
sock.listen(1)  # Listen for incoming connections, with a backlog of 1 connection
conn, addr = sock.accept()  # Accept an incoming connection)

position_launcher_x_direction = 5 #m REMEMBER TO DETERMINE THE DISTANCE OF BALLL LAUNCHER

radius = 0
x_ball = 0
y_ball = 0

lower_range_green = np.array([30, 50, 50]) #GREEN
upper_range_green = np.array([80, 255, 255])

lower_range_blue = np.array([98,50,50]) #BLUE
upper_range_blue = np.array([139,255,255])

lower_range_white = np.array([0,0,255]) #WHITE
upper_range_white = np.array([179,62,255])

lower_range_yellow = np.array([0,50,50]) #BLUE
upper_range_yellow = np.array([30,255,255])

kernel = np.ones((5, 5), np.uint8)
cap2 = cv2.VideoCapture(1) # set to 1
cap2.set(3, 640)
cap2.set(4, 480)
time.sleep(1)

distance = 0
rot_angle = 0
wiper = 0

print("STARTING BALL DETECTOR COMPONENTS")
while True:
    ret2, frame2 = cap2.read()
    hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)

    # mask_green = cv2.inRange(hsv, lower_range_green, upper_range_green)
    # mask_green = cv2.erode(mask_green, kernel, iterations=2)
    # mask_green = cv2.dilate(mask_green, kernel, iterations=2)

    mask_blue = cv2.inRange(hsv, lower_range_blue, upper_range_blue)
    mask_blue = cv2.erode(mask_blue, kernel, iterations=2)
    mask_blue = cv2.dilate(mask_blue, kernel, iterations=2)

    mask_white = cv2.inRange(hsv, lower_range_white, upper_range_white)
    mask_white = cv2.erode(mask_white, kernel, iterations=2)
    mask_white = cv2.dilate(mask_white, kernel, iterations=2)

    contours_white, _ =cv2.findContours(mask_white,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours_blue) > 0:
        contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours_blue]
        largest_contour = max(contour_sizes, key=lambda x: x[0])[1]
        (x_ball, y_ball), radius = cv2.minEnclosingCircle(largest_contour)
        center = (int(x_ball), int(y_ball))
        radius = int(radius)
        cv2.circle(frame2, center, radius, (0, 255, 0), 2)
    if len(contours_white) > 0:
        contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours_white]
        largest_contour = max(contour_sizes, key=lambda x: x[0])[1]
        (x_ball, y_ball), radius = cv2.minEnclosingCircle(largest_contour)
        center = (int(x_ball), int(y_ball))
        radius = int(radius)
        cv2.circle(frame2, center, radius, (0, 255, 0), 2)
    # if len(contours_green) > 0:
    #     contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours_green]
    #     largest_contour = max(contour_sizes, key=lambda x: x[0])[1]
    #     (x_ball, y_ball), radius = cv2.minEnclosingCircle(largest_contour)
    #     center = (int(x_ball), int(y_ball))
    #     radius = int(radius)
    #     cv2.circle(frame2, center, radius, (0, 255, 0), 2)

    cv2.imshow("frame", frame2)
    data_received = conn.recv(4096)
    data_received = data_received.decode()
    if not data_received:
        print("ERROR: BALL DETECTOR TURNING OFF")
        break
    
    #if cv2.waitKey(1) & 0xFF == ord('0'):
    if cv2.waitKey(1) & keyboard.is_pressed("0"):
        print("BALL DETECTOR TURNING OFF")
        break

    try:
        distance, rot_angle, wiper, launch_ball= map(float, data_received.split(','))
        if radius >= 30.00 and radius <= 50.00:
            result, image = cap2.read()
            #print("result: ", result)
            if result == True:
                if rot_angle < 90:
                    new_angle = abs(rot_angle - 90)
                    position_player_x_direction = ((math.sin(math.radian(new_angle)) * distance) + position_launcher_x_direction) * 100
                    position_player_y_direction = (math.cos(math.radian(new_angle)) * (distance)) * 100/2
                else:
                    new_angle = abs(90 - rot_angle)
                    position_player_x_direction = (position_launcher_x_direction - (math.sin(math.radian(new_angle)) * distance)) * 100 
                    position_player_y_direction = (math.cos(math.radian(new_angle)) * (distance)) * 100/2
                    
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
    except ValueError as e:
        print("Error while parsing data:", e)
                
cap2.release()
cv2.destroyAllWindows()
conn.close()
sock.close()
