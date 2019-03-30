import libcam
import libgps
import librequests
import time
import util

mainUrl = "10.20.2.99"

#init
print(util.makelog("INIT"))
cam = libcam.prepareCam()
detector = util.Detector()

#run
while True:
	print(util.makelog("take picture"))
	pic = libcam.capture(cam)

	if detector.predict(pic) : #TODO
		print(util.makelog("got object"))
		lat, lon = libgps.getPos()
		print(util.makelog("lat:" + str(lat) + ", long:" + str(lon)))
		librequests.sendBackEnd("http://" + mainUrl + ":3000/data", lat, lon)
	else : print(util.makelog("no object"))

	time.sleep(0.1)

#post
print(util.makelog("finish"))
libcam.closeCam(cam)