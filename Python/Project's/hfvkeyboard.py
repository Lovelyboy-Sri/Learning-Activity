import cv2
import mediapipe as mp
import pyautogui as pg
import numpy as np
import time
import autopy as ap
import HandTrackingModule as htm

cam = cv2.VideoCapture(0)
hg = mp.solutions.hand


while True:
    _, frame = cam.read()


    cv2.imshow("Virtual keyboard using hand gesture ",frame)
    cv2.waitKey(1)