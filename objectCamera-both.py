import numpy as np
import cv2
import time

cap1 = cv2.VideoCapture(0) # First webcam
cap2 = cv2.VideoCapture(2) # Second webcam

fgbg = cv2.createBackgroundSubtractorMOG2()
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap1.set(3, 640)
cap1.set(4, 480)
cap2.set(3, 640)
cap2.set(4, 480)

x_medium1 = 0
y_medium1 = 0
x_medium2 = 0
y_medium2 = 0
angle = 90 #set angle Servo
object_detector = cv2.createBackgroundSubtractorMOG2(history=10, varThreshold=5)

while(True):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # time.sleep(5)

    # Process frame from first webcam
    height1, width1, _ = frame1.shape
    center1 = int(width1/2)
    boxes1, weights1 = hog.detectMultiScale(frame1,winStride=(8, 8), padding=(4, 4),scale=1.05)
    for (x1, y1, w1, h1) in boxes1:
        pad_w1, pad_h1 = int(0.15 * w1), int(0.01 * h1)
        cv2.rectangle(frame1, (x1, y1), (x1 + w1, y1 + h1), (255, 255, 0), 2)
        x_medium1 = int((x1 + x1 + w1) / 2)
        y_medium1 = int((y1 + y1 + h1) / 2)
        break
            
    cv2.line(frame1, (x_medium1, 0), (x_medium1, 480), (255, 255, 0), 2)
    cv2.line(frame1, (0, y_medium1), (640, y_medium1), (255, 255, 0), 2)
    cv2.line(frame1, (int(width1/2), 0), (int(width1/2), 480), (255, 255, 0), 2)
    cv2.line(frame1, (0, int(height1/2)), (640, int(height1/2)), (255, 255, 0), 2)
    cv2.imshow("Human 1", frame1)
    
    if x_medium1 < center1 - 20:
        angle = angle + 1
    elif x_medium1 > center1 + 20:
        angle = angle - 1
    else:
        angle = angle
    print("Servo Angle for Human 1 is: ", angle)
    print("Human 1 Center is: ", x_medium1)
    print("Frame 1 Center is: ", center1)
    print()

    # time.sleep(0.5)
    # Process frame from second webcam
    height2, width2, _ = frame2.shape
    center2 = int(width2/2)
    boxes2, weights2 = hog.detectMultiScale(frame2,winStride=(8, 8), padding=(4, 4),scale=1.05)
    for (x2, y2, w2, h2) in boxes2:
        pad_w2, pad_h2 = int(0.15 * w2), int(0.01 * h2)
        cv2.rectangle(frame2, (x2, y2), (x2 + w2, y2 + h2), (255, 255, 0), 2)
        x_medium2 = int((x2 + x2 + w2) / 2)
        y_medium2 = int((y2 + y2 + h2) / 2)
        break

    cv2.line(frame2, (x_medium2, 0), (x_medium2, 480), (255, 255, 0), 2)
    cv2.line(frame2, (0, y_medium2), (640, y_medium2), (255, 255, 0), 2)
    cv2.line(frame2, (int(width2/2), 0), (int(width2/2), 480), (255, 255, 0), 2)
    cv2.line(frame2, (0, int(height2/2)), (640, int(height2/2)), (255, 255, 0), 2)
    cv2.imshow("Human 2", frame2)
    
    if x_medium2 < center2 - 20:
        angle = angle + 1
    elif x_medium2 > center2 + 20:
        angle = angle - 1
    else:
        angle = angle
    print("Servo Angle for Human 2 is: ", angle)
    print("Human 2 Center is: ", x_medium2)
    print("Frame 2 Center is: ", center2)
    print()
    if cv2.waitKey(1) == ord("q"):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()