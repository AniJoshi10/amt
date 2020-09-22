import mysql.connector
import os
import csv
import shutil
import time
from tkinter import *
import bcrypt
from datetime import datetime;
import mysql.connector;
from PIL import ImageTk,Image
from tkinter import messagebox
# creating instance of TK
root = Tk()

# stting title for the window
root.title("Sheet Generator")
#root.configure(bg='gray')
p1 = datetime.date(datetime.now())
p = str(datetime.date(datetime.now()))
time = str(time.localtime())


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
    mydb = mysql.connector.connect(host="", user="", passwd="", database="")
    mycursor = mydb.cursor()
    username = name_box.get()
    password = roll_no_box.get()
    sql = "SELECT pass FROM passwords WHERE id=%(id)s;"
    year=clicked.get()
    sub=subject_box.get()
    mydata = {
        'id': username
    }
    row_count = mycursor.execute(sql, mydata)
    var1 = mycursor.fetchall()
    for recod in var1:
        print(recod[0])
        booleanval = bcrypt.hashpw(password.encode(), recod[0].encode())
        if booleanval == recod[0].encode():
            if year == "Final":
                mydb1 = mysql.connector.connect(host="", user="", passwd="", database="")
                cursor1 = mydb1.cursor()


                mydb = mysql.connector.connect(host="", user="", passwd="",
                                               database="")
                mycursor = mydb.cursor()
                sql = "SELECT * FROM Attendance"
                mycursor.execute(sql, mydata)
                rows = mycursor.fetchall()
                for tuple in rows:
                    name=tuple[0]
                    roll_no=tuple[1]
                    year=tuple[2]
                    ststs=tuple[3]
                    cur_date=tuple[4]
                    subject=sub
                    now=datetime.now()
                    tm=now.strftime("%H:%M:%S")

                    sql1 = "INSERT INTO Central_database(name,roll_no,class,status,date,sub,time) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                    args1 = (name, roll_no, year, ststs, cur_date,subject,now)
                    cursor1.execute(sql1, (name, roll_no, year, ststs, cur_date,subject,now))
                    mydb1.commit()


                    print(tuple)
                with open('attendance_' + p + time + '.csv', 'w') as f:
                    a = csv.writer(f, delimiter=',')
                    a.writerows(["name", "roll_no", "class", "status", "date"])  ## etc
                    a.writerows(rows)  ## closing paren added

                original = "C:\\Users\\Aditya\\PycharmProjects\\B_Tech_Project\\" + 'attendance_' + p + time + '.csv'
                destination = "C:\\Users\\Aditya\\PycharmProjects\\B_Tech_Project\\sheets\\" + 'attendance_' + p + time + '.csv'
                shutil.move(original, destination)

                messagebox.showinfo("Success", "Successfully exported to csv file.")
            elif year == "Third":
                mydb1 = mysql.connector.connect(host="", user="", passwd="", database="")
                cursor1 = mydb1.cursor()

                mydb = mysql.connector.connect(host="", user="", passwd="",
                                               database="")
                mycursor = mydb.cursor()
                sql = "SELECT * FROM Attendance_third"
                mycursor.execute(sql, mydata)
                rows = mycursor.fetchall()
                for tuple in rows:
                    name = tuple[0]
                    roll_no = tuple[1]
                    year = tuple[2]
                    ststs = tuple[3]
                    cur_date = tuple[4]
                    subject = sub
                    now = datetime.now()
                    tm = now.strftime("%H:%M:%S")

                    sql1 = "INSERT INTO Central_database(name,roll_no,class,status,date,sub,time) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                    args1 = (name, roll_no, year, ststs, cur_date, subject, now)
                    cursor1.execute(sql1, (name, roll_no, year, ststs, cur_date, subject, now))
                    mydb1.commit()

                    print(tuple)
                with open('attendance_' + p + time + '.csv', 'w') as f:
                    a = csv.writer(f, delimiter=',')
                    a.writerows(["name", "roll_no", "class", "status", "date"])  ## etc
                    a.writerows(rows)  ## closing paren added

                original = "C:\\Users\\Aditya\\PycharmProjects\\B_Tech_Project\\" + 'attendance_' + p + time + '.csv'
                destination = "C:\\Users\\Aditya\\PycharmProjects\\B_Tech_Project\\sheets_third\\" + 'attendance_' + p + time + '.csv'
                shutil.move(original, destination)

                messagebox.showinfo("Success", "Successfully exported to csv file.")
            else:
                mydb1 = mysql.connector.connect(host="", user="", passwd="", database="")
                cursor1 = mydb1.cursor()

                mydb = mysql.connector.connect(host="", user="", passwd="",
                                               database="")
                mycursor = mydb.cursor()
                sql = "SELECT * FROM Attendance_second"
                mycursor.execute(sql, mydata)
                rows = mycursor.fetchall()
                for tuple in rows:
                    name = tuple[0]
                    roll_no = tuple[1]
                    year = tuple[2]
                    ststs = tuple[3]
                    cur_date = tuple[4]
                    subject = sub
                    now = datetime.now()
                    tm = now.strftime("%H:%M:%S")

                    sql1 = "INSERT INTO Central_database(name,roll_no,class,status,date,sub,time) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                    args1 = (name, roll_no, year, ststs, cur_date, subject, now)
                    cursor1.execute(sql1, (name, roll_no, year, ststs, cur_date, subject, now))
                    mydb1.commit()

                    print(tuple)
                with open('attendance_' + p + time + '.csv', 'w') as f:
                    a = csv.writer(f, delimiter=',')
                    a.writerows(["name", "roll_no", "class", "status", "date"])  ## etc
                    a.writerows(rows)  ## closing paren added

                original = "C:\\Users\\Aditya\\PycharmProjects\\B_Tech_Project\\" + 'attendance_' + p + time + '.csv'
                destination = "C:\\Users\\Aditya\\PycharmProjects\\B_Tech_Project\\sheets_second\\" + 'attendance_' + p + time + '.csv'
                shutil.move(original, destination)

                messagebox.showinfo("Success", "Successfully exported to csv file.")
        else:
            messagebox.showerror("Warning", "Passwword dosen't match")
            root.destroy()

    return

#Creating a label for Id
name_label = Label(root, text="Faculty ID",font=("Candara",12,"bold"),fg="#00008B")
name_label.grid(row=1,column=0,padx=10,pady=10)

#creating a label for Password
roll_no_label=Label(root,text="Passward",font=("Candara",12,"bold"),fg="#00008B")
roll_no_label.grid(row=2,column=0,padx=10,pady=10)

#Entry Field for id
name_box=Entry(root,width=20,font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
name_box.grid(row=1,column=1,padx=10,pady=10)

#creating a Enrty field for Password
roll_no_box=Entry(root,width=20,show='*',font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
roll_no_box.grid(row=2,column=1,padx=10,pady=10)

sub_label=Label(root, text="Year",font=("Candara",12,"bold"),fg="#00008B")
sub_label.grid(row=3,column=0,padx=10,pady=10)

#Creating entry field for subject
#sub_entry=Entry(manual_frame,width=20)
#sub_entry.grid(row=3,column=1,padx=10,pady=10)

popupMenu = OptionMenu(root, clicked, *options)
popupMenu.grid(row=3,column=1,padx=10,pady=10,sticky=N+E+W+S)

#Creating submit and clear buttons
submit_btn = Button(root, text="Submit",font=("Candara",12,"bold"),fg="#00008B", command=verify)
reset_button = Button(root, text="Clear",font=("Candara",12,"bold"),fg="#00008B", command=clear_input)

#Setting up grids for submit and reset buttons
submit_btn.grid(row=5, column=1,padx=10,pady=10,ipadx=70)
reset_button.grid(row=5, column=0,padx=10,pady=10,ipadx=20)

subject_label=Label(root, text="Subject",font=("Candara",12,"bold"),fg="#00008B")
subject_label.grid(row=4,column=0,padx=10,pady=10)
subject_box=Entry(root,width=20,font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
subject_box.grid(row=4,column=1,padx=10,pady=10)

root.mainloop()
