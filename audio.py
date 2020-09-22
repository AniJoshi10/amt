from tkinter import *
import os
import turtle
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
import mysql.connector;
from datetime import date

#Creating the window for New Student registration
window = Tk()
window.title("Student registration.")
window.configure(bg='black')
window.geometry("800x500")
#Background Image
#back_image=ImageTk.PhotoImage(Image.open("pngtree-blue-smart-light-tech-background-backgroundlight-effect-backgroundelectronic-image_81225.jpg"))
#background_label=Label(window,image=back_image)
#background_label.grid(row=0,column=0,rowspan=4,columnspan=2)


#elements for the dropdownbox
clicked=StringVar()
clicked.set("Final")

options={
    "Final",
    "Third",
    "Second"
}


#SGGS Image logo insertion
sggs_image=ImageTk.PhotoImage(Image.open("ci51-01.png"))
image_label=Label(window,image=sggs_image,borderwidth=2, relief="sunken")
image_label.grid(row=0,column=0,columnspan=2)

#Creating a frame for registration
Login_frame=Frame(window,bg="white",borderwidth=2, relief="sunken")
Login_frame.place(x=250,y=220)


#Defining the function to Clear the inpu fields
def clear_input():
    name_box.delete(0, END)
    roll_no_box.delete(0, END)


def insert():
    name=name_box.get()
    roll_no=roll_no_box.get()
    year=clicked.get()
    stats = "Absent"
    cur_date = date.today()
    print(cur_date)

    if year=="Final":
        # Creating connection with the MYSQL database of Final Year
        mydb = mysql.connector.connect(host="", user="", passwd="", database="")
        cursor = mydb.cursor()

        sql = "INSERT INTO Attendance(name,roll_no,class,stats,date) VALUES(%s,%s,%s,%s,%s)"
        args = (name, roll_no, year, stats, cur_date)
        cursor.execute(sql, (name, roll_no, year, stats, cur_date))
        mydb.commit()

        messagebox.showinfo("Success", "Student is successfull enroled!")
    elif year=="Third":
        # Creating connection with the MYSQL database of third Year
        mydb = mysql.connector.connect(host="", user="", passwd="", database="")
        cursor = mydb.cursor()

        sql = "INSERT INTO Attendance_third(name,roll_no,class,stats,date) VALUES(%s,%s,%s,%s,%s)"
        args = (name, roll_no, year, stats, cur_date)
        cursor.execute(sql, (name, roll_no, year, stats, cur_date))
        mydb.commit()

        messagebox.showinfo("Success", "Student is successfull enroled!")
    else:
        # Creating connection with the MYSQL database of second Year
        mydb = mysql.connector.connect(host="", user="", passwd="", database="")
        cursor = mydb.cursor()

        sql = "INSERT INTO Attendance_second(name,roll_no,class,stats,date) VALUES(%s,%s,%s,%s,%s)"
        args = (name, roll_no, year, stats, cur_date)
        cursor.execute(sql, (name, roll_no, year, stats, cur_date))
        mydb.commit()

        messagebox.showinfo("Success", "Student is successfull enroled!")

text=Label(window,text="STUDENT INFO",font=("Candara",10,"bold"),fg="#111111",bg="white",borderwidth=2,relief="sunken").place(x=220,y=210)
#Fields for registraing student
#Creating a label for name
name_label = Label(Login_frame, text="Name",font=("Candara",12,"bold"),fg="#00008B",bg="White")
name_label.grid(row=1,column=0,padx=10,pady=10)

#creating a label for roll_no
roll_no_label=Label(Login_frame,text="Roll No.",font=("Candara",12,"bold"),fg="#00008B",bg="White")
roll_no_label.grid(row=2,column=0,padx=10,pady=10)

#Entry Field for name
name_box=Entry(Login_frame,width=20,font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
name_box.grid(row=1,column=1,padx=10,pady=10)

#creating a Enrty field for roll_no
roll_no_box=Entry(Login_frame,width=20,font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
roll_no_box.grid(row=2,column=1,padx=10,pady=10)

#Label for Subject
sub_label=Label(Login_frame, text="Year",font=("Candara",12,"bold"),fg="#00008B",bg="White")
sub_label.grid(row=3,column=0,padx=10,pady=10)

#Creating entry field for subject
#sub_entry=Entry(manual_frame,width=20)
#sub_entry.grid(row=3,column=1,padx=10,pady=10)

popupMenu = OptionMenu(Login_frame, clicked, *options)
popupMenu.grid(row=3,column=1,padx=10,pady=10,sticky=N+E+W+S)


#Creating submit and clear buttons
submit_btn = Button(Login_frame, text="Submit",font=("Candara",12,"bold"),fg="#00008B",bg="White", command=insert)
reset_button = Button(Login_frame, text="Clear",font=("Candara",12,"bold"),fg="#00008B",bg="White", command=clear_input)

#Setting up grids for submit and reset buttons
submit_btn.grid(row=4, column=1,padx=10,pady=10,ipadx=70)
reset_button.grid(row=4, column=0,padx=10,pady=10,ipadx=20)


window.mainloop()
