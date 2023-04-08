# create 3 page frames for KickPro Application
root = tk.Tk()
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)

# config frame 1
frame1.addBackGroundImage() # add image background to frame 1
# add first button to point to the 2nd frame
frame1_btn = tk.Button(frame1, text='PAGE 1', command=lambda:show_frame(frame2), bg='cyan2', compound = LEFT)  
frame1_btn.place(x=408, y=530)
# add second button to point to the 3rd frame
frame1_btn_2 = tk.Button(frame1, text='PAGE 2', command=lambda:show_frame(frame3), bg='cyan2', compound = LEFT)
frame1_btn_2.place(x=590, y=530)

# config frame 2
frame2.config(bg="pink")
# the position of ball in net will be displayed in an image
canvas.create_image(0, 0, anchor=NW, image=image2)
canvas.create_oval(x_ball-radius, y_ball-radius, x_ball+radius, y_ball+radius, outline="blue", width=3)
# textbox will contain feedback to players
textbox = Text(left_frame, width=20, height=10)
# add exit button
Button(tool_bar, text="Exit", image=exit_image,command=root.quit, bg='red3', width = 50)
# add reset button
Button(tool_bar, text="Reset", image=reset_image, command=reset, bg='aquamarine', width = 50)
# add home button
Button(tool_bar, text="Home", image=home_image, command=lambda:show_frame(frame1), bg='dodgerblue1', width = 50)
# next button
Button(tool_bar, text="Next", image=next_image, command=lambda:show_frame(frame3), bg='khaki1', width = 50)

# config frame 3
frame3.config(bg="pink")
# add exit button
Button(tool_bar, text="Exit", image=exit_image,command=root.quit, bg='red3', width = 50)
# add reset button
Button(tool_bar, text="Reset", image=reset_image, command=reset, bg='aquamarine', width = 50)
# add webcam button
Button(tool_bar, text="Webcam", image=webcam_image, command=open_camera, bg='aqua', width = 50)
# add home button
Button(tool_bar, text="Home", image=home_image, command=lambda:show_frame(frame1), bg='dodgerblue1', width = 50)
# add back button
Button(tool_bar, text="Back", image=back_image, command=lambda:show_frame(frame2), bg='khaki1', width = 50)
# function to enable webcam when button Webcam is pressed
def open_camera():
    _, frame = vid.read()