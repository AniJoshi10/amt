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
root.title("Face Registration")


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
        unique_registration = Unique_Identification_box.get()
        vid_cam = cv2.VideoCapture(0)
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        count = 0
        # Start looping
        while (True):
            _, image_frame = vid_cam.read()

            gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:

                cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
                count += 1
                cv2.imwrite("dataset_final/Final." + str(unique_registration) + '.' + str(count) + ".jpg",
                            gray[y:y + h, x:x + w])
                cv2.imshow('Scanning', image_frame)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif count >= 200:
                messagebox.showinfo("Success", "Your face data is successfully captured.")
                break

        vid_cam.release()
        cv2.destroyAllWindows()
        return
    elif year=="Third":
        unique_registration = Unique_Identification_box.get()
        vid_cam = cv2.VideoCapture(0)
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        count = 0
        # Start looping
        while (True):

            _, image_frame = vid_cam.read()
            gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

                count += 1
                cv2.imwrite("dataset_third/Third." + str(unique_registration) + '.' + str(count) + ".jpg",
                            gray[y:y + h, x:x + w])
                cv2.imshow('Scanning', image_frame)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif count >= 200:
                messagebox.showinfo("Success", "Your face data is successfully captured.")
                break

        vid_cam.release()
        cv2.destroyAllWindows()
        return
    else:
        unique_registration = Unique_Identification_box.get()
        vid_cam = cv2.VideoCapture(0)
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        count = 0
        # Start looping
        while (True):
            _, image_frame = vid_cam.read()
            gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.1, 10)
            for (x, y, w, h) in faces:
                cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

                count += 1
                cv2.imwrite("dataset_second/Second." + str(unique_registration) + '.' + str(count) + ".jpg",
                            gray[y:y + h, x:x + w])
                cv2.imshow('Scanning', image_frame)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif count >= 200:
                messagebox.showinfo("Success", "Your face data is successfully captured.")
                break

        vid_cam.release()
        cv2.destroyAllWindows()
        return

#Setting up Label;
text=Label(root,text="Please enter roll no. of respective class",font=("Candara",12,"bold"),fg="#00008B")
text.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
name_label = Label(root, text="Roll. no",font=("Candara",12,"bold"),fg="#00008B")
name_label.grid(row=1,column=0,padx=10,pady=10)
#creating a Enrty field for Unique Identification Number
Unique_Identification_box=Entry(root,width=20,font=("Courier new",12,"bold"),fg="#000000",borderwidth=2,relief="sunken")
Unique_Identification_box.grid(row=1,column=1,padx=10,pady=10)

#Label for Subject
sub_label=Label(root, text="Year",font=("Candara",12,"bold"),fg="#00008B")
sub_label.grid(row=2,column=0,padx=10,pady=10)

#Creating entry field for subject
#sub_entry=Entry(manual_frame,width=20)
#sub_entry.grid(row=3,column=1,padx=10,pady=10)

popupMenu = OptionMenu(root, clicked, *options)
popupMenu.grid(row=2,column=1,padx=10,pady=10,sticky=N+E+W+S)

#Setting up button for submit
submit_btn = Button(root, text="Submit",font=("Candara",12,"bold"),fg="#00008B", command=verify)
submit_btn.grid(row=3, column=1,padx=10,pady=10,ipadx=20)

root.mainloop()