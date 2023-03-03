def Gesture_Control():
    from cvzone.HandTrackingModule import HandDetector
    import cv2
    import os
    import numpy as np
    from auto import open_file,start_presentation,move_left,move_right,close_presentation
 
    # Parameters
    width, height = 500, 500
    gestureThreshold = 400
   
    q_count=0
    w_count=0
    
    # Camera Setup
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)
    
    # Hand Detector
    detectorHand = HandDetector(detectionCon=0.8, maxHands=1)
    
    # Variables
    buttonPressed = False
    imgNumber = 0
    hs, ws = int(120 * 1), int(213 * 1)  # width and height of small image
    
 
    while True:
        # Get image frame
        success, img = cap.read()
        img = cv2.flip(img, 1)
      
        # Find the hand and its landmarks
        hands, img = detectorHand.findHands(img)  # with draw
        # Draw Gesture Threshold line
        cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 10)
    
        if hands and buttonPressed is False:  # If hand is detected
    
            hand = hands[0]
            cx, cy = hand["center"]
            lmList = hand["lmList"]  # List of 21 Landmark points
            fingers = detectorHand.fingersUp(hand)  # List of which fingers are up
    
            # Constrain values for easier drawing
            xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
            yVal = int(np.interp(lmList[8][1], [150, height-150], [0, height]))
            indexFinger = xVal, yVal
    
            if cy <= gestureThreshold:  # If hand is at the height of the face
                if fingers==[1,1,0,0,0] and q_count==0:
                    open_file()
                    q_count=1
                if fingers==[1,1,1,0,0] and w_count==0:
                    start_presentation()
                    # w_count=1
                    
                if fingers == [0, 1, 0, 0, 0]:
                    print("Left")
                    move_left()
                if fingers == [0, 1, 1, 0, 0]:
                    print("Right")
                    move_right()
                if fingers==[0,1,1,1,1]:
                    close_presentation()
                    # w_count=0
    
        cv2.imshow("Image", img)
    
        key = cv2.waitKey(1)
        if key == ord('q'):
            break