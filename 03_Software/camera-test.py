#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (2592, 1944)
camera.framerate = 1
camera.awb_mode = 'off'
camera.capture('test.jpg')
# for red in range (0, 9, 1):
#     for blue in range(0, 9, 1):
#         camera.awb_gains = (red, blue)
#         sleep(2)
#         camera.capture(f"red{red}-blue{blue}.jpg")
#         print(f"Captured image with red: {red} and blue: {blue}...")