# Code for Virtual Quiz interface

import cv2
import csv
from cvzone.HandTrackingModule import HandDetector
import cvzone
import time
capture = cv2.VideoCapture(0)
capture.set(3,1280)
capture.set(4,720)


while True:
    sucess,image = capture.read()
    cv2.imshow('frame',image)
    cv2.waitKey(1)
