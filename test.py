import cv2 
import numpy as np
from ultralytics import YOLO

count = 0
points = []
model = YOLO('yolov8n-pose.pt')
out = cv2.VideoWriter('transformed_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (640, 480))

def click_event(event, x, y, flags, params): 
	global count
	if event == cv2.EVENT_LBUTTONDOWN: 
		print(x, ' ', y) 
		points.append((x,y))
		count+=1

def bird_eye_tranform(image, points, pts2):
	points = np.float32(points)
	matrix = cv2.getPerspectiveTransform(points, pts2)
	transformed_frame = cv2.warpPerspective(image, matrix, (640, 480))
	return transformed_frame

if __name__=="__main__": 
	pts2 = np.float32([[0,0],[0,480],[640,0],[640,480]])
	vid = cv2.VideoCapture("drone_crowd.mp4")
	success, image = vid.read()
	while success:
		success, image =vid.read()
		if success == False:
			continue
		cv2.imshow('image', image)
		if count < 4:  
			cv2.setMouseCallback('image', click_event)
		else:
			transformed_frame = bird_eye_tranform(image, points, pts2) 
			out.write(transformed_frame)
			cv2.imshow('trans', transformed_frame)
		cv2.waitKey(34)
	out.release()
	cv2.destroyAllWindows() 
	if count ==4:
		results = model("transformed_video.mp4", show=True)
