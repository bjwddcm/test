import numpy as np
import cv2

win = cv2.namedWindow('dzd',cv2.WINDOW_NORMAL)
cv2.resizeWindow('dzd',640,200)
rose = cv2.imread('./rose.jpg')
cv2.imshow('dzd',rose)
cv2.waitKey(0)
cv2.destroyWindow('dzd')

# v = cv2.VideoCapture('./dzd2.mp4')
face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt2.xml')
# 视频是由一张张图片组成，每一张图片，帧
while True:
    flag,frame = v.read()
    if not flag:
        break
#     frame = cv2.resize(frame,(640,360))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_zones = face_detector.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 3)
    for x,y,w,h in face_zones:
        cv2.rectangle(frame,pt1 = (x,y),pt2 = (x+w,y+h),color = [0,0,255],thickness=2)
    cv2.imshow('dzd',frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
         break
v.release()#释放视频流
cv2.destroyAllWindows()