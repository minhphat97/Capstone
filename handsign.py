import cv2
#import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    value = 10
    if hand:
        imlist = hand[0]
        if imlist:
            fingerup = detector.fingersUp(imlist)
            if fingerup == [1, 1, 0, 0, 1]:
                new_value = value + 5
                print("It s 1")
                print("New value: ", new_value)
            elif fingerup == [0, 1, 1, 0, 0]:
                new_value = value - 5
                print("It s 2")
                print("New value: ", new_value)
            elif fingerup == [0, 1, 1, 1, 0]:
                new_value = value
                print("It s 3")
                print("New value: ", new_value)
    
    # fing = cv2.resize(fing, (220, 180))
    # img[50:330, 20:240] = fing
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
