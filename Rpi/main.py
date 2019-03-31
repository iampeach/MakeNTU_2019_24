import libcam
import libgps
import librequests
import time
import util

ML_SERVER_URL = "http://10.20.2.96:5000/data"

#init
print(util.makelog("INIT"))
cam = libcam.prepareCam()

#run
while True:
	print(util.makelog("start take picture"))
	pic = libcam.capture(cam)
	print(util.makelog("end take picture"))

	lat, lon = libgps.getPos()
	print(util.makelog("lat:" + str(lat) + ", long:" + str(lon)))
	librequests.sendBackEnd(ML_SERVER_URL, lat, lon)
	time.sleep(0.1)

#post
print(util.makelog("finish"))
libcam.closeCam(cam)