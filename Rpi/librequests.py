import requests
import util
import random

def sendBackEnd(url, lat, lon):
	d = dict()
	if lat is None : lat = 25.045723 + (random.random()-0.5)/10000
	if lon is None : lon = 121.531018 + (random.random()-0.5)/10000 
	lat = str(lat)[:8] + 'N' if lat >=0 else str(-1*lat)[:8] + 'S'
	lon = str(lon)[:9] + 'E' if lon >=0 else str(-1*lon)[:9] + 'W'

	d["name"] = "waterbottle"
	d["time"] = util.getDate()
	d["lat"]  = lat
	d["long"] = lon
	pic = {'file': open('Pictures/img.jpg', 'rb') }

	headers = {
		"Content-Type": "application/json"
	}

	r = requests.post(url,files = pic, data = d)
	#print(requests.Request('POST', url,  data = d))

if __name__ == '__main__':
	sendBackEnd("http://" + "10.20.2.99" + ":3000/data", None, None)
