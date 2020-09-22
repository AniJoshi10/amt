from tkinter import *
import os
import turtle
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
import mysql.connector;
from datetime import date
import bcrypt

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
    id_box.delete(0,END)
    old_pass_box.delete(0, END)
    new_pass_box.delete(0, END)
    conf_pass_box.delete(0,END)


def insert():
    id1=id_box.get()
    old=old_pass_box.get()
    new=new_pass_box.get()
    confirm=conf_pass_box.get()

    mydb = mysql.connector.connect(host="localhost", user="root", passwd="AdityaRP23", database="practice")
    mycursor = mydb.cursor()
    sql = "SELECT pass FROM passwords WHERE id=%(id)s;"

    mydata = {
        'id': id1
    }
    row_count = mycursor.execute(sql, mydata)
    var1 = mycursor.fetchall()
    for recod in var1:
        print(recod[0])
        booleanval = bcrypt.hashpw(old.encode(), recod[0].encode())
        if booleanval == recod[0].encode():
            if new==confirm:
                passwd = new.encode()
                # Random initial salt to be added to passwd rounds=15
                salt = bcrypt.gensalt()

                # Hashed value to be stored in Database
                hashed = bcrypt.hashpw(passwd, salt)
                print(hashed)
                sql = "UPDATE passwords SET pass=%(hash)s WHERE id=%(rollno)s;"
                mydata = {
                    'hash': hashed,
                    'rollno': id1
                }
                mycursor.execute(sql, mydata)
                mydb.commit()
                messagebox.showinfo("Success","Password is successfully updated!")
            else:
                messagebox.showerror("Warning","Your new and confirm password are not matching")
        else:
            messagebox.showerror("Warning", "Passwword dosen't match")
            window.destroy()




text=Label(window,text="UPDATE",font=("Candara",12,"bold"),fg="#111111",bg="white",borderwidth=2,relief="sunken").place(x=220,y=210)
#Fields for registraing student
#Creating a label for id
id_label = Label(Login_frame, text="ID.",font=("Candara",12,"bold"),fg="#00008B",bg="White")
id_label.grid(row=1,column=0,padx=10,pady=10)

id_box=Entry(Login_frame,width=20,font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
id_box.grid(row=1,column=1,padx=10,pady=10)


name_label = Label(Login_frame, text="Old password.",font=("Candara",12,"bold"),fg="#00008B",bg="White")
name_label.grid(row=2,column=0,padx=10,pady=10)

#creating a label for roll_no
roll_no_label=Label(Login_frame,text="New password.",font=("Candara",12,"bold"),fg="#00008B",bg="White")
roll_no_label.grid(row=3,column=0,padx=10,pady=10)

#Entry Field for name
old_pass_box=Entry(Login_frame,width=20,font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
old_pass_box.grid(row=2,column=1,padx=10,pady=10)

#creating a Enrty field for roll_no
new_pass_box=Entry(Login_frame,width=20,font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
new_pass_box.grid(row=3,column=1,padx=10,pady=10)

#Label for Subject
conf_pass_label=Label(Login_frame, text="Confirm password.",font=("Candara",12,"bold"),fg="#00008B",bg="White")
conf_pass_label.grid(row=4,column=0,padx=10,pady=10)

#Creating entry field for subject
#sub_entry=Entry(manual_frame,width=20)
#sub_entry.grid(row=3,column=1,padx=10,pady=10)

conf_pass_box=Entry(Login_frame,width=20,font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
conf_pass_box.grid(row=4,column=1,padx=10,pady=10)


#Creating submit and clear buttons
submit_btn = Button(Login_frame, text="Submit",font=("Candara",12,"bold"),fg="#00008B",bg="White", command=insert)
reset_button = Button(Login_frame, text="Clear",font=("Candara",12,"bold"),fg="#00008B",bg="White", command=clear_input)

#Setting up grids for submit and reset buttons
submit_btn.grid(row=5, column=1,padx=10,pady=10,ipadx=70)
reset_button.grid(row=5, column=0,padx=10,pady=10,ipadx=20)


window.mainloop()