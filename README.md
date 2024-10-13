# An Introduction to Object Detection and Pose Estimation with YOLOv11

## Abstract:
The YOLO (You Only Look Once) algorithm is the current state of the art for object detection within the field of computer vision. In addition to providing real-time inference capabilities suitable for both static images and video feeds, the newest YOLO release supports additional tasks such as pose estimation, oriented bounding boxes, and image segmentation. Attendees will gain a foundational understanding of how this algorithm operates, as well as hands-on experience using the Ultralytics python library. Provided code notebooks will demonstrate how to run out-of-the-box inference with basic pretrained models, as well as how to fine-tune existing models for additional functionality and train new models from scratch for domain-specific use cases.

## Description:
This tutorial will consist of three sections:

### Introduction
We will begin by providing a basic background in the fundamentals of the YOLO algorithm. Attendees will become familiar with the foundational concepts of object detection, including how YOLO works under the hood to predict bounding box coordinates and class probabilities with a single pass over an image or video frame.

### Live Demonstration
Using the presenter’s live webcam feed, we will see how both the object detection and pose estimation models work in real-time. This will demonstrate both the functionality of these tools as well as the limitations of the out-of-the-box pretrained models. We will also take a brief look at the source code of the Ultralytics python library to see how the pose estimation model builds upon the existing architecture of the object detection model to produce the additional keypoint predictions (as well as the standard bounding boxes).

### Code Examples and Applications
Finally, we will work through three notebooks to gain hands-on experience applying these tools. Code will be provided in advance through a GitHub repository, and all necessary datasets will be integrated directly through the Ultralytics and HuggingFace APIs.

#### Attendees will leave understanding how to:
-	Use pretrained object detection and pose estimation models to run inference on new datasets (previously unseen to the models).
-	Update the base dataset for the object detection model to include new object classes and retrain the model to include this new functionality.
-	Train a completely new object detection model on a novel dataset consisting of domain-specific classes.
-	Train completely new pose estimation models to demonstrate domain-specific applications on both live and pre-recorded video feeds.
