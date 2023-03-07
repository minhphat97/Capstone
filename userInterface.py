import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk

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
root.maxsize(2000,1000)
root.geometry("1000x500")
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
frame1_btn_2 = tk.Button(frame1, text='Page2', image=next_image, command=lambda:show_frame(frame3), bg='cyan2', compound = LEFT)
frame1_btn_2.place(x=440, y=200)
frame1_btn_2.pack(side=BOTTOM)
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

# canvas = Canvas(right_frame, bg = "green", height = 300, width = 550)
# canvas.pack(padx = 5, pady = 5)
# canvas.create_image(0, 0, anchor=NW, image=image2)
# canvas.create_oval(x_ball-radius, y_ball-radius, x_ball+radius, y_ball+radius, outline="blue", width=3)

tool_bar = Frame(left_frame, width=180, height=185, bg='pink')
tool_bar.grid(row=2, column=0, padx=5, pady=5)
textbox = Text(left_frame, width=15, height=5)
Button(tool_bar, text="Exit", image=exit_image,command=root.quit, bg='red3').grid(row=0, column=0, padx=5, pady=3, ipadx=10) 
Button(tool_bar, text="Reset", image=reset_image, command=reset, bg='aquamarine').grid(row=1, column=0, padx=5, pady=3, ipadx=10)

Label(tool_bar, text="PERFORMANCE RATE:",font=("Comic Sans MS", 15, "bold"),bg='pink').grid(row=4, column=0, padx=5, pady=3, ipadx=10)
textbox.grid(row=3, column=0, padx=5, pady=3, ipadx=10)

vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
width, height = 50, 20
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
right_frame.bind('<Escape>', lambda e: right_frame.quit())
label_widget = Label(right_frame)
label_widget.pack(padx = 0, pady = 0)

def open_camera():
    _, frame = vid.read()
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    captured_image = Image.fromarray(opencv_image)
    photo_image = ImageTk.PhotoImage(image=captured_image)
    label_widget.photo_image = photo_image
    label_widget.configure(image=photo_image)
    label_widget.after(5, open_camera)

Button(tool_bar, text="OpenCamera", command=open_camera, bg='aquamarine').grid(row=2, column=0, padx=5, pady=3, ipadx=10)
# button1 = Button(right_frame, text="Oen Camera", command=open_camera)
# button1.pack()



root.mainloop()