import cv2
import pyautogui as ap
import mediapipe as mp

cam = cv2.VideoCapture(0)
hd = mp.solutions.hands.Hands()
du = mp.solutions.drawing_utils
sw,sh = ap.size()

ind_y = 0

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame,1)
    fh,fw,_ = frame.shape


    efr = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    op = hd.process(efr)
    hands = op.multi_hand_landmarks

    if hands:
        for hand in hands:
            du.draw_landmarks(frame,hand)
            lms = hand.landmark

            for id, lm in enumerate(lms):
                x = int(lm.x*fw)
                y = int(lm.y*fh)


                if id == 8:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,132,123))
                    ind_x = sw/fw*x
                    ind_y = sh/fh*y
                    ap.moveTo(ind_x,ind_y)
                
                if id == 4:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,132,123))
                    mid_x = sw/fw*x
                    mid_y = sh/fh*y
                #    ap.moveTo(ind_x,ind_y)

                    print("Outside value : ",abs(ind_y - mid_y))
                    if abs(ind_y-mid_y)<55:
                        ap.click()
                        ap.sleep(1)


    cv2.imshow("Hand free mouse",frame)
    cv2.waitKey(1)