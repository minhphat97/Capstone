import cv2

# Initialize the first camera (change 0 to 1 if using a second camera)
cap1 = cv2.VideoCapture(0)

# Initialize the second camera (change 1 to 2 if using a third camera)
cap2 = cv2.VideoCapture(2)

# Load the Haar Cascade classifier for human detection
human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Check if the cameras have been successfully opened
if not cap1.isOpened() or not cap2.isOpened():
    print("Cannot open webcams")
    exit()

# Define a function to perform human detection and tracking
def detect_and_track(frame, scale_factor=1.1, min_neighbors=5):
    # Convert the frame to grayscale for human detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform human detection using the Haar Cascade classifier
    humans = human_cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors)

    # Draw bounding boxes around the detected humans and return their coordinates
    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return humans

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

    # Perform human detection and tracking on both frames
    humans1 = detect_and_track(frame1)
    humans2 = detect_and_track(frame2)

    # Display the frames with human detection and tracking
    cv2.imshow("Camera 1", frame1)
    cv2.imshow("Camera 2", frame2)

    # Wait for a key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the cameras and close the windows
cap1.release()
cap2.release()
cv2.destroyAllWindows()