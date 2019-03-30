import picamera
import time

with picamera.PiCamera() as camera :
    camera.start_preview()
    camera.start_recording('/home/pi/video'+ str(time.time())+'.h264')
    time.sleep(120)
    camera.stop_recording()
    camera.stop_preview()
