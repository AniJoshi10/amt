#If trainer file already exits in teh given directory the it will be overwrriten.
import cv2
import numpy as np
from PIL import Image
import os
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
from tkinter import messagebox
root = Tk()

# stting title for the window
root.title("Face Traning")


#elements for the dropdownbox
clicked=StringVar()
clicked.set("Final")

options={
    "Final",
    "Third",
    "Second"
}

# Path for face image database
path = 'dataset_final'
path2= 'dataset_second'
path3= 'dataset_third'
recognizer = cv2.face.LBPHFaceRecognizer_create()
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");


def verify():
    year=clicked.get()
    if year=="Final":
        def getImagesAndLabels(path):
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
            faceSamples = []
            ids = []
            for imagePath in imagePaths:
                PIL_img = Image.open(imagePath).convert('L')
                img_numpy = np.array(PIL_img, 'uint8')
                id = int(os.path.split(imagePath)[-1].split(".")[1])
                faces = face_detector.detectMultiScale(img_numpy)

                for (x, y, w, h) in faces:
                    faceSamples.append(img_numpy[y:y + h, x:x + w])
                    ids.append(id)

            return faceSamples, ids

        faces, ids = getImagesAndLabels(path)
        recognizer.train(faces, np.array(ids))

        # Save the model into trainer/trainer.yml
        recognizer.write('trainer_final/trainer.yml')
        # Print the numer of faces trained and end program
        print("\n [INFO] {0} faces trained into trainer.".format(len(np.unique(ids))))
        messagebox.showinfo("Success", "Data is trained!.")
    elif year=="Third":
        def getImagesAndLabels(path):
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
            faceSamples = []
            ids = []
            for imagePath in imagePaths:
                PIL_img = Image.open(imagePath).convert('L')
                img_numpy = np.array(PIL_img, 'uint8')
                id = int(os.path.split(imagePath)[-1].split(".")[1])
                faces = face_detector.detectMultiScale(img_numpy)

                for (x, y, w, h) in faces:
                    faceSamples.append(img_numpy[y:y + h, x:x + w])
                    ids.append(id)

            return faceSamples, ids

        faces, ids = getImagesAndLabels(path3)
        recognizer.train(faces, np.array(ids))

        recognizer.write('trainer_third/trainer.yml')

    else:
        def getImagesAndLabels(path):
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
            faceSamples = []
            ids = []
            for imagePath in imagePaths:
                PIL_img = Image.open(imagePath).convert('L')
                img_numpy = np.array(PIL_img, 'uint8')
                id = int(os.path.split(imagePath)[-1].split(".")[1])
                faces = face_detector.detectMultiScale(img_numpy)

                for (x, y, w, h) in faces:
                    faceSamples.append(img_numpy[y:y + h, x:x + w])
                    ids.append(id)

            return faceSamples, ids

        faces, ids = getImagesAndLabels(path2)
        recognizer.train(faces, np.array(ids))

        #We got our trainer
        recognizer.write('trainer_second/trainer.yml')


#Label for Subject
text=Label(root,text="Please select respective yrar to train dataset.",font=("Candara",12,"bold"),fg="#00008B")
text.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

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