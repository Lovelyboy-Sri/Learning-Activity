import cv2
import mediapipe as mp
import pyautogui as pat


cam = cv2.VideoCapture(0)
fm = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

sw,sh = pat.size()

while True:
    _, frame = cam.read()

    frame = cv2.flip(frame,1)    
    ef = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    op = fm.process(ef)

    lp = op.multi_face_landmarks

    fh,fw,_ = frame.shape
    if lp:
        lm = lp[0].landmark
        for id, lms in enumerate(lm[468:478]):
            x = int(lms.x * fw)
            y = int(lms.y * fh)

            cv2.circle(frame, (x,y),3,(0, 255, 0))
            if id == 1:
                sx = sw / fw * x
                sy = sh /fh * y
                pat.moveTo(sx,sy)
                

        l = [lm[145],lm[159]]   
        for lm in l:
             x = int(lms.x * fw)
             y = int(lms.y * fh)
             cv2.circle(frame, (x,y),3,(0, 255, 255))
        if (l[0].y - l[1].y) < 0.01:
            pat.click()
            print("click")
            pat.sleep(2)

        else:
            print("Not click")


    cv2.imshow("Eye Controlled mouse", frame)
    cv2.waitKey(1)


