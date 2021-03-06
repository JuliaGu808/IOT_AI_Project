from google.cloud import vision
import os
from PIL import Image, ImageDraw
from picamera import PiCamera
import time
import serial

# Create an object for GCP Vision
client = vision.ImageAnnotatorClient()

# Init Pi camera
camera = PiCamera()
camera.resolution = (720, 480)
camera.rotation = 180
print("Waiting 2 seconds to init the camera...")
time.sleep(2)
print("Camera setup OK.")

# Set serial to read when arduino signal comes in
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print("Serial OK.")

def take_foto():
    file_name = "imgs/img_" + str(time.time()) + ".jpg"
    camera.capture(file_name)
    return file_name

def saveStatus(status):
        f = open("status.txt", "w")
        f.write(status)
        f.close()

def send_img_if_joy_send_back(file_name):
    image_name=file_name # "imgs/img_1640358742.2227461.jpg" file_name

    with open(image_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.face_detection(image=image)
    faces = response.face_annotations
    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE','LIKELY', 'VERY_LIKELY')
    is_open=False
    for face in faces:
        if(likelihood_name[face.joy_likelihood] in ['LIKELY', 'VERY_LIKELY']): is_open=True
    if is_open:
        ser.write("open\n".encode('utf-8'))
        saveStatus("open")
    else:
        saveStatus("close")
        time.sleep(2)
        saveStatus("init")


# Execute this loop forever until terminated by the user or
# the raspberry pi fails
while True:
    try:
        time.sleep(0.01)
        if ser.in_waiting > 0:
            msg = ser.readline().decode('utf-8').rstrip()
            if(msg=="foto"):
                file=take_foto()
                send_img_if_joy_send_back(file)
            if(msg=="init"):
                saveStatus("init")
    # In case of keyboard interruption or system crash, raise these exceptions
    except (KeyboardInterrupt, SystemExit):
        print("Close serial communication.")
        ser.close()
        raise
