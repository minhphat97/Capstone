import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import pathlib
import datetime as dt
from time import strftime
import csv
import time
import subprocess

def reset():
    #do_nothing
    print("do nothing")
def show_frame(frame):
    frame.tkraise()
def helloCallBack():
    subprocess.run("python3 PID_control.py & python3 objectBallFeeder.py.py & python3 objectBallNano.py", shell=True) # previously python objectNano.py & python objectBallNano.py
    # to open python scripts in separate terminals. Maybe only the PID control should be opened in separate terminal. 
    # in that case, then remove PID control from the above subprocess, then copy and paste the below line before the subprocess.run line
    # subprocess.Popen(['gnome-terminal', '--', 'python3', 'PID_control.py'])
    # subprocess.Popen(['gnome-terminal', '--', 'python3', 'objectBallFeeder.py'])
    # subprocess.Popen(['gnome-terminal', '--', 'python3', 'objectBallNano.py'])

# x_ball = 50
# y_ball = 100
# x_ball_1 = 100
# y_ball_1 = 50
# x_ball_2 = 500
# y_ball_2 = 500
X = []
Y = []
X_player = []
Y_player = []
with open('outputtest.csv') as file:
    for row in file:
        X.append(row.split(",")[0])
        Y.append(row.split(",")[1])
        X_player.append(row.split(",")[0])
        Y_player.append(row.split(",")[1])

# for x in range(len(X)):
#     print (X[x])
# for x in range(len(Y)):
#     print (Y[x])

# time.sleep(5000)

radius = 18
color = (255, 0, 0)
thickness = 4
cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
clf = cv2.CascadeClassifier(str(cascade_path))
root = tk.Tk()  # create root window
root.maxsize(1080, 566)
root.geometry("1080x566")
#root.geometry("1000x500")
root.title("IronFoot Technologies")  # title of the GUI window
root.config(bg="pink")  # specify background color
p1 = PhotoImage(file = "icon.png")
root.iconphoto(False, p1)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)
for frame in (frame1, frame2, frame3, frame4):
    frame.grid(row=0, column=0, sticky='nsew')

#============================================Frame 1 code============================================
bg_img = PhotoImage(file='imagBall.png', master=frame1)
label = Label(root, image = bg_img)
label.pack
canvas = Canvas(frame1, width=1080, height=566)
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=bg_img)
canvas.create_rectangle(3, 3, 1075, 556, outline = "lightpink2", width = 60)
frame1_btn = tk.Button(frame1, text='PAGE 1', command=lambda:show_frame(frame2), bg='cyan2', compound = LEFT)
frame1_btn.place(x=408, y=530)
# frame1_btn_2 = tk.Button(frame1, text='PAGE 2', command=lambda:show_frame(frame3), bg='cyan2', compound = LEFT)
# frame1_btn_2.place(x=500, y=530)
frame1_btn_3 = tk.Button(frame1, text='PAGE 2', command=lambda:show_frame(frame4), bg='cyan2', compound = LEFT)
frame1_btn_3.place(x=500, y=530)
play_button = tk.Button(frame1, text='RUN', command=helloCallBack, bg='aquamarine', compound = LEFT)
play_button.place(x=592, y=530)



date = dt.datetime.now()
label = Label(frame1, text=f"{date:%A, %B %d, %Y}", font="Calibri, 20")
label.place(x=380, y=450)

label = Label(frame1, text=strftime('%H:%M:%S %p'), font="Calibri, 20")
label.place(x=440, y=80)
show_frame(frame1)

#============================================Frame 2 code===========================================
frame2.config(bg="pink")  # specify background color
left_frame = Frame(frame2, width=200, height=400, bg='pink')
left_frame.grid(row=0, column=0, padx=10, pady=10)

right_frame = Frame(frame2, width=650, height=400, bg='pink')
right_frame.grid(row=0, column=1, padx=10, pady=10)

image = PhotoImage(file="ironfoot.png")
original_image = image.subsample(3,3)  # resize image using subsample

Label(left_frame, image=original_image).grid(row=0, column=0, padx=5, pady=5)
image2 = PhotoImage(file="netImage.png") #760x532

canvas = Canvas(right_frame, bg = "green", height = 532, width = 760)
canvas.pack(padx = 5, pady = 5)
canvas.create_image(0, 0, anchor=NW, image=image2)

for i in range(len(X)):
   canvas.create_oval(float(X[i])-radius, float(Y[i])-radius, float(X[i])+radius, float(Y[i])+radius, outline="blue", width=3) 



tool_bar = Frame(left_frame, width=180, height=185, bg='pink')
tool_bar.grid(row=2, column=0, padx=5, pady=5)
textbox = Text(left_frame, width=20, height=10)
exit_image=PhotoImage(file='exit.png')
Button(tool_bar, text="Exit", image=exit_image,command=root.quit, bg='red3', width = 50).grid(row=0, column=0, padx=5, pady=3, ipadx=10) 
reset_image=PhotoImage(file='reset.png')
Button(tool_bar, text="Reset", image=reset_image, command=reset, bg='aquamarine', width = 50).grid(row=1, column=0, padx=5, pady=3, ipadx=10)
home_image=PhotoImage(file = "home.png")
Button(tool_bar, text="Home", image=home_image, command=lambda:show_frame(frame1), bg='dodgerblue1', width = 50).grid(row=2, column=0, padx=5, pady=3, ipadx=10)
next_image=PhotoImage(file = "next.png")
Button(tool_bar, text="Next", image=next_image, command=lambda:show_frame(frame3), bg='khaki1', width = 50).grid(row=3, column=0, padx=5, pady=3, ipadx=10)

Label(tool_bar, text="PERFORMANCE RATE:",font=("Comic Sans MS", 15, "bold"),bg='pink').grid(row=4, column=0, padx=5, pady=3, ipadx=10)
textbox.grid(row=5, column=0, padx=5, pady=3, ipadx=10)

#==============================================Frame 3 code=========================================
# frame3.config(bg="pink")  # specify background color
# left_frame = Frame(frame3, width=200, height=400, bg='pink')
# left_frame.grid(row=0, column=0, padx=10, pady=10)

# right_frame = Frame(frame3, width=650, height=400, bg='pink')
# right_frame.grid(row=0, column=1, padx=10, pady=10)

# Label(left_frame, image=original_image).grid(row=0, column=0, padx=5, pady=5)

# tool_bar = Frame(left_frame, width=180, height=185, bg='pink')
# tool_bar.grid(row=2, column=0, padx=5, pady=5)
# textbox = Text(left_frame, width=20, height=10)
# Button(tool_bar, text="Exit", image=exit_image,command=root.quit, bg='red3', width = 50).grid(row=0, column=0, padx=5, pady=3, ipadx=10) 
# Button(tool_bar, text="Reset", image=reset_image, command=reset, bg='aquamarine', width = 50).grid(row=1, column=0, padx=5, pady=3, ipadx=10)

# Label(tool_bar, text="PERFORMANCE RATE:",font=("Comic Sans MS", 15, "bold"),bg='pink').grid(row=5, column=0, padx=5, pady=3, ipadx=10)
# textbox.grid(row=6, column=0, padx=5, pady=3, ipadx=10)

# vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# # width, height = 50, 20
# vid.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
# # vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
# right_frame.bind('<Escape>', lambda e: right_frame.quit())
# label_widget = Label(right_frame)
# label_widget.pack(padx = 0, pady = 0)

# def open_camera():
#     _, frame = vid.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = clf.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30, 30),
#         flags=cv2.CASCADE_SCALE_IMAGE
#     )
#     for (x, y, width, height) in faces:
#         cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 255, 0), 2)
#         break
#     opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#     #cv2.imshow("Frame", frame)
#     captured_image = Image.fromarray(opencv_image)
#     photo_image = ImageTk.PhotoImage(image=captured_image)
#     label_widget.photo_image = photo_image
#     label_widget.configure(image=photo_image)
#     label_widget.after(5, open_camera)

#Button(tool_bar, text="Open Camera", command=open_camera, bg='aquamarine').grid(row=2, column=0, padx=5, pady=3, ipadx=10)
# webcam_image=PhotoImage(file='webcam.png')
# Button(tool_bar, text="Webcam", image=webcam_image, command=open_camera, bg='aqua', width = 50).grid(row=2, column=0, padx=5, pady=3, ipadx=10)
# Button(tool_bar, text="Next", image=next_image, command=lambda:show_frame(frame4), bg='dodgerblue1', width = 50).grid(row=3, column=0, padx=5, pady=3, ipadx=10)
back_image=PhotoImage(file='back.png')
# Button(tool_bar, text="Back", image=back_image, command=lambda:show_frame(frame2), bg='khaki1', width = 50).grid(row=4, column=0, padx=5, pady=3, ipadx=10)

#==============================================Frame 4 code=========================================
frame4.config(bg="pink")  # specify background color
left_frame = Frame(frame4, width=200, height=400, bg='pink')
left_frame.grid(row=0, column=0, padx=10, pady=10)

right_frame = Frame(frame4, width=650, height=400, bg='pink')
right_frame.grid(row=0, column=1, padx=10, pady=10)

Label(left_frame, image=original_image).grid(row=0, column=0, padx=5, pady=5)

image4 = PhotoImage(file="soccerfield.png") #760x532
canvas = Canvas(right_frame, bg = "green", height = 532, width = 760)
canvas.pack(padx = 5, pady = 5)
canvas.create_image(0, 0, anchor=NW, image=image4)

for i in range(len(X_player)):
   canvas.create_oval(float(X_player[i])-radius, float(Y_player[i])-radius, float(X_player[i])+radius, float(Y_player[i])+radius, outline="blue", width=3)

tool_bar = Frame(left_frame, width=180, height=185, bg='pink')
tool_bar.grid(row=2, column=0, padx=5, pady=5)
textbox = Text(left_frame, width=20, height=10)

Button(tool_bar, text="Exit", image=exit_image,command=root.quit, bg='red3', width = 50).grid(row=0, column=0, padx=5, pady=3, ipadx=10) 
Button(tool_bar, text="Reset", image=reset_image, command=reset, bg='aquamarine', width = 50).grid(row=1, column=0, padx=5, pady=3, ipadx=10)
Button(tool_bar, text="Home", image=home_image, command=lambda:show_frame(frame1), bg='dodgerblue1', width = 50).grid(row=2, column=0, padx=5, pady=3, ipadx=10)
Button(tool_bar, text="Back", image=back_image, command=lambda:show_frame(frame2), bg='khaki1', width = 50).grid(row=3, column=0, padx=5, pady=3, ipadx=10)

Label(tool_bar, text="PLAYER POSITION",font=("Comic Sans MS", 15, "bold"),bg='pink').grid(row=4, column=0, padx=5, pady=3, ipadx=10)
root.mainloop()
