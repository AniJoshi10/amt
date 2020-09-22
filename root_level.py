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
import bcrypt
# creating instance of TK
root = Tk()

# stting title for the window
root.title("Admin Verification")
#root.configure(bg='gray')
admin_id=""

#elements for the dropdownbox
clicked=StringVar()
clicked.set("Register")

options={
    "Register",
    "Update"
}


def clear_input():
    name_box.delete(0, END)
    roll_no_box.delete(0, END)
    return

def verify():
    id1=name_box.get()
    pass1=roll_no_box.get()
    option=clicked.get()
    mydb = mysql.connector.connect(host="", user="", passwd="", database="")
    mycursor = mydb.cursor()
    sql = "SELECT pass FROM passwords WHERE id=%(id)s;"

    mydata = {
        'id': admin_id
    }
    row_count = mycursor.execute(sql, mydata)
    var1 = mycursor.fetchall()
    for recod in var1:
        print(recod[0])
        booleanval = bcrypt.hashpw(pass1.encode(), recod[0].encode())
        if booleanval == recod[0].encode():
            if option == "Register":
                root.destroy()
                os.system("faculty_registration.py")
            else:
                root.destroy()
                # call for update window
                os.system("update_window.py")
        else:
            messagebox.showerror("Error", "Admin privelege denied.")
            root.destroy()
            os.system("Teachers_portal.py")


    return


#Creating a label for Id
name_label = Label(root, text="Admin ID",font=("Candara",12,"bold"),fg="#00008B")
name_label.grid(row=1,column=0,padx=10,pady=10)

#creating a label for Password
roll_no_label=Label(root,text="Password",font=("Candara",12,"bold"),fg="#00008B")
roll_no_label.grid(row=2,column=0,padx=10,pady=10)

#Entry Field for id
name_box=Entry(root,width=20,font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
name_box.grid(row=1,column=1,padx=10,pady=10)

#creating a Enrty field for Password
roll_no_box=Entry(root,width=20,show='*',font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
roll_no_box.grid(row=2,column=1,padx=10,pady=10)

#Creating entry field for subject
#sub_entry=Entry(manual_frame,width=20)
#sub_entry.grid(row=3,column=1,padx=10,pady=10)
#Creating submit and clear buttons
sub_label=Label(root, text="Options",font=("Candara",12,"bold"),fg="#00008B")
sub_label.grid(row=3,column=0,padx=10,pady=10)

#Creating entry field for subject
#sub_entry=Entry(manual_frame,width=20)
#sub_entry.grid(row=3,column=1,padx=10,pady=10)

popupMenu = OptionMenu(root, clicked, *options)
popupMenu.grid(row=3,column=1,padx=10,pady=10,sticky=N+E+W+S)


submit_btn = Button(root, text="Submit",font=("Candara",12,"bold"),fg="#00008B", command=verify)
reset_button = Button(root, text="Clear",font=("Candara",12,"bold"),fg="#00008B", command=clear_input)

#Setting up grids for submit and reset buttons
submit_btn.grid(row=4, column=1,padx=10,pady=10,ipadx=70)
reset_button.grid(row=4, column=0,padx=10,pady=10,ipadx=20)


root.mainloop()
