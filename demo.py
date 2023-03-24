def Gesture_Control():
    import cv2
    import HandTrackingModule as htm
    from autobot import open_file,start_presentation,move_left,move_right,close_presentation
    
    wCam, hCam = 640, 480
    w_count=0
    
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    detector = htm.HandDetector(detectionCon=0.75)
    
    tipIds = [4, 8, 12, 16, 20]
    
    while True:
        success, img = cap.read()
        img=cv2.flip(img,1)
        if not success:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        # print(lmList)
        if len(lmList) != 0:
            fingers = []
            # Thumb
            if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
    
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            
            
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
                        print("done")
    
        cv2.imshow("Image", img)
        if cv2.waitKey(1)&0xFF==ord('q'):
            break
                   
    cv2.destroyAllWindows
  