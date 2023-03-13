import cv2

# Initialize the first camera (change 0 to 1 if using a second camera)
cap1 = cv2.VideoCapture(0)

# Initialize the second camera (change 1 to 2 if using a third camera)
cap2 = cv2.VideoCapture(1)

# Check if the cameras have been successfully opened
if not cap1.isOpened() or not cap2.isOpened():
    print("Cannot open webcams")
    exit()

# Capture and display frames from both cameras
while True:
    # Read a frame from the first camera
    ret1, frame1 = cap1.read()
    if not ret1:
        print("Cannot read a frame from the first camera")
        break

    # Read a frame from the second camera
    ret2, frame2 = cap2.read()
    if not ret2:
        print("Cannot read a frame from the second camera")
        break

    # Display the frames from both cameras
    cv2.imshow("Camera 1", frame1)
    cv2.imshow("Camera 2", frame2)

    # Wait for a key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the cameras and close the windows
cap1.release()
cap2.release()
cv2.destroyAllWindows()