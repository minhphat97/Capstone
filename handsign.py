import cv2
#import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
flag = 3
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
                flag = 1
                print("It s 1")
                print("New value: ", new_value)
            elif fingerup == [0, 1, 1, 0, 0]:
                new_value = value - 5
                flag = 2
                print("It s 2")
                print("New value: ", new_value)
            elif fingerup == [0, 1, 1, 1, 0]:
                new_value = value
                flag = 3
                print("It s 3")
                print("New value: ", new_value)

    if flag == 1:
        new_value = value + 5
        print("New value: ", new_value)
    elif flag == 2:
        new_value = value - 5
        print("New value: ", new_value)
    elif flag == 3:
        new_value = value
        print("New value: ", new_value)

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
