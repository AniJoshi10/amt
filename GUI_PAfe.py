# import module from tkinter for UI
from tkinter import *
# from playsound import playsound
import os
from datetime import datetime;
import mysql.connector;
from PIL import ImageTk,Image

# creating instance of TK
root = Tk()

# stting title for the window
root.title("SGGS Attendance Portal")

#Setting up the background Image
back_image=ImageTk.PhotoImage(Image.open("pngtree-blue-smart-light-tech-background-backgroundlight-effect-backgroundelectronic-image_81225.jpg"))
background_label=Label(root,image=back_image)
background_label.grid(row=0,column=0,rowspan=4,columnspan=2)

#Adding SGGS Logo Image in top
sggs_image=ImageTk.PhotoImage(Image.open("ci51-01.png"))
image_label=Label(root,image=sggs_image,borderwidth=2, relief="sunken")
image_label.grid(row=0,column=0,columnspan=2)

#Setting up the frame for butoons
bg_frame=Frame(root,bg="skyblue",borderwidth=2, relief="sunken")
bg_frame.place(x=320,y=200)


# root.geometry("300x300")

def function1():
    return


def function2():
    return

def function3():
    return    # playsound('sound.mp3')


def function5():
    root.destroy()


def function6():
    return

def attend():
    return




# creating first button
create_face_button=Button(bg_frame, text="Create Face Dataset", font=("Arial",15), command=function1)
create_face_button.grid(row=0,column=0, sticky=N+E+W+S,padx=5, pady=5)
# creating second button

train_faces_button=Button(bg_frame, text="Train Face Dataset",font=("Arial",15),command=function2)
train_faces_button.grid(row=1, column=0,sticky=N+E+W+S, padx=5, pady=5)
# creating third button


recognize_face_and_set_attendance=Button(bg_frame, text="Recognize Face and Set Attendance",font=("Arial",15),command=function3)
recognize_face_and_set_attendance.grid(row=2, column=0, sticky=N+E+W+S,padx=5, pady=5)

# creating attendance button

generate_attendance_button=Button(bg_frame, text="Generate Attendance Sheet",font=("Arial",15),command=attend)
generate_attendance_button.grid(row=3, column=0, sticky=N+E+W+S,padx=5, pady=5)



enter_student_details_button=Button(bg_frame, text="Enter students details",font=("Arial",15),command=function6)
enter_student_details_button.grid(row=4, column=0, sticky=N+E+W+S,padx=5, pady=5)

exit_button=Button(bg_frame, text="Exit",font=("Arial",15), command=function5)
exit_button.grid(row=5,column=0,sticky=N+E+W+S,padx=5, pady=5)



root.mainloop()