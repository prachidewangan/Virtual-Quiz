# Code for Virtual Quiz interface

import cv2
import csv
from cvzone.HandTrackingModule import HandDetector
import cvzone
import time
capture = cv2.VideoCapture(0)
capture.set(3,1280)
capture.set(4,720)

#hand detector
detector = HandDetector(detectionCon = 0.8, maxHands = 2)

# for video capture
while True:
    sucess,image = capture.read()
    hands,image = detector.findHands(image)
    #print(sucess)
    cv2.imshow('frame',image)
    cv2.waitKey(1)
