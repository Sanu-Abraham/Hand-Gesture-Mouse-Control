import cv2
import mediapipe as mp
import time

class HandTracker:
    
    def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectConf=0.5, trackConf=0.5):
        
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectConf = detectConf
        self.trackConf = trackConf
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectConf, self.trackConf)
        self.drawing_utils = mp.solutions.drawing_utils


    def trackHands(self, img, draw=True):
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for landmark in self.results.multi_hand_landmarks:
                if draw:
                    self.drawing_utils.draw_landmarks(img, landmark, self.mpHands.HAND_CONNECTIONS)
        return img

    
    def getPosition(self, img, handNo=0, draw=False, index=[]):

        lmList = []
        
        if self.results.multi_hand_landmarks:
            print(self.results.multi_hand_landmarks)
            handLandmarks = self.results.multi_hand_landmarks[handNo]
            for idx, lm in enumerate(handLandmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([idx, cx, cy])
                for i in index:
                    if idx == i and draw:
                        cv2.circle(img, (cx, cy), 5, (255,0,0), 5)
        return lmList
