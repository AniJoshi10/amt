from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
import csv


mydb=mysql.connector.connect(host="",user="",passwd="",database="")

mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE Attendance1(name varchar(255),roll_no INT(10),class varchar(255),stats varchar(255),date varchar(255))")

mydb.commit()
