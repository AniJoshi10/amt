from tkinter import *
import os
import turtle
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
import mysql.connector;
from datetime import date
import bcrypt
import time

#Creating the window for New Student registration
window = Tk()
window.title("Faculty registration.")
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
    email_box.delete(0,END)


def insert():
    id=name_box.get()
    pas=roll_no_box.get()
    email=email_box.get()
    #Calculating the cost factor
    starting=time.time()
    passwd = pas.encode()
    # Random initial salt to be added to passwd rounds=15
    salt = bcrypt.gensalt(16)

    # Hashed value to be stored in Database
    hashed = bcrypt.hashpw(passwd, salt)

    # Creating connection with the MYSQL database of Final Year
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="AdityaRP23", database="practice")
    cursor = mydb.cursor()

    sql = "INSERT INTO passwords(id,pass,email) VALUES(%s,%s,%s)"
    args = (id,hashed, email)
    cursor.execute(sql, (id,hashed, email))
    mydb.commit()
    #ending
    ending=time.time()
    print(ending-starting)
    messagebox.showinfo("Success", "Faculty info is inserted!")

text=Label(window,text="FACULTY INFO",font=("Candara",12,"bold"),fg="#111111",bg="white",borderwidth=2,relief="sunken").place(x=220,y=210)
#Fields for registraing student
#Creating a label for name
name_label = Label(Login_frame, text="Faculty id.",font=("Candara",12,"bold"),fg="#00008B",bg="White")
name_label.grid(row=1,column=0,padx=10,pady=10)

#creating a label for roll_no
roll_no_label=Label(Login_frame,text="Passward.",font=("Candara",12,"bold"),fg="#00008B",bg="White")
roll_no_label.grid(row=2,column=0,padx=10,pady=10)

#Entry Field for name
name_box=Entry(Login_frame,width=20,font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
name_box.grid(row=1,column=1,padx=10,pady=10)

#creating a Enrty field for roll_no
roll_no_box=Entry(Login_frame,width=20,show='*',font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
roll_no_box.grid(row=2,column=1,padx=10,pady=10)

#Label for Subject
sub_label=Label(Login_frame, text="Email id.",font=("Candara",12,"bold"),fg="#00008B",bg="White")
sub_label.grid(row=3,column=0,padx=10,pady=10)

#Creating entry field for subject
#sub_entry=Entry(manual_frame,width=20)
#sub_entry.grid(row=3,column=1,padx=10,pady=10)

email_box=Entry(Login_frame,width=20,font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
email_box.grid(row=3,column=1,padx=10,pady=10)


#Creating submit and clear buttons
submit_btn = Button(Login_frame, text="Submit",font=("Candara",12,"bold"),fg="#00008B",bg="White", command=insert)
reset_button = Button(Login_frame, text="Clear",font=("Candara",12,"bold"),fg="#00008B",bg="White", command=clear_input)

#Setting up grids for submit and reset buttons
submit_btn.grid(row=4, column=1,padx=10,pady=10,ipadx=70)
reset_button.grid(row=4, column=0,padx=10,pady=10,ipadx=20)


window.mainloop()