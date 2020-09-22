import mysql.connector
import os
import csv
import shutil
import time
from tkinter import *
from datetime import datetime;
import mysql.connector;
from PIL import ImageTk, Image
from tkinter import messagebox

# creating instance of TK
root = Tk()

# stting title for the window
root.title("Central Database")
# root.configure(bg='gray')
p1 = datetime.date(datetime.now())
p = str(datetime.date(datetime.now()))
time = str(time.localtime())

# elements for the dropdownbox
clicked = StringVar()
clicked.set("Final")

options = {
    "Final",
    "Third",
    "Second"
}


# Defining function for clearing input of the field
def clear_input():
    name_box.delete(0, END)
    roll_no_box.delete(0, END)
    return


# Defining function for Database operation
def verify():
    year = clicked.get()
    sub = name_box.get()
    date = roll_no_box.get()
    print(year)
    print(sub)
    print(date)
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="AdityaRP23",
                                   database="practice")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM Central_database WHERE class=%s AND date=%s AND sub=%s;"
    """
    mydata = {
        'yr': year,
        'dt': date,
        'subject': sub
    }
    """
    mycursor.execute(sql,(year,date,sub))
    rows = mycursor.fetchall()
    for tuple in rows:
        print(tuple)
    with open('attendance_' + p + time + '.csv', 'w') as f:
        a = csv.writer(f, delimiter=',')
        #a.writerows(["name", "roll_no", "class", "status", "date", "sub", "time"])  ## etc
        a.writerows(rows)  ## closing paren added

    original = "C:\\Users\\Aditya\\PycharmProjects\\B_Tech_Project\\" + 'attendance_' + p + time + '.csv'
    destination = "C:\\Users\\Aditya\\PycharmProjects\\B_Tech_Project\\Central\\" + 'attendance_' + p + time + '.csv'
    shutil.move(original, destination)

    messagebox.showinfo("Success", "Successfully exported to csv file to central folder.")


    return

# Creating a label for Id
name_label = Label(root, text="Sub", font=("Candara", 12, "bold"), fg="#00008B")
name_label.grid(row=1, column=0, padx=10, pady=10)

# creating a label for Password
roll_no_label = Label(root, text="Date", font=("Candara", 12, "bold"), fg="#00008B")
roll_no_label.grid(row=2, column=0, padx=10, pady=10)

# Entry Field for id
name_box = Entry(root, width=20, font=("Courier new", 12, "bold"), fg="#000000", borderwidth=2, relief="sunken")
name_box.grid(row=1, column=1, padx=10, pady=10)

# creating a Enrty field for Password
roll_no_box = Entry(root, width=20, font=("Courier new", 12, "bold"), fg="#000000", borderwidth=2, relief="sunken")
roll_no_box.grid(row=2, column=1, padx=10, pady=10)

sub_label = Label(root, text="Year", font=("Candara", 12, "bold"), fg="#00008B")
sub_label.grid(row=3, column=0, padx=10, pady=10)

# Creating entry field for subject
# sub_entry=Entry(manual_frame,width=20)
# sub_entry.grid(row=3,column=1,padx=10,pady=10)

popupMenu = OptionMenu(root, clicked, *options)
popupMenu.grid(row=3, column=1, padx=10, pady=10, sticky=N + E + W + S)

# Creating submit and clear buttons
submit_btn = Button(root, text="Submit", font=("Candara", 12, "bold"), fg="#00008B", command=verify)
reset_button = Button(root, text="Clear", font=("Candara", 12, "bold"), fg="#00008B", command=clear_input)

# Setting up grids for submit and reset buttons
submit_btn.grid(row=4, column=1, padx=10, pady=10, ipadx=70)
reset_button.grid(row=4, column=0, padx=10, pady=10, ipadx=20)

root.mainloop()
