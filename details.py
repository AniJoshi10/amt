# -*- coding: utf-8 -*-

from tkinter import *
import os
from datetime import datetime;
import mysql.connector;
from datetime import date
from tkinter import messagebox

#Creating our Window
root=Tk()

#Creating connection with the MYSQL database
mydb = mysql.connector.connect(host="localhost",user="root",passwd="AdityaRP23",database="practice")
cursor = mydb.cursor()

name=input("enter name")
rid=int(input("enter rolll no."))
clss=input("enter class")
stats="Absent"

#Taking date from device
cur_date = date.today()



sql="INSERT INTO Attendance(name,roll_no,class,stats,date) VALUES(%s,%s,%s,%s,%s)"

args = (name,rid,clss,stats,cur_date)
cursor.execute(sql,(name,rid,clss,stats,cur_date))
mydb.commit()
messagebox.showinfo("Success","Student is successfull enroled!")
s = "update Attendance SET date=current_date();"
cursor.execute(s);
mydb.commit()
print(cursor.rowcount, "record inserted.")
print("Database updated")

