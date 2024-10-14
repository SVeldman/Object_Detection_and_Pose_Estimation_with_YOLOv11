'''
This file is used to run various versions of the YOLO pose estimation model for real-time inference using either a live webcam or previously recorded video
'''

from ultralytics import YOLO

model = YOLO('yolo11n-pose.pt')
#model = YOLO('hand_model.pt')
#tiger_model = YOLO('tiger_model.pt')

results = model(source=0, show=True, conf=0.3, save=True)

#while True:
    #results = model(source="https://www.youtube.com/watch?v=Mol0lrRBy3g", show=True)

#results = tiger_model(source="https://www.youtube.com/watch?v=JMsCJhGtPKM", show=True)
