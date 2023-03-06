import pathlib
import cv2
import time

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
print(cascade_path)
clf = cv2.CascadeClassifier(str(cascade_path))
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# camera.set(3, 1920) # [640, 480], [1280, 720], [1920, 1080] 
# camera.set(4, 1080)
temp, frame = camera.read()
rows, cols, temp2 = frame.shape
x_medium = int(cols/2)
center = int(cols/2)
position = 90

while True:
    temp, frame = camera.read()
    (h, w) = frame.shape[:2]
    print("height frame is: ", h)
    print("width frame is: ", w)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 255, 0), 2)
        x_medium = int((x + x + width) / 2)
        y_medium = int((y + y + height) / 2)
        break

    cv2.line(frame, (x_medium, 0), (x_medium, 480), (255, 255, 0), 2)
    cv2.line(frame, (0, y_medium), (640, y_medium), (255, 255, 0), 2)
    cv2.line(frame, (320, 0), (320, 480), (255, 255, 0), 2)
    cv2.line(frame, (0, 240), (640, 240), (255, 255, 0), 2)
    cv2.imshow("Faces", frame)
    if cv2.waitKey(1) == ord("q"):
        break
    #move sensor
    if x_medium < center - 20:
        position = position + 1
    elif x_medium > center + 20:
        position = position - 1
    elif x_medium == center:
        position  = position
    print("Position is: ", position)
    print("x_medium is: ", x_medium)
    print("center: ", center)
    
camera.release()
cv2.destroyAllWindows()