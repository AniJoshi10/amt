from tkinter import *
import os
from datetime import datetime;
import mysql.connector;
from datetime import date
from tkinter import messagebox
import cv2
import os
import mysql.connector
import os
import csv
from datetime import datetime
import shutil
import time
from tkinter import *
import os
from datetime import datetime;
import mysql.connector;
from PIL import ImageTk,Image
from tkinter import messagebox


root = Tk()

# stting title for the window
root.title("Reset database")

#elements for the dropdownbox
clicked=StringVar()
clicked.set("Final")

options={
    "Final",
    "Third",
    "Second"
}

def verify():
    year=clicked.get()
    if year=="Final":
        # Creating connection with the MYSQL database
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="AdityaRP23", database="practice")
        cursor = mydb.cursor()

        # Taking date from device
        cur_date = date.today()

        # Generating Query to reset database to today and chnging status to Absent
        sql_query = "update Attendance SET date=current_date(),stats='Absent';"
        cursor.execute(sql_query);
        mydb.commit()
        messagebox.showinfo("Success","Final year database is reseted.")
    elif year=="Third":
        # Creating connection with the MYSQL database
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="AdityaRP23", database="practice")
        cursor = mydb.cursor()

        # Taking date from device
        cur_date = date.today()

        # Generating Query to reset database to today and chnging status to Absent
        sql_query = "update Attendance_third SET date=current_date(),stats='Absent';"
        cursor.execute(sql_query);
        mydb.commit()
        messagebox.showinfo("Success","Third year database is reseted.")
    else:
        # Creating connection with the MYSQL database
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="AdityaRP23", database="practice")
        cursor = mydb.cursor()

        # Taking date from device
        cur_date = date.today()

        # Generating Query to reset database to today and chnging status to Absent
        sql_query = "update Attendance_second SET date=current_date(),stats='Absent';"
        cursor.execute(sql_query);
        mydb.commit()
        messagebox.showinfo("Success","Second year database is reseted.")

    return

text=Label(root, text="Please select Year to reset Attendance.",font=("Candara",12,"bold"),fg="#00008B")
text.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
#Label for Subject
sub_label=Label(root, text="Year",font=("Candara",12,"bold"),fg="#00008B")
sub_label.grid(row=2,column=0,padx=10,pady=10)

#Creating entry field for subject
#sub_entry=Entry(manual_frame,width=20)
#sub_entry.grid(row=3,column=1,padx=10,pady=10)

popupMenu = OptionMenu(root, clicked, *options,)
popupMenu.grid(row=2,column=1,padx=10,pady=10,sticky=N+E+W+S)

#Setting up button for submit
submit_btn = Button(root, text="Submit",font=("Candara",12,"bold"),fg="#00008B", command=verify)
submit_btn.grid(row=3, column=1,padx=10,pady=10,ipadx=20)

root.mainloop()