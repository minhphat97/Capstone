import numpy as np
import cv2
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
servo_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)
pwm = GPIO.PWM(servo_pin,50) 
print("Starting at zero...")
pwm.start(5) 

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
fgbg = cv2.createBackgroundSubtractorMOG2()
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap.set(3, 640)
cap.set(4, 480)
x_medium = 0
y_medium = 0
angle = 90 #set angle Servo
duty = angle / 27 + 2
pwm.ChangeDutyCycle(duty) 


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
    if x_medium < center - 30:
        angle = angle + 1
        duty = angle / 27 + 2
        pwm.ChangeDutyCycle(duty)
    elif x_medium > center + 30:
        angle = angle - 1
        duty = angle / 27 + 2
        pwm.ChangeDutyCycle(duty)
    else:
        angle = angle
        duty = angle / 27 + 2
        pwm.ChangeDutyCycle(duty)
    print("Servo Angle is: ", angle)
    print("Human Center is: ", x_medium)
    print("Frame Center is: ", center)
    print()
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
