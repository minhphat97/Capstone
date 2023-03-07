import tkinter as tk
from tkinter import *
import cv2
from PIL import Image

def reset():
    #do_nothing
    print("do nothing")
def show_frame(frame):
    frame.tkraise()

x_ball = 50
y_ball = 100
radius = 10
color = (255, 0, 0)
thickness = 3

root = tk.Tk()  # create root window
root.maxsize(880,330)
root.geometry("880x330")
root.title("IronFoot Technologies")  # title of the GUI window
root.config(bg="pink")  # specify background color
p1 = PhotoImage(file = "icon.png")
root.iconphoto(False, p1)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='nsew')

#============Frame 1 code===========
bg = PhotoImage(file='wall2 (1).png', master=frame1)
image_label = Label(frame1, image = bg)
next_image=PhotoImage("exit.png")
image_label.place(relx=0.5, rely=0.5, anchor=CENTER)
frame1_btn = tk.Button(frame1, text='Next', image=next_image, command=lambda:show_frame(frame2), bg='cyan2', compound = LEFT)
frame1_btn.place(x=440, y=200)
frame1_btn.pack(side=BOTTOM)
show_frame(frame1)

#============Frame 2 code===========
frame2.config(bg="pink")  # specify background color
left_frame = Frame(frame2, width=200, height=400, bg='pink')
left_frame.grid(row=0, column=0, padx=10, pady=10)

right_frame = Frame(frame2, width=650, height=400, bg='pink')
right_frame.grid(row=0, column=1, padx=10, pady=10)

image = PhotoImage(file="ironfoot.png")
original_image = image.subsample(3,3)  # resize image using subsample

Label(left_frame, image=original_image).grid(row=0, column=0, padx=5, pady=5)
image2 = PhotoImage(file="save2.png")


canvas = Canvas(right_frame, bg = "green", height = 300, width = 550)
canvas.pack(padx = 5, pady = 5)
canvas.create_image(0, 0, anchor=NW, image=image2)
canvas.create_oval(x_ball-radius, y_ball-radius, x_ball+radius, y_ball+radius, outline="blue", width=3)


tool_bar = Frame(left_frame, width=180, height=185, bg='pink')
tool_bar.grid(row=2, column=0, padx=5, pady=5)
textbox = Text(left_frame, width=15, height=5)
exit_image=PhotoImage(file='exit.png')
Button(tool_bar, text="Exit", image=exit_image,command=root.quit, bg='red3').grid(row=0, column=0, padx=5, pady=3, ipadx=10) 

reset_image=PhotoImage(file='reset.png')

Button(tool_bar, text="Reset", image=reset_image, command=reset, bg='aquamarine').grid(row=1, column=0, padx=5, pady=3, ipadx=10)
Label(tool_bar, text="PERFORMANCE RATE:",font=("Comic Sans MS", 15, "bold"),bg='pink').grid(row=2, column=0, padx=5, pady=3, ipadx=10)
textbox.grid(row=3, column=0, padx=5, pady=3, ipadx=10)

#============Frame 3 code===========
frame3.config(bg="pink")  # specify background color
left_frame = Frame(frame3, width=200, height=400, bg='pink')
left_frame.grid(row=0, column=0, padx=10, pady=10)

right_frame = Frame(frame3, width=650, height=400, bg='pink')
right_frame.grid(row=0, column=1, padx=10, pady=10)


Label(left_frame, image=original_image).grid(row=0, column=0, padx=5, pady=5)


root.mainloop()