import numpy
import cv2
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.eval('tk::PlaceWindow . center')

ROOT.withdraw()
ROOT.wm_attributes("-topmost", True)
USER_INP = simpledialog.askstring(title="Name",
                                  prompt="Masukkan Nama?")

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
while True:
    ret, im = cap.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=2,
        minSize=(20, 20),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Camera', im)
    if cv2.waitKey(1) & 0xFF == ord('q'): # press 'p to quit'
        break

cap.release()
cv2.destroyAllWindows()