import numpy as np
import cv2
import time
from adafruit_servokit import ServoKit

# Constants
SERVO_PIN = 0
SERVO_ANGLE = 90
SLEEP_TIME = 5

# Initialization
kit = ServoKit(channels=16)
kit.servo[SERVO_PIN].angle = SERVO_ANGLE
print("ANGLE IS 90")
print(f"SLEEPING FOR {SLEEP_TIME} S")
time.sleep(SLEEP_TIME)

# Video capture settings
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
x_medium_prev = 0
x_medium = 0

while True:
    ret, frame = cap.read()
    frame_height, frame_width, _ = frame.shape
    frame_center = int(frame_width/2)

    # Human detection and tracking
    boxes, _ = hog.detectMultiScale(frame, winStride=(8, 8), padding=(4, 4), scale=1.05)
    frame = cv2.flip(frame, 1)

    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
        x_medium = int((x + x + w) / 2)
        break

    # Predict next position
    velocity_x = x_medium - x_medium_prev
    x_medium_next = x_medium + velocity_x  # Predicts position in the next frame
    x_medium_prev = x_medium

    # Servo rotation prediction
    if x_medium_next < frame_center - 90:
        SERVO_ANGLE = min(178, SERVO_ANGLE + 2) if SERVO_ANGLE >= 180 else max(2, SERVO_ANGLE + 2)
        kit.servo[SERVO_PIN].angle = SERVO_ANGLE
    elif x_medium_next > frame_center + 90:
        SERVO_ANGLE = min(178, SERVO_ANGLE - 2) if SERVO_ANGLE >= 180 else max(2, SERVO_ANGLE - 2)
        kit.servo[SERVO_PIN].angle = SERVO_ANGLE
    else:
        kit.servo[SERVO_PIN].angle = SERVO_ANGLE

    cv2.imshow("Human", frame)

    # Exit condition
    if cv2.waitKey(1) == ord("q"):
        break

# Releasing the resources
cap.release()
cv2.destroyAllWindows()
