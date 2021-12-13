import cv2
import os
import tkinter as tk
from tkinter import simpledialog

cam = cv2.VideoCapture(0)
#cam = cv2.VideoCapture(0)
#cam.set(3, 640) # set video width
#cam.set(4, 480) # set video height

haar_file = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
datasets ="dataset"

ROOT = tk.Tk()
ROOT.withdraw()
nama = simpledialog.askstring(title="Name",prompt="Masukkan Nama?")

path = os.path.join(datasets, nama)
if not os.path.isdir(path):
    os.mkdir(path)

count = 1
while count <= 200: 
    (_, im) = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = haar_file.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face = gray[y:y + h, x:x + w]
        #face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('%s/%s.jpg' % (path,count), face)
        print("Saving Image : ", str(count)+'.jpg')
    count += 1

    cv2.imshow('Dataset', im)
    k = cv2.waitKey(10)
    if k == 27 & 0xFF == ord('q'):
        break
    
print("Saving Complete")
cam.release()
cv2.destroyAllWindows()  