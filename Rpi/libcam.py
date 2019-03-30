import picamera 
import util
import cv2
import time
import sys

def prepareCam() :
	cam = picamera.PiCamera()
	cam.start_preview()
	time.sleep(2)
	return cam

def closeCam(cam) :
	cam.stop_preview()

def capture(cam, name="Pictures/img.jpg") :
	cam.capture(name)
	return cv2.imread(name) 

def record(cam, name="Videos/Video" + util.getTime() + ".h264", duration = 60):
	cam.start_recording(name)
	
	for i in range(int(duration)):
		print(i)
		time.sleep(1)
	cam.stop_recording()

if __name__ == '__main__':
	cam = prepareCam()

	if len(sys.argv) == 1 : capture(cam, "Pictures/img" + util.getTime() + ".jpg")
	else : record(cam, duration = int(sys.argv[1]) )

	closeCam(cam)