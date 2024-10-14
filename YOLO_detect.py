'''
This file is used to run various versions of the YOLO object detection model for real-time inference over a live webcam or previously recorded video
'''

from ultralytics import YOLO

model = YOLO('yolo11s.pt')
#model = YOLO('pen_detect.pt')

results = model(source=0, show=True, conf=0.3, save=True)
#results = model(source="https://www.youtube.com/watch?v=iZxNbAwY_rk", show=True)