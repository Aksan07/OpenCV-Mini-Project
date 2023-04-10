from HandTrackingModule import HandDetector
import cv2
import numpy as np
import pyautogui as pe
import time
def start_presentation():
    pe.keyDown('f5')
    pe.keyUp('f5')
def move_left():
    pe.press('left')
    time.sleep(1)
def move_right():
    pe.press('right')
    time.sleep(1)
def close_presentation():
    pe.press('esc') 
 
# Parameters
width, height = 1280, 720
gestureThreshold = 300

 
# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)
 
# Hand Detector
detectorHand = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    # Get image frame
    success, img = cap.read()
    img = cv2.flip(img, 1)
    # Find the hand and its landmarks
    
    hands, img = detectorHand.findHands(img)  # with draw
    # Draw Gesture Threshold line
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 10)
    cv2.imshow("Image",img)

    if hands:  # If hand is detected
 
        hand = hands[0]
        cx, cy = hand["center"]
        lmList = hand["lmList"]  # List of 21 Landmark points
        fingers = detectorHand.fingersUp(hand)  # List of which fingers are up
 
        if cy <= gestureThreshold:  # If hand is at the height of the face
            
            if fingers ==[1,1,0,0,0]:
                start_presentation()
            if fingers == [0, 1, 0, 0, 0]:
                move_left()
            if fingers == [0, 1, 1, 0, 0]:
                print("Right")
                move_right()
            if fingers==[0,1,1,1,1]:
                close_presentation()
    
    key = cv2.waitKey(20)
    if key == ord('q'):
        break