from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import numpy as np
import imutils
import cv2 as cv
import serial
import random

windowCenter = 320
centerBuffer = 10
pwmBound = float(50)
cameraBound = float(320)
kp = pwmBound / cameraBound
leftBound = int(windowCenter - centerBuffer)
rightBound = int(windowCenter + centerBuffer)
error = 0
ballPixel = 0

serial_obj=serial.Serial('/dev/ttyACM0',9600)

#Camera setup
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 15
rawCapture = PiRGBArray(camera, size = (640, 480))

time.sleep(0.1)

lower_yellow = np.array([17, 98, 66])
upper_yellow = np.array([72, 255, 255])

def arudino_cam():
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    	image = frame.array
    	output = image.copy()
    	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    	mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    	mask = cv2.erode(mask, None, iterations=2)
    	mask = cv2.dilate(mask, None, iterations=2)
    	output = cv2.bitwise_and(output, output, mask=mask)
    	gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 3, 500, minRadius = 10, maxRadius = 200, param1 = 100,  param2 = 60)
    	ballPixel = 0

    	if circles is not None:
    		circles = np.round(circles[0, :]).astype("int")
    		for (x, y, radius) in circles:

    			cv2.circle(output, (x, y), radius, (0, 255, 0), 4)

    			if radius > 10:
    				ballPixel = x
    			else:
    				ballPixel = 0

    	key = cv2.waitKey(1) & 0xFF
    	rawCapture.truncate(0)

    	if ballPixel == 0:
    		print ("no ball")
    		error =0
    		serial_obj.write(b'4')

    	elif (ballPixel < leftBound) or (ballPixel > rightBound):
    		error = windowCenter - ballPixel
    		if  ballPixel < (leftBound):
    			print ("left side")
    			serial_obj.write(b'3')
    		elif ballPixel > (rightBound):
    			print ("right side")
    			serial_obj.write(b'2')
    	else:
    		print ("middle")
    		serial_obj.write(b'1')
    		if (radius < 40):
    			serial_obj.write(b'1')
    		else:
    			serial_obj.write(b'0')

    	if key == ord('q'):
    		break

    cv2.destroyAllWindows()
    camera.close()
'''
def arudino_data():
    data=serial_obj.readline()
    try:
        str_rn = data.decode()
        str = str_rn.rstrip()
        return str
    except:
        return 0
'''
arudino_cam()
