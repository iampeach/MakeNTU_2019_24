import serial
import time
import util

def getPos(timeout = 2, logfile = "/home/pi/log/gps.log") :
	start = time.time()

	getData = False
	lat_deg = -1
	lat_min = -1.0
	lat_ele = ""
	long_deg = -1
	long_min = -1.0
	long_ele = ""
	gps = serial.Serial('/dev/ttyS0', baudrate = 9600, timeout = 0.5)

	while not getData :
		if time.time() - start > timeout : break

		try:
			data = gps.readline()
		except Exception as e:
			#print(e)
			gps.close()
			gps = serial.Serial('/dev/ttyS0', baudrate = 9600, timeout = 0.5)
			continue

		data = str(data, 'utf-8')
		if not data or data == '\n': continue
		if logfile :
			with open(logfile, "a") as f :
				log = str(util.getTime()) + " : " + data
				f.write(log)

		#parse data
		data = data.split(',')
		if data[0] == "$GPRMC" :
			if len(data) != 13 : continue
			if data[2] == 'V' : continue

			getData = True
			#lat
			if data[3] and data[4] :
				lat_deg = int(data[3][0:2])
				lat_min = float(data[3][2:])
				lat_ele = str(data[4])

			#long
			if data[5] and data[6] :
				long_deg = int(data[5][0:3])
				long_min = float(data[5][3:])
				long_ele = str(data[6])

		elif data[0] == "$GPGGA" :
			if len(data) != 15 : continue
			if data[6] == '0' : continue
			if data[7] == '00' : continue

			getData = True
			#lat
			if data[2] and data[3] :
				lat_deg = int(data[2][0:2])
				lat_min = float(data[2][2:])
				lat_ele = str(data[3])

			#long
			if data[4] and data[5] :
				long_deg = int(data[4][0:3])
				long_min = float(data[4][3:])
				long_ele = str(data[5])

		elif data[0] == "$GPGLL" :
			if len(data) != 8 : continue
			if data[6] == 'V' : continue

			getData = True
			#lat
			if data[1] and data[2] :
				lat_deg = int(data[1][0:2])
				lat_min = float(data[1][2:])
				lat_ele = str(data[2])

			#long
			if data[3] and data[4] :
				long_deg = int(data[3][0:3])
				long_min = float(data[3][3:])
				long_ele = str(data[4])

		else : continue

	#result
	if lat_deg == -1 : return None, None

	lat_min, long_min = lat_min/60, long_min/60
	lat , lon= lat_deg + lat_min , long_deg + long_min
	lat = -1*lat if lat_ele == "S" else lat
	lon = -1*lon if long_ele == "W" else lon

	return lat, lon

if __name__ == '__main__':
	print(getPos())