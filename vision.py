from google.cloud import vision
import os
from PIL import Image, ImageDraw
from picamera import PiCamera
import time

client = vision.ImageAnnotatorClient()

camera = PiCamera()
camera.resolution = (720, 480)
camera.rotation = 180
print("Waiting 2 seconds to init the camera...")
time.sleep(2)
print("Camera setup OK.")
file_name = "imgs/img_" + str(time.time()) + ".jpg"
camera.capture(file_name)

image_name="imgs/img_1640207935.3103487.jpg"
with open(image_name, 'rb') as image_file:
    content = image_file.read()
    
image = vision.Image(content=content)
response = client.face_detection(image=image)
print(response)
