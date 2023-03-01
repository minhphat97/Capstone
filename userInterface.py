from tkinter import *

root = Tk()  # create root window
root.title("IronFoot Technologies")  # title of the GUI window
root.maxsize(900, 600)  # specify the max size the window can expand to
root.config(bg="pink")  # specify background color

# Create left and right frames
left_frame = Frame(root, width=200, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=10)

right_frame = Frame(root, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=10)


# load image to be "edited"
image = PhotoImage(file="testPhoto.png")
original_image = image.subsample(3,3)  # resize image using subsample
Label(left_frame, image=original_image).grid(row=0, column=0, padx=5, pady=5)

# Display image in right_frame
image2 = PhotoImage(file="net2-PhotoRoom.png")
Label(right_frame, image=image2).grid(row=0,column=0, padx=5, pady=5)

# Create tool bar frame
tool_bar = Frame(left_frame, width=180, height=185)
tool_bar.grid(row=2, column=0, padx=5, pady=5)
textbox = Text(left_frame, width=15, height=5)
# Example labels that serve as placeholders for other widgets
Label(tool_bar, text="Done", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
Label(tool_bar, text="Reset", relief=RAISED).grid(row=1, column=0, padx=5, pady=3, ipadx=10)
Label(tool_bar, text="Perfomance Score", relief=RAISED).grid(row=2, column=0, padx=5, pady=3, ipadx=10)
textbox.grid(row=3, column=0, padx=5, pady=3, ipadx=10)
root.mainloop()