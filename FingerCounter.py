import numpy
import cv2
import time
import os
import HandTrackingModule as htm

wCam, hCam = 640, 480    # dim of screen

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "FingerImages"
myList = os.listdir(folderPath)     # list of image directories
print(myList)

overlayList = []    # list of actual images
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')  # store one image
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)       # append that image

pTime = 0

detector = htm.handDetector(detectionCon=0.75)
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []
        # thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # fingers
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        # print(fingers)
        totalFingers = fingers.count(1)


        h, w, c = overlayList[totalFingers-1].shape
        img[0:h, 0:w] = overlayList[totalFingers-1]
        

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:{int(fps)}', (560, 27), cv2.FONT_HERSHEY_COMPLEX,
                0.7, (255, 165, 255), 1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)