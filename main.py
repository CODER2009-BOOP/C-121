import cv2
import time
import numpy as np

#To save the output in a file output.avi
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc , 20.0 , (640,480))

#starting the webcam
cap = cv2.VideoCapture(0)

#Allowing the webcam to start by making the code sleep for 2 seconds
time.sleep(2)
bg = 0

#Capturing background for 60 frames
for i in range(60):
    ret,bg = cap.read()

#Flipping the background
bg = np.flip(bg, axis = 1)

#Reading the capured frame until the camera is open
while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    #Flipping the image for consistency
    
    img = np.flip(img, axis = 1) 

    #Converting the color from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)