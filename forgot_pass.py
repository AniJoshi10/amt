import cv2
import mysql.connector
import csv
from datetime import datetime
import shutil
import time
from tkinter import *
import os
import mysql.connector;
from PIL import ImageTk,Image
from tkinter import messagebox
import random
import string
import bcrypt
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

root = Tk()

# generating title for the window
root.title("Forgot password window")

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def verify():
    fac_id=Unique_Identification_box.get()
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="AdityaRP23", database="practice")
    mycursor = mydb.cursor()
    sql = "SELECT email FROM passwords WHERE id=%(id)s;"
    mydata = {
        'id': fac_id
    }
    row_count = mycursor.execute(sql, mydata)
    var1 = mycursor.fetchall()
    for recod in var1:
        random_str=get_random_alphanumeric_string(5)
        passwd = random_str.encode()
        # Random initial salt to be added to passwd rounds=15
        salt = bcrypt.gensalt()

        # Hashed value to be stored in Database
        hashed = bcrypt.hashpw(passwd, salt)
        print(hashed)
        sql = "UPDATE passwords SET pass=%(hash)s WHERE id=%(rollno)s;"
        mydata = {
            'hash':hashed,
            'rollno': fac_id
        }
        mycursor.execute(sql, mydata)
        mydb.commit()

        port = 587
        smtp_server = "smtp.gmail.com"
        sender_email = "rppundkar@gmail.com"
        receiver_email = recod[0]
        password = input("Type your password and press enter:")
        message = """\
        Joshi Buwa

        Hi. Your temporory password is: """
        msg1=message+random_str
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg1)
        messagebox.showinfo("Success!","Your new password is successfully sent to your email. Thank you")
    return

#Setting up Label;
text=Label(root,text="Please enter your faculty id to receive temporory password.",font=("Candara",12,"bold"),fg="#00008B")
text.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
name_label = Label(root, text="Faculty id.",font=("Candara",12,"bold"),fg="#00008B")
name_label.grid(row=1,column=0,padx=10,pady=10)
#creating a Enrty field for Unique Identification Number
Unique_Identification_box=Entry(root,width=20,font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
Unique_Identification_box.grid(row=1,column=1,padx=10,pady=10)

#Setting up button for submit
submit_btn = Button(root, text="Submit",font=("Candara",12,"bold"),fg="#00008B", command=verify)
submit_btn.grid(row=3, column=1,padx=10,pady=10,ipadx=20)

root.mainloop()