# -*- coding: utf-8 -*-
from tkinter import *
import os
import turtle
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
import mysql.connector;
import bcrypt


#Creating the window for Teacher
window = Tk()
window.title("Faculty Login")
window.configure(bg='skyblue')
#window.configure(background='black')

window.resizable(False,False)

#Background Image
back_image=ImageTk.PhotoImage(Image.open("pngtree-blue-smart-light-tech-background-backgroundlight-effect-backgroundelectronic-image_81225.jpg"))
background_label=Label(window,image=back_image)
background_label.grid(row=0,column=0,rowspan=4,columnspan=2)


#SGGS Image logo insertion
sggs_image=ImageTk.PhotoImage(Image.open("ci51-01.png"))
image_label=Label(window,image=sggs_image,borderwidth=2, relief="sunken")
image_label.grid(row=0,column=0,columnspan=2)

#Creating a frame for login credentils
Login_frame=Frame(window,bg="white",borderwidth=2, relief="sunken")
Login_frame.place(x=340,y=250,height=200)

#Defining the function to Clear the inpu fields
def clear_input():
    id_box.delete(0, END)
    passwd_box.delete(0, END)

#Defing function for verifyng details
def verify():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="AdityaRP23", database="practice")
    mycursor = mydb.cursor()
    username=id_box.get()
    password=passwd_box.get()
    sql = "SELECT pass FROM passwords WHERE id=%(id)s;"

    mydata = {
        'id': username
    }
    row_count=mycursor.execute(sql, mydata)
    var1 = mycursor.fetchall()
    for recod in var1:
        print(recod[0])
        booleanval=bcrypt.hashpw(password.encode(),recod[0].encode())
        if booleanval == recod[0].encode():
                window.destroy()
                os.system("temp.py")
        else:
                messagebox.showerror("Warning", "Passwword dosen't match")
                window.destroy()

def student():
    os.system("face_recognization.py")


def faculty():
    window.destroy()
    os.system("root_level")

    os.system("Teachers_portal")
    return

def forgot():
    window.destroy()
    os.system("forgot_pass.py")
    os.system("Teachers_portal.py")
#label1=Label(window,text="Welcome to Faculty Portal")
#label1.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
#Creating a label for Id

text=Label(window,text="FACULTY LOGIN",font=("Candara",12,"bold"),fg="#111111",bg="white",borderwidth=2,relief="sunken").place(x=320,y=235)

id_label = Label(Login_frame, text="Faculty Id",font=("Candara",12,"bold"),fg="#00008B",bg="White")
id_label.grid(row=1,column=0,padx=10,pady=10)

#creating a label for Password
passwd_label=Label(Login_frame,text="Password",font=("Candara",12,"bold"),fg="#00008B",bg="White")
passwd_label.grid(row=2,column=0,padx=10,pady=10)

#Entry Field for id
id_box=Entry(Login_frame,width=20,font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
id_box.grid(row=1,column=1,padx=10,pady=10)

#creating a Enrty field for Password
passwd_box=Entry(Login_frame,width=20,show='*',font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
passwd_box.grid(row=2,column=1,padx=10,pady=10)


#Creating submit and clear buttons
submit_btn = Button(Login_frame, text="Submit",font=("Candara",12,"bold"),bg="#4169E1",fg="White", command=verify)
reset_button = Button(Login_frame, text="Clear",font=("Candara",12,"bold"),bg="#4169E1",fg="White", command=clear_input)

#Setting up grids for submit and reset buttons
submit_btn.grid(row=3, column=1,padx=10,pady=10,ipadx=70)
reset_button.grid(row=3, column=0,padx=10,pady=10,ipadx=20)
forget_but=Button(Login_frame,text="Forgot password?",bg="white",fg="#00008B",bd=0,font=("Candara",12,"bold"),command=forgot)
forget_but.grid(row=4, column=1,padx=10,pady=10,ipadx=20)

stu_btn=Button(window, text="I am Student",font=("Candara",12,"bold"),bg="skyblue",fg="#111111",bd=2,relief="sunken",command=student)
stu_btn.place(x=570,y=440)

faculty_reg=Button(window, text="Update / Register",font=("Candara",12,"bold"),bg="skyblue",fg="#111111",bd=2,relief="sunken",command=faculty)
faculty_reg.place(x=350,y=440)

#running the Window to screen
window.mainloop()