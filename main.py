from ultralytics import YOLO
import os
from IPython.display import display, Image
from IPython import display
display.clear_output()
# !yolo checks



# !pip install roboflow


from roboflow import Roboflow
rf = Roboflow(api_key="zYyYzOw5fYwT2yGqGY4U")
project = rf.workspace("pattern-recognition-and-machine-learning").project("carplate-collected-by-us-and-roboflow")
version = project.version(5)
dataset = version.download("yolov8")



# !pip install ultralytics==8.0.196

# !yolo task=detect mode=train model=yolov8m.pt data={dataset.location}/data.yaml epochs=1 imgsz=640


Image(filename=f'/content/runs/detect/train/confusion_matrix.png',width=600)

Image(filename=f'/content/runs/detect/train/results.png', width = 600)

# !yolo task=detect mode=val model=/content/runs/detect/train/weights/best.pt data={dataset.location}/data.yaml

# !yolo task=detect mode=predict model=/content/runs/detect/train/weights/best.pt conf=0.5 source={dataset.location}/test/images

import glob
from IPython.display import Image, display

for imageName in glob.glob('/content/runs/detect/predict/*.jpg'):
    display(Image(filename=imageName, height=600))
    print("\n")