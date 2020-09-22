# import module from tkinter for UI for Project
from tkinter import *
# from playsound import playsound
import os
from datetime import datetime;
import mysql.connector;
from PIL import ImageTk,Image
from tkinter import messagebox
# creating instance of TK
root = Tk()

# stting title for the window
root.title("SGGS Attendance Portal")
root.resizable(False,False)
#Setting up the background Image
back_image=ImageTk.PhotoImage(Image.open("6308362bb768cc6a787edf7463b41d5e-700.jpg"))
background_label=Label(root,image=back_image)
background_label.grid(row=0,column=0,rowspan=4,columnspan=2)

#Adding SGGS Logo Image in top
sggs_image=ImageTk.PhotoImage(Image.open("ci51-01.png"))
image_label=Label(root,image=sggs_image,borderwidth=2, relief="sunken")
image_label.grid(row=0,column=0,columnspan=2)

#Setting up the frame for butoons
bg_frame=Frame(root,bg="black",borderwidth=2, relief="sunken")
bg_frame.place(x=730,y=280)


#Setting up the frame for Manually Filling the attendance
manual_frame=Frame(root,bg="white",borderwidth=2, relief="sunken")
manual_frame.place(x=100,y=250)


#Setting downside Frame
down_frame=Frame(root,bg="black",borderwidth=2, relief="sunken")
down_frame.place(x=210,y=600)



#elements for the dropdownbox
clicked=StringVar()
clicked.set("Final")

options={
    "Final",
    "Third",
    "Second"
}


#functiond for manually filling the attendance

def clear_input():
    id_box.delete(0, END)
    passwd_box.delete(0, END)



def verify():
    global name
    global roll_no
    global year_of_student
    if id_box.get()=="" or passwd_box.get()=="":
        messagebox.showwarning("Warning","Please Enter The Fields")
    else:
        name = id_box.get()
        roll_no=passwd_box.get()
        year_of_student = clicked.get()
        # Updating the database
        if year_of_student=="Final":
            mydb = mysql.connector.connect(host="", user="", passwd="", database="")
            mycursor = mydb.cursor()

            sql = "UPDATE Attendance SET stats='Present' WHERE roll_no=%(rollno)s;"
            mydata = {
                'rollno': roll_no
            }
            mycursor.execute(sql, mydata)
            mydb.commit()
            messagebox.showinfo("Success", "Updation Successfull")
        elif year_of_student=="Third":
            mydb = mysql.connector.connect(host="", user="", passwd="", database="")
            mycursor = mydb.cursor()

            sql = "UPDATE Attendance_third SET stats='Present' WHERE roll_no=%(rollno)s;"
            mydata = {
                'rollno': roll_no
            }
            mycursor.execute(sql, mydata)
            mydb.commit()
            messagebox.showinfo("Success", "Updation Successfull")
        else:
            mydb = mysql.connector.connect(host="", user="", passwd="", database="")
            mycursor = mydb.cursor()

            sql = "UPDATE Attendance_second SET stats='Present' WHERE roll_no=%(rollno)s;"
            mydata = {
                'rollno': roll_no
            }
            mycursor.execute(sql, mydata)
            mydb.commit()
            messagebox.showinfo("Success", "Updation Successfull")

# root.geometry("300x300")

def function1():
    #Calling program for capturing students face images and store it in specified folder
    os.system("face_capture.py")
    messagebox.showinfo("Success","Face is succussfully captured.")
    return


def function2():
    os.system("face_images_training.py")
    messagebox.showinfo("Success!","Dataset is trained Succesfully..")
    return

def function3():
    root.destroy()
    os.system("face_recognization.py")
    os.system("temp.py")
    return


def function5():
    root.destroy()
    os.system("audio.py")
    os.system("temp.py")

def function6():
    root.destroy()

    os.system("search_student_stats.py")
    os.system("temp.py")
    return


def Reset_database():
    #Calling program to reset database to tadays date and satus=Absent
    os.system("reset_attendance.py")
    return

def attend():
    #Calling program for creating excel file
    os.system("animation.py")
    return

def central_database():
    os.system("central_database.py")
    return




# creating first button
create_face_button=Button(down_frame, text="Take student images",font=("Candara",15,"bold"),fg="#00008B",bg="White", command=function1)
create_face_button.grid(row=0,column=0, sticky=N+E+W+S,padx=20, pady=5)
# creating second button

train_faces_button=Button(down_frame, text="Retrain student Dataset",font=("Candara",15,"bold"),fg="#00008B",bg="White",command=function2)
train_faces_button.grid(row=0, column=1,sticky=N+E+W+S, padx=20, pady=5)
# creating third button


recognize_face_and_set_attendance=Button(down_frame, text="Recognize Face.",font=("Candara",15,"bold"),fg="#00008B",bg="White",command=function3)
recognize_face_and_set_attendance.grid(row=0, column=2, sticky=N+E+W+S,padx=20, pady=5)

# creating attendance button

generate_attendance_button=Button(bg_frame, text="Print Attendance Sheet",font=("Candara",15,"bold"),fg="#00008B",bg="White",command=attend)
generate_attendance_button.grid(row=0, column=0, sticky=N+E+W+S,padx=5, pady=5)



enter_student_details_button=Button(bg_frame, text="Search Student status",font=("Candara",15,"bold"),fg="#00008B",bg="White",command=function6)
enter_student_details_button.grid(row=1, column=0, sticky=N+E+W+S,padx=5, pady=5)

reset_database_button=Button(bg_frame, text="Reset Attendace today.",font=("Candara",15,"bold"),fg="#00008B",bg="White",command=Reset_database)
reset_database_button.grid(row=2, column=0, sticky=N+E+W+S,padx=5, pady=5)

exit_button=Button(bg_frame, text="Register New Student",font=("Candara",15,"bold"),fg="#00008B",bg="White", command=function5)
exit_button.grid(row=3,column=0,sticky=N+E+W+S,padx=5, pady=5)

#Fields for Manually filling the attendance
#Creating a label for Id
id_label = Label(manual_frame, text="",font=("Arial",12),bg="White")
id_label.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
id_label = Label(manual_frame, text="Name",font=("Arial",12),bg="White")
id_label.grid(row=2,column=0,padx=10,pady=10)

#creating a label for Password
passwd_label=Label(manual_frame,text="Roll No.",font=("Arial",12),bg="White")
passwd_label.grid(row=3,column=0,padx=10,pady=10)

#Entry Field for id
id_box=Entry(manual_frame,width=20)
id_box.grid(row=2,column=1,padx=10,pady=10)

#creating a Enrty field for Password
passwd_box=Entry(manual_frame,width=20,show='*')
passwd_box.grid(row=3,column=1,padx=10,pady=10)

#Label for Subject
sub_label=Label(manual_frame, text="Year",font=("Arial",12),bg="White")
sub_label.grid(row=4,column=0,padx=10,pady=10)

#Creating entry field for subject
#sub_entry=Entry(manual_frame,width=20)
#sub_entry.grid(row=3,column=1,padx=10,pady=10)

popupMenu = OptionMenu(manual_frame, clicked, *options)
popupMenu.grid(row=4,column=1,padx=10,pady=10,sticky=N+E+W+S)


#Creating submit and clear buttons
submit_btn = Button(manual_frame, text="Fill Manually",font=("Arial",12), command=verify)
reset_button = Button(manual_frame, text="Clear",font=("Arial",12), command=clear_input)

#Setting up grids for submit and reset buttons
submit_btn.grid(row=5, column=1,padx=10,pady=10,ipadx=40)
reset_button.grid(row=5, column=0,padx=10,pady=10,ipadx=20)

central_database_search=Button(root, text="Scan central",font=("Candara",15,"bold"),fg="#00008B",bg="White", command=central_database)
central_database_search.place(x=790,y=490)


text=Label(root,text="MANUAL ATTENDANCE",font=("Arial",12,"bold"),fg="#00008B",bg="White",borderwidth=2,relief="sunken").place(x=160,y=260)

text1=Label(root,text="STUDENT'S RELATED",font=("Arial",12,"bold"),fg="black",bg="White",borderwidth=2,relief="sunken").place(x=755,y=255)
text2=Label(root,text="FACE RELATED",font=("Arial",12,"bold"),fg="black",bg="White",borderwidth=2,relief="sunken").place(x=190,y=580)

#Running main GUI window
root.mainloop()
