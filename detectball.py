# import cv2
# import pathlib
# import urllib.request

# # Download the cascade classifier XML file
# cascade_file_url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_soccerball.xml'
# cascade_file_path = 'haarcascade_soccerball.xml'
# urllib.request.urlretrieve(cascade_file_url, cascade_file_path)
# soccer_cascade = cv2.CascadeClassifier(cascade_file_path)

# # Function to detect soccer balls in the frame
# def detect_soccer_balls(frame):
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     soccer_balls = soccer_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     for (x, y, w, h) in soccer_balls:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#     return frame

# # Start the webcam feed
# video_capture = cv2.VideoCapture(0)  # 0 for default webcam, or provide the specific index if multiple webcams are available

# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()

#     # Detect soccer balls in the frame
#     frame = detect_soccer_balls(frame)

#     # Display the resulting frame
#     cv2.imshow('Soccer Ball Detection', frame)

#     # Exit the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture and close the window
# video_capture.release()
# cv2.destroyAllWindows()

import cv2 as cv
import numpy as np

videoCapture = cv.VideoCapture(0)
prevCircle = None
dist = lambda x1, y1, x2, y2: (x1 - x2)**2 + (y1 - y2)**2

while True:
    ret, frame = videoCapture.read()
    if not ret: break
    
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurFrame = cv.GaussianBlur(grayFrame, (17,17), 0)

    circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, 1.2, 100, param1=100, param2=30, minRadius=75, maxRadius=400)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None: chosen = i
            if prevCircle is not None:
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1], prevCircle[0], prevCircle[1]):
                    chosen = i
        cv.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
        cv.circle(frame, (chosen[0], chosen[1]), chosen[2], (255, 0, 255), 3)
        prevCircle = chosen
    cv.imshow("Cirlcles", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):break

videoCapture.release()
cv.destroyAllWindows()

