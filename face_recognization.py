import cv2
import os
import mysql.connector
import csv
import shutil
import time
from tkinter import *
from datetime import datetime;
from PIL import ImageTk,Image
from tkinter import messagebox
import numpy as np
import mysql.connector

root = Tk()

# stting title for the window
root.title("Face Recognisation")

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
        mydb = mysql.connector.connect(host="", user="", passwd="", database="")
        mycursor = mydb.cursor()
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.read('trainer_final/trainer.yml')
        cascade_file_Path = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascade_file_Path);
        font = cv2.FONT_HERSHEY_SIMPLEX

        # iniciate roll no. within year
        unique_identification = 0
        #list of all students of particular year
        names = ['Zero']
        mycursor.execute("Select name from Attendance")
        myresult = mycursor.fetchall()
        #reading names from respective database
        for x in myresult:
            print(x)
            names.append(x[0])

        cam = cv2.VideoCapture(0)

        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        while True:

            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.3,  # image scaling is 130%
                minNeighbors=5,
            )

            for (x, y, w, h) in faces:

                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
                unique_identification, confidence = face_recognizer.predict(gray[y:y + h, x:x + w])

                if (confidence < 70):
                    unique_identification = names[unique_identification]
                    confidence = "  {0}%".format(round(100 * (1 - (confidence / 300))))
                    sql = "Update Attendance SET stats='Present' where name='" + unique_identification + "'"
                    mycursor.execute(sql)
                    mydb.commit()
                else:
                    unique_identification = "Cannot detect face"
                    confidence = "  {0}%".format(round(100 * (1 - (confidence / 300))))

                cv2.putText(img, str(unique_identification), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
                cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

            cv2.imshow('Scanning', img)
            k = cv2.waitKey(10) & 0xff
            if k == 27:
                break

        cam.release()
        cv2.destroyAllWindows()
    elif year=="Third":
        mydb = mysql.connector.connect(host="", user="", passwd="", database="")
        mycursor = mydb.cursor()
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.read('trainer_third/trainer.yml')
        cascade_file_Path = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascade_file_Path);
        font = cv2.FONT_HERSHEY_SIMPLEX

        # iniciate unique_identification counter counter
        unique_identification = 0

        names = ['None']

        mycursor.execute("Select name from Attendance_third")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
            names.append(x[0])

        cam = cv2.VideoCapture(0)

        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        while True:

            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.3,  # image scaling is 130%
                minNeighbors=5,
            )

            for (x, y, w, h) in faces:

                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
                unique_identification, confidence = face_recognizer.predict(gray[y:y + h, x:x + w])

                if (confidence < 70):
                    unique_identification = names[unique_identification]
                    confidence = "  {0}%".format(round(100 * (1 - (confidence / 300))))
                    sql = "Update Attendance_third SET stats='Present' where name='" + unique_identification + "'"
                    mycursor.execute(sql)
                    mydb.commit()
                else:
                    unique_identification = "Cannot detect face"
                    confidence = "  {0}%".format(round(100 * (1 - (confidence / 300))))

                cv2.putText(img, str(unique_identification), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
                cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

            cv2.imshow('Scanning', img)
            k = cv2.waitKey(10) & 0xff
            if k == 27:
                break

        cam.release()
        cv2.destroyAllWindows()
    else:
        mydb = mysql.connector.connect(host="", user="", passwd="", database="")
        mycursor = mydb.cursor()
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.read('trainer_second/trainer.yml')
        cascade_file_Path = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascade_file_Path);
        font = cv2.FONT_HERSHEY_SIMPLEX

        # iniciate roll no within year
        unique_identification = 0

        names = ['None']

        mycursor.execute("Select name from Attendance_second")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
            names.append(x[0])

        cam = cv2.VideoCapture(0)

        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        while True:

            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.3,  # image scaling is 130%
                minNeighbors=5,
            )

            for (x, y, w, h) in faces:

                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
                unique_identification, confidence = face_recognizer.predict(gray[y:y + h, x:x + w])

                if (confidence < 70):
                    unique_identification = names[unique_identification]
                    confidence = "  {0}%".format(round(100*(1-(confidence/300))))
                    sql = "Update Attendance_second SET stats='Present' where name='" + unique_identification + "'"
                    mycursor.execute(sql)
                    mydb.commit()
                else:
                    unique_identification = "Cannot detect face"
                    confidence = "  {0}%".format(round(100 * (1 - (confidence / 300))))

                cv2.putText(img, str(unique_identification), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
                cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

            cv2.imshow('Scanning', img)
            k = cv2.waitKey(10) & 0xff
            if k == 27:
                break
        cam.release()
        cv2.destroyAllWindows()

text=Label(root,text="Please enter your respective class",font=("Candara",12,"bold"),fg="#00008B")
text.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
#Label for Subject
sub_label=Label(root, text="Year",font=("Candara",12,"bold"),fg="#00008B")
sub_label.grid(row=1,column=0,padx=10,pady=10)

#Creating entry field for subject
#sub_entry=Entry(manual_frame,width=20)
#sub_entry.grid(row=3,column=1,padx=10,pady=10)

popupMenu = OptionMenu(root, clicked, *options)
popupMenu.grid(row=1,column=1,padx=10,pady=10,sticky=N+E+W+S)

#Setting up button for submit
submit_btn = Button(root, text="Submit",font=("Candara",12,"bold"),fg="#00008B", command=verify)
submit_btn.grid(row=2, column=1,padx=10,pady=10,ipadx=70)


root.mainloop()
