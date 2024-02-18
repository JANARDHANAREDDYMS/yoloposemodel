import cv2
import numpy as np

vidcap =  cv2.VideoCapture("/Users/janardhanareddyms/Desktop/crowd.mp4")

success, img = vidcap.read()

while success:
    success, img = vidcap.read()
    frame = cv2.resize(img,(640,480))

    tl = (252,122)
    bl=(202,444)
    tr=(483,123)
    br = (584,433)

    cv2.circle(frame,tl,5,(0,0,255),-1)
    cv2.circle(frame,bl,5,(0,0,255),-1)
    cv2.circle(frame,tr,5,(0,0,255),-1)
    cv2.circle(frame,br,5,(0,0,255),-1)


    pts1 = np.float32([tl,bl,tr,br])
    pts2  = np.float32([[0,0], [0,480], [640,0], [640,480]])

    matrix = cv2.getPerspectiveTransform(pts1,pts2)

    transformed  = cv2.warpPerspective(frame,matrix,(640,480))

    cv2.imshow("Frame",frame)
    cv2.imshow("Trans Frame", transformed)

    if cv2.waitKey(1) == '27':
        break