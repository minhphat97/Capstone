# import numpy as np
# import cv2
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# fgbg = cv2.createBackgroundSubtractorMOG2()
# cap.set(3, 640)
# cap.set(4, 480)

# object_detector = cv2.createBackgroundSubtractorMOG2(history=10, varThreshold=5)

# while(True):
#     ret, frame = cap.read()
#     height, width, _ = frame.shape
#     roi = frame[0:480, 0:640]
#     mask = object_detector.apply(roi)
#     # remove everything below 254 (get only white
#     # not sure this is needed
#     #_, mask = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)

#     contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     detections = []
#     biggest_index = 0
#     biggest_area = 0
#     ind = 0
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area > 200:
#             #cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
#             x,y,w,h = cv2.boundingRect(cnt)
#             detections.append([x,y,w,h])
#             area = w*h
#             if area > biggest_area:
#                 biggest_area = area
#                 biggest_index = ind
#             ind = ind + 1

#     if (len(detections) > 0):
#         x,y,w,h = detections[biggest_index]
#         cv2.rectangle(roi, (x,y), (x+w, y+h), (255, 255, 0), 3)
            

#     cv2.line(roi, (int(width/2), 0), (int(width/2), 480), (255, 255, 0), 2)
#     cv2.line(roi, (0, int(height/2)), (640, int(height/2)), (255, 255, 0), 2)
#     cv2.imshow("Human", frame)
#     cv2.imshow("ROI", roi)
#     cv2.imshow("Mask", mask)
#     if cv2.waitKey(1) == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()

import numpy as np
import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
fgbg = cv2.createBackgroundSubtractorMOG2()
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap.set(3, 640)
cap.set(4, 480)

x_medium = 0
y_medium = 0
angle = 90 #set angle Servo
object_detector = cv2.createBackgroundSubtractorMOG2(history=10, varThreshold=5)

while(True):
    ret, frame = cap.read()
    height, width, _ = frame.shape
    center = int(width/2)
    boxes, weights = hog.detectMultiScale(frame,winStride=(8, 8), padding=(4, 4),scale=1.05)
    for (x, y, w, h) in boxes:
        pad_w, pad_h = int(0.15 * w), int(0.01 * h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
        x_medium = int((x + x + w) / 2)
        y_medium = int((y + y + h) / 2)
        break
            
    cv2.line(frame, (x_medium, 0), (x_medium, 480), (255, 255, 0), 2)
    cv2.line(frame, (0, y_medium), (640, y_medium), (255, 255, 0), 2)
    cv2.line(frame, (int(width/2), 0), (int(width/2), 480), (255, 255, 0), 2)
    cv2.line(frame, (0, int(height/2)), (640, int(height/2)), (255, 255, 0), 2)
    cv2.imshow("Human", frame)
    if x_medium < center - 20:
        angle = angle + 1
    elif x_medium > center + 20:
        angle = angle - 1
    else:
        angle = angle
    print("Servo Angle is: ", angle)
    print("Human Center is: ", x_medium)
    print("Frame Center is: ", center)
    print()
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
