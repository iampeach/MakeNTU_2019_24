import requests
import util
import random

def sendBackEnd(url, lat, lon):
	d = dict()
	if lat is None : lat = 25.045723 + random.random()/1000 - 0.5
	if lon is None : lon = 121.531018 + random.random()/1000 - 0.5
	lat = str(lat)[:8] + 'N' if lat >=0 else str(-1*lat)[:8] + 'S'
	lon = str(lon)[:9] + 'E' if lon >=0 else str(-1*lon)[:9] + 'W'

	d["name"] = "waterbottle"
	d["time"] = util.getDate()
	d["lat"]  = lat
	d["long"] = lon

	r = requests.post(url, data = d)

if __name__ == '__main__':
	sendBackEnd(None, None)
