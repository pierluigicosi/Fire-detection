#GRADIO APP


import gradio as gr
import torch
from PIL import Image


# Model
model = torch.hub.load('yolov5', 'custom', 'best.pt', source='local',force_reload=True)  # local repo


def yolo(im, size=640):
    g = (size / max(im.size))  # gain
    im = im.resize((int(x * g) for x in im.size), Image.ANTIALIAS)  # resize

    results = model(im)  # inference
    results.render()  # updates results.imgs with boxes and labels
    return Image.fromarray(results.imgs[0])


inputs = gr.inputs.Image(type='pil', label="Original Image")
outputs = gr.outputs.Image(type="pil", label="Output Image")


title = "Fire Detection with YOLOv5"
description = "YOLOv5 demo for fire detection. Upload an image or click an example image to use."
article = "<p style='text-align: center'>YOLOv5 is a family of compound-scaled object detection models trained on the COCO dataset, and includes " \
          "simple functionality for Test Time Augmentation (TTA), model ensembling, hyperparameter evolution, " \
          "and export to ONNX, CoreML and TFLite. <a href='https://github.com/ultralytics/yolov5'>Source code</a> |" \
          "<a href='https://apps.apple.com/app/id1452689527'>iOS App</a> | <a href='https://pytorch.org/hub/ultralytics_yolov5'>PyTorch Hub</a></p>"

examples = [['example/fire.103.png'], ['example/fire.158.png'],['example/fire.204.png']]
gr.Interface(yolo, inputs, outputs, title=title, description=description, article=article, examples=examples).launch(
    debug=True)
