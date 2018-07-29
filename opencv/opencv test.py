"""import cv2
import numpy as np
#this edit was made in Git
img = cv2.imread('fantasy-wallpaper-22.jpg')
for i in range (100):
    for g in range (100):
        img[i ,g] = [255,255,255]
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""import numpy as np
import cv2
import matplotlib as plt
#initialize variable cap
cap = cv2.VideoCapture(0)
cv2.namedWindow('boyo', cv2.WINDOW_NORMAL)
shouldRun = True

while(shouldRun) :
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(frame, 100, 200)
    plt.subplot(121),plt.imshow(frame,cmap = 'gray')
    plt.title('boyo')
    cv2.imshow('boyo', frame)
    if(cv2.waitKey(20) != -1):
        shouldRun = False:
"""

import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cv2.namedWindow('boyo', cv2.WINDOW_NORMAL)

while (True):
    ret, frame = cap.read()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.imshow('boyo',frame)
    if(cv2.waitKey(20) != -1):
        break

