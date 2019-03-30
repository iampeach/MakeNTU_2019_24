import requests
import util
import random

def sendBackEnd(lat, lon):
	d = dict()
	if lat is None : lat = 25.045723 + random.random()/1000
	if lon is None : lon = 121.531018 + random.random()/1000
	lat = str(lat)[:8] + 'N' if lat >=0 else str(-1*lat)[:8] + 'S'
	lon = str(lon)[:9] + 'E' if lon >=0 else str(-1*lon)[:9] + 'W'

	d["name"] = "waterbottle"
	d["time"] = util.getDate()
	d["lat"]  = lat
	d["long"] = lon

	r = requests.post("http://10.20.2.99:3000/data", data = d)

if __name__ == '__main__':
	sendBackEnd(None, None)
