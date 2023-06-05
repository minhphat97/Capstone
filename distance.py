import cv2
import pathlib
import time
DECLARED_LEN = 70
DECLARED_WID = 14.3
focal_length_found = (140 * 60) / 14.3
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

fonts = cv2.FONT_HERSHEY_COMPLEX

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
face_detector = cv2.CascadeClassifier(str(cascade_path))

# def focal_length(determined_distance, actual_width, width_in_rf_image):  
#     focal_length_value = (width_in_rf_image * determined_distance) / actual_width  
#     return focal_length_value

def distance_finder(focal_length, real_face_width, face_width_in_frame):  
    distance = (real_face_width * focal_length) / face_width_in_frame  
    return distance

def face_data(image):
    face_width = 0
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)
    for (x, y, h, w) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), GREEN, 1)
        face_width = w
    return face_width

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    ret, frame = cap.read()
    face_width_in_frame = face_data(frame)
    if face_width_in_frame != 0:
        Distance = distance_finder(focal_length_found, DECLARED_WID, face_width_in_frame)
        cv2.putText(frame, f"Distance = {round(Distance,2)} CM", (50, 50), fonts, 1, (WHITE), 2)  

    cv2.imshow("frame", frame)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows() 