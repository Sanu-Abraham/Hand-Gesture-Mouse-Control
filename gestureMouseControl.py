import cv2
import time
import numpy as np
import HandTrackingModule as htm
import mouse
import math

capture = cv2.VideoCapture(0)

tracker = htm.HandTracker(detectConf=0.98)

while True:
    success, img = capture.read()

    scale_percent = 150 
    width = int(img.shape[1] * scale_percent / 100) 
    height = int(img.shape[0] * scale_percent / 100) 
    dim = (width, height) 
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) 
    
    img = tracker.trackHands(img)
    lmList = tracker.getPosition(img, 0, draw=True, index=[8, 12])
    
    if len(lmList) != 0:
        indexX, indexY = lmList[8][1], lmList[8][2]
        middleX, middleY = lmList[12][1], lmList[12][2]

        xPosition = np.interp(indexX, [200, width-200], [1920, 0])
        yPosition = np.interp(indexY, [200, height-200], [0, 1080])

        width = int(math.hypot((indexX-middleX), (indexY-middleY)))
        
        if width <= 50:
            cv2.rectangle(img, (middleX, middleY, width, 20), (255, 0, 0), cv2.FILLED)
            mouse.click('left')
        else:
            mouse.move(xPosition, yPosition, True, 0.00001)

    cv2.imshow("Hand Gesture Mouse Control", img)
    cv2.waitKey(1)
