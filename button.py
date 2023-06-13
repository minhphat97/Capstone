import cv2
import keyboard

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
flag = 3
while True:
    ret, img = video.read()
    value = 10
    if keyboard.is_pressed("a"):
        flag = 1
        print("It s 1")
        print("New value: ", new_value)
    elif keyboard.is_pressed("s"):
        flag = 2
        print("It s 2")
        print("New value: ", new_value)
    elif keyboard.is_pressed("d"):
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
