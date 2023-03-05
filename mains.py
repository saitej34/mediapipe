import cv2
from cvzone.HandTrackingModule import HandDetector
video = cv2.VideoCapture(0)
handdetect = HandDetector(detectionCon=0.8,maxHands=2)
while True:
    ret,frame = video.read()
    hands,img=handdetect.findHands(frame)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
