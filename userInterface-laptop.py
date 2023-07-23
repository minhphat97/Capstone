import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import pathlib
import datetime as dt
from time import strftime
import csv

csv_file_path = '/home/jg26/Capstone/outputtest.csv'
csv_file_path_2 = '/home/jg26/Capstone/outputtestPlayer.csv'
def reset():
    with open(csv_file_path, 'w') as file:
        file.truncate(0)
    print("CSV file ball emptied successfully.")

    with open(csv_file_path_2, 'w') as file:
        file.truncate(0)
    print("CSV file player emptied successfully.")

def show_frame(frame):
    frame.tkraise()

X = []
Y = []
X_player = []
Y_player = []

def is_csv_file_empty(csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        return not any(csv_reader)

if is_csv_file_empty(csv_file_path):
    print("No data ball")
else:
    print("Some data ball")
    with open(csv_file_path) as file:
        for row in file:
            X.append(row.split(",")[0])
            Y.append(row.split(",")[1])

if is_csv_file_empty(csv_file_path_2):
    print("No data player")
else:
    print("Some data player")
    with open(csv_file_path_2) as file:
        for row in file:
            X_player.append(row.split(",")[0])
            Y_player.append(row.split(",")[1])

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
p1 = PhotoImage(file = "/home/jg26/Capstone/icon.png")
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
bg_img = PhotoImage(file='/home/jg26/Capstone/imagBall.png', master=frame1)
label = Label(root, image = bg_img)
label.pack
canvas = Canvas(frame1, width=1080, height=566)
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=bg_img)
canvas.create_rectangle(3, 3, 1075, 556, outline = "lightpink2", width = 60)
frame1_btn = tk.Button(frame1, text='PAGE 1', command=lambda:show_frame(frame2), bg='cyan2', compound = LEFT)
frame1_btn.place(x=408, y=530)
frame1_btn_3 = tk.Button(frame1, text='PAGE 2', command=lambda:show_frame(frame4), bg='cyan2', compound = LEFT)
frame1_btn_3.place(x=590, y=530)

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

image = PhotoImage(file="/home/jg26/Capstone/ironfoot.png")
original_image = image.subsample(3,3)  # resize image using subsample

Label(left_frame, image=original_image).grid(row=0, column=0, padx=5, pady=5)
image2 = PhotoImage(file="/home/jg26/Capstone/netImage.png") #760x532

canvas = Canvas(right_frame, bg = "green", height = 532, width = 760)
canvas.pack(padx = 5, pady = 5)
canvas.create_image(0, 0, anchor=NW, image=image2)

for i in range(len(X)):
   canvas.create_oval(float(X[i])-radius, float(Y[i])-radius, float(X[i])+radius, float(Y[i])+radius, outline="blue", width=3) 

tool_bar = Frame(left_frame, width=180, height=185, bg='pink')
tool_bar.grid(row=2, column=0, padx=5, pady=5)

exit_image=PhotoImage(file='/home/jg26/Capstone/exit.png')
Button(tool_bar, text="Exit", image=exit_image,command=lambda: [root.quit(), reset()], bg='red3', width = 50).grid(row=0, column=0, padx=5, pady=3, ipadx=10) 
home_image=PhotoImage(file = "/home/jg26/Capstone/home.png")
Button(tool_bar, text="Home", image=home_image, command=lambda:show_frame(frame1), bg='dodgerblue1', width = 50).grid(row=2, column=0, padx=5, pady=3, ipadx=10)
next_image=PhotoImage(file = "/home/jg26/Capstone/next.png")
Button(tool_bar, text="Next", image=next_image, command=lambda:show_frame(frame4), bg='khaki1', width = 50).grid(row=3, column=0, padx=5, pady=3, ipadx=10)

Label(tool_bar, text="GOAL POSITION:",font=("Comic Sans MS", 15, "bold"),bg='pink').grid(row=4, column=0, padx=5, pady=3, ipadx=10)

back_image=PhotoImage(file='/home/jg26/Capstone/back.png')

#==============================================Frame 4 code=========================================
frame4.config(bg="pink")  # specify background color
left_frame = Frame(frame4, width=200, height=400, bg='pink')
left_frame.grid(row=0, column=0, padx=10, pady=10)

right_frame = Frame(frame4, width=650, height=400, bg='pink')
right_frame.grid(row=0, column=1, padx=10, pady=10)

Label(left_frame, image=original_image).grid(row=0, column=0, padx=5, pady=5)

image4 = PhotoImage(file="/home/jg26/Capstone/soccerfield.png") #760x532
canvas = Canvas(right_frame, bg = "green", height = 532, width = 760)
canvas.pack(padx = 5, pady = 5)
canvas.create_image(0, 0, anchor=NW, image=image4)

for i in range(len(X_player)):
   canvas.create_oval(float(X_player[i])-radius, float(Y_player[i])-radius, float(X_player[i])+radius, float(Y_player[i])+radius, outline="blue", width=3)

tool_bar = Frame(left_frame, width=180, height=185, bg='pink')
tool_bar.grid(row=2, column=0, padx=5, pady=5)
textbox = Text(left_frame, width=20, height=10)

Button(tool_bar, text="Exit", image=exit_image,command=lambda: [root.quit(), reset()], bg='red3', width = 50).grid(row=0, column=0, padx=5, pady=3, ipadx=10) 
Button(tool_bar, text="Home", image=home_image, command=lambda:show_frame(frame1), bg='dodgerblue1', width = 50).grid(row=2, column=0, padx=5, pady=3, ipadx=10)
Button(tool_bar, text="Back", image=back_image, command=lambda:show_frame(frame2), bg='khaki1', width = 50).grid(row=3, column=0, padx=5, pady=3, ipadx=10)

Label(tool_bar, text="PLAYER POSITION",font=("Comic Sans MS", 15, "bold"),bg='pink').grid(row=4, column=0, padx=5, pady=3, ipadx=10)
root.mainloop()