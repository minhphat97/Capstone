import cv2
import numpy as np
import math

# Known diameter of the soccer ball in meters.
soccer_ball_diameter = 0.22
radius = 0
# Known distance from the camera to the soccer ball in meters.
soccer_ball_distance = 1.5
x = 0
y = 0
# Start the webcam stream.
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam.
    ret, frame = cap.read()

    # Convert the frame to the HSV color space.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the color range for the soccer ball.
    lower_range = np.array([30, 50, 50])
    upper_range = np.array([80, 255, 255])

    # Create a binary mask for the soccer ball color range.
    mask = cv2.inRange(hsv, lower_range, upper_range)

    # Perform morphological operations to remove noise and fill gaps in the ball region.
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Detect the contours of the ball region.
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw a bounding box around the ball region if a contour is detected.
    if len(contours) > 0:
        contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
        largest_contour = max(contour_sizes, key=lambda x: x[0])[1]
        (x, y), radius = cv2.minEnclosingCircle(largest_contour)
        center = (int(x), int(y))
        radius = int(radius)
        #radius = math.sqrt(x)
        cv2.circle(frame, center, radius, (0, 255, 0), 2)

        # Calculate the distance and radius of the ball in meters.
        ball_size = radius * 2
        distance = (2*radius*soccer_ball_distance) / (soccer_ball_diameter)
        #radius_m = (soccer_ball_diameter * cap.get(3) * soccer_ball_distance) / (radius * 1000)
        cv2.putText(frame, f"Distance: {distance:.2f}cm", (int(x - radius), int(y - radius) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(frame, f"Radius: {radius :.2f}cm", (int(x - radius), int(y - radius) - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the resulting frame with the ball region highlighted.
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #if cv2.waitKey(1) & 0xFF == ord('k'):
    
    if radius >= 35.00 and radius <= 45.00:
        #if result:
        result, image = cap.read()
        cv2.imshow("Ball", image)
        # print ("X: ", x)
        # print ("Y: ", y)

# Release the webcam and close all windows.
cap.release()
cv2.destroyAllWindows()
