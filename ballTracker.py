# import cv2
# import numpy as np

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# prevCircle = None
# dist = lambda x1,y1,x2,y2: (x1-x2)**2+(y1-y2)**2

# while True:
#     ret, frame = cap.read()
#     if not ret: break

#     grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     blurrFrame = cv2.GaussianBlur(grayFrame, (17,17), 0)
#     circles = cv2.HoughCircles(blurrFrame, cv2.HOUGH_GRADIENT, 1.2, 100, param1=50, param2=30, minRadius=50, maxRadius=150)

#     if circles is not None:
#         circles = np.uint16(np.around(circles))
#         for pt in circles[0, :]:
#             a, b, r = pt[0], pt[1], pt[2]
#             cv2.circle(frame, (a, b), r, (0, 255, 0), 2)
#             cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)
#             print("RADIUS: ", r)
#             cv2.imshow("frame", frame)
#         # chosen = None
#         # for i in circles[0, :]:
            
#         #     if chosen is None: chosen = i
#         #     if prevCircle is not None:
#         #         if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1], prevCircle[0], prevCircle[1]):
#         #             chosen = i
#         # print("chosen[0]: ", int(chosen[0]))
#         # print("chosen[1]: ", int(chosen[1]))
#         # print("chosen[2]: ", int(chosen[2]))
#         # cv2.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
#         # cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (255, 0, 255), 3)
#         # print("RADIUS: ", r)
#         #prevCircle = chosen
#     #cv2.imshow("frame", frame)


#     if cv2.waitKey(1) == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()



# import cv2
# import numpy as np

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# lower = np.array([20, 100, 100])
# upper = np.array([30, 255, 255])

# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
    
#     # Convert frame to HSV color space
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
#     # Threshold the HSV image to get only the soccer ball colors
#     mask = cv2.inRange(hsv, lower, upper)
    
#     # Find contours in the thresholded image
#     contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     # Draw a bounding box around each detected contour
#     for contour in contours:
#         x, y, w, h = cv2.boundingRect(contour)
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
#     # Display the resulting frame
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
        
# # Release the capture
# cap.release()
# cv2.destroyAllWindows()

# import torch

# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
# import cv2

# cap = cv2.VideoCapture(0)

# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
    
#     # Detect objects in the frame using YOLOv5
#     results = model(frame)
    
#     # Filter the results to only include the soccer ball
#     soccer_ball_results = results.pred[results.pred[:, 5] == 0].xyxy[0]
    
#     # Draw a bounding box around the soccer ball
#     if len(soccer_ball_results) > 0:
#         x1, y1, x2, y2, conf, class_id = soccer_ball_results[0].tolist()
#         cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    
#     # Display the resulting frame
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
        
# # Release the capture
# cap.release()
# cv2.destroyAllWindows()
import cv2
import numpy as np

# Define the lower and upper bounds of the color of the soccer ball
lower_bound = np.array([30, 50, 50])   # HSV values
upper_bound = np.array([80, 255, 255]) # HSV values

# Create a VideoCapture object to capture frames from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the image based on the color of the soccer ball
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Apply some morphological operations to the mask to remove noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Find the contours of the soccer ball in the binary image
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw a bounding box around the soccer ball
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with the bounding box around the soccer ball
    cv2.imshow('Soccer Ball Detection', frame)

    # Wait for a key press and exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and destroy all windows
cap.release()
cv2.destroyAllWindows()