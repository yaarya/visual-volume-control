import cv2
import time
import numpy
import HandTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
######################################################

wCam, hCam = 640, 480

#####################################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 455
volPer = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)

    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        #print(lmList[4], lmList[8])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        z1, z2 = lmList[4][3], lmList[8][3]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1, y1), 7, (255, 165, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 7, (255, 165, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 165, 0), 2)
        cv2.circle(img, (cx, cy), 5, (0, 165, 255), cv2.FILLED)

        length = math.hypot(x2-x1,y2-y1,z2-z1)
        # print(length)
        # print(z2-z1)

        # Hand Range = 20 to 130 at one arm distant torso (hand will be at approx 3/4 of that distance)
        # Volume Range = -96.0 to 0
        # Bar Range = 455 (min) to 10 (max)
        vol = numpy.interp(length, [20,130], [minVol, maxVol])
        volBar = numpy.interp(length, [20,130], [455, 10])
        volPer = numpy.interp(length, [20, 130], [0,100])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length<20:
            cv2.circle(img, (cx, cy), 7, (0, 0, 0), cv2.FILLED)

    cv2.rectangle(img, (10,10), (30,455), (0, 0, 0), 3)
    cv2.rectangle(img, (10, int(volBar)), (30, 455), (0, 165, 255), cv2.FILLED)
    cv2.putText(img, f'vol:{int(volPer)}%', (33, 455), cv2.FONT_HERSHEY_TRIPLEX,
                0.7, (0, 165, 255), 1)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:{int(fps)}', (560, 27), cv2.FONT_HERSHEY_COMPLEX,
                0.7, (255, 165, 255), 1)

    cv2.imshow("Img", img)
    cv2.waitKey(1)