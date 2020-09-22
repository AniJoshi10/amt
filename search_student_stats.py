from tkinter import *
# from playsound import playsound
import os
from datetime import datetime;
import mysql.connector;
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector;


root=Tk()
root.title("Scanning database..")

#elements for the dropdownbox
clicked=StringVar()
clicked.set("Final")

options={
    "Final",
    "Third",
    "Second"
}

#Defining function for clearing input of the field
def clear_input():
    name_box.delete(0,END)
    roll_no_box.delete(0,END)
    return

#Defining function for Database operation
def verify():
    year=clicked.get()
    if year=="Final":
        roll_no = roll_no_box.get()
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="AdityaRP23", database="practice")
        cursor = mydb.cursor()
        sql = "SELECT STATS FROM Attendance WHERE roll_no=%(rollno)s;"
        mydata = {
            'rollno': roll_no
        }
        cursor.execute(sql, mydata)
        var1 = cursor.fetchall()
        print_records = ''
        for recod in var1:
            print_records += recod[0]
        if print_records=="Absent":
            query_lab = Label(root, text=print_records, font=("Candara", 12, "bold"),fg="red")
            query_lab.grid(row=5, column=0, columnspan=2)
        else:
            query_lab = Label(root, text=print_records,font=("Candara",12,"bold"))
            query_lab.grid(row=5, column=0, columnspan=2)
        mydb.commit()
    elif year=="Third":
        roll_no = roll_no_box.get()
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="AdityaRP23", database="practice")
        cursor = mydb.cursor()
        sql = "SELECT STATS FROM Attendance_third WHERE roll_no=%(rollno)s;"
        mydata = {
            'rollno': roll_no
        }
        cursor.execute(sql, mydata)
        var1 = cursor.fetchall()
        print_records = ''
        for recod in var1:
            print_records += recod[0]
        if print_records=="Absent":
            query_lab = Label(root, text=print_records, font=("Candara", 12, "bold"),fg="red")
            query_lab.grid(row=5, column=0, columnspan=2)
        else:
            query_lab = Label(root, text=print_records,font=("Candara",12,"bold"))
            query_lab.grid(row=5, column=0, columnspan=2)
        mydb.commit()
    else:
        roll_no = roll_no_box.get()
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="AdityaRP23", database="practice")
        cursor = mydb.cursor()
        sql = "SELECT STATS FROM Attendance_second WHERE roll_no=%(rollno)s;"
        mydata = {
            'rollno': roll_no
        }
        cursor.execute(sql, mydata)
        var1 = cursor.fetchall()
        print_records = ''
        for recod in var1:
            print_records += recod[0]
        if print_records=="Absent":
            query_lab = Label(root, text=print_records, font=("Candara", 12, "bold"),fg="red")
            query_lab.grid(row=5, column=0, columnspan=2)
        else:
            query_lab = Label(root, text=print_records,font=("Candara",12,"bold"))
            query_lab.grid(row=5, column=0, columnspan=2)
        mydb.commit()

    return

#Creating a label for Id
name_label = Label(root, text="Name",font=("Candara",12,"bold"),fg="#00008B")
name_label.grid(row=1,column=0,padx=10,pady=10)

#creating a label for Password
roll_no_label=Label(root,text="Roll No",font=("Candara",12,"bold"),fg="#00008B")
roll_no_label.grid(row=2,column=0,padx=10,pady=10)

#Entry Field for id
name_box=Entry(root,width=20,font=("Courier new",12,"bold"),fg="#000000")
name_box.grid(row=1,column=1,padx=10,pady=10)

#creating a Enrty field for Password
roll_no_box=Entry(root,width=20,font=("Courier new",12,"bold"),fg="#000000")
roll_no_box.grid(row=2,column=1,padx=10,pady=10)

#Label for Subject
sub_label=Label(root, text="Year",font=("Candara",12,"bold"),fg="#00008B")
sub_label.grid(row=3,column=0,padx=10,pady=10)

#Creating entry field for subject
#sub_entry=Entry(manual_frame,width=20)
#sub_entry.grid(row=3,column=1,padx=10,pady=10)

popupMenu = OptionMenu(root, clicked, *options)
popupMenu.grid(row=3,column=1,padx=10,pady=10,sticky=N+E+W+S)


#Creating submit and clear buttons
submit_btn = Button(root, text="Submit",font=("Candara",12,"bold"), command=verify)
reset_button = Button(root, text="Clear",font=("Candara",12,"bold"), command=clear_input)

#Setting up grids for submit and reset buttons
submit_btn.grid(row=4, column=1,padx=10,pady=10,ipadx=75)
reset_button.grid(row=4, column=0,padx=10,pady=10,ipadx=20)


root.mainloop()