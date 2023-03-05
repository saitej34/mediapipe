import streamlit as st
import cv2
import pyautogui as pt
from cvzone.HandTrackingModule import HandDetector
video = cv2.VideoCapture(0)
handdetect = HandDetector(detectionCon=0.8,maxHands=1)
def play():
    while True:
        ret,frame = video.read()
        hands,img=handdetect.findHands(frame)
        if hands: 
            lmlist = hands[0]
            k=handdetect.fingersUp(lmlist)
            print(k)
            if k==[1,1,1,1,1] :
                pt.press("space")
                cv2.putText(frame,'Jumping',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,cv2.LINE_AA)
                cv2.putText(frame,'Running',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,cv2.LINE_AA)
            elif k==[0,0,0,0,0]:
                pt.press("down")

        cv2.imshow("Frame",frame)
        k=cv2.waitKey(1)
        if k==ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()
st.title("Enjoy Games using Hands")
temp = st.button("Start Camera")
if temp==True:
    play()
st.text("Test with Chrome Dino")
