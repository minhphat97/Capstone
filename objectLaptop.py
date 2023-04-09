import numpy as np
import cv2
import socket
import pickle

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap.set(3, 640)
cap.set(4, 480)

object_detector = cv2.createBackgroundSubtractorMOG2(history=10, varThreshold=5)

# Socket setup
# Run `ifconfig` on Pi and look at inet under wlan0 to find IP address or look at connections in Mobile Hotspot if that is used
host = "192.168.210.151" #"raspberrypi.local"  # Change this to the hostname or IP address of your Raspberry Pi
port = 12345  # Choose a unique port number for the communication
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

x_medium = 0
y_medium = 0

while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape
    center = int(width / 2)
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8), padding=(4, 4), scale=1.05)
    
    for (x, y, w, h) in boxes:
        pad_w, pad_h = int(0.15 * w), int(0.01 * h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
        x_medium = int((x + x + w) / 2)
        y_medium = int((y + y + h) / 2)
        break

    # Send the x_medium value to Raspberry Pi
    data = {"x_medium": x_medium, "center": center}
    s.sendall(pickle.dumps(data))
    cv2.line(frame, (x_medium, 0), (x_medium, 480), (255, 255, 0), 2)
    cv2.line(frame, (0, y_medium), (640, y_medium), (255, 255, 0), 2)
    cv2.line(frame, (int(width/2), 0), (int(width/2), 480), (255, 255, 0), 2)
    cv2.line(frame, (0, int(height/2)), (640, int(height/2)), (255, 255, 0), 2)
    cv2.imshow("Human", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
s.close()
