import cv2
import numpy as np
import time
import pose_estimation_module as pm


cap = cv2.VideoCapture("videos/curls.mp4")

detector = pm.poseDetector()

count = 0
direction = 0
pTime = 0

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    # img = cv2.imread("videos/test_dips.jpg")
    img = detector.findPose(img,False)
    lmList = detector.findPosition(img, False)
    # print(lmList)

    if len(lmList) != 0:
        angle = detector.findAngle(img,11,13,15)
        percentage = np.interp(angle,(210,310),(0,100))
        # print(percentage,angle)

        # check for the dumbell curls
        if percentage == 100:
            if direction==0 :
                count += 0.5
                direction = 1

        if percentage == 0:
            if direction == 1:
                count += 0.5
                direction = 0

        print(count)


        cTime = time.time()
        fps = 1/ (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f'{int(count)}', (50,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 5)
        cv2.putText(img, f'fps: {int(fps)}',(1000,50),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)











    cv2.imshow("Scene1", img)
    cv2.waitKey(1)

