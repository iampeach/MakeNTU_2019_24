from __future__ import print_function
import serial
import time

#init
gps = serial.Serial('/dev/ttyS0', baudrate = 9600, timeout = 0.5)
lat_deg = -1
lat_min = -1.0
lat_ele = ""
long_deg = -1
long_min = -1.0
ling_ele = ""

#run
while True:
	time.sleep(0.5)

	try:
		data = gps.readline()
	except Exception as e:
		print(e)
		gps.close()
		gps = serial.Serial('/dev/ttyS0', baudrate = 9600, timeout = 0.5)
		continue

	if not data : continue
	data = data.split(',')

	#parse data
	if data[0] == "$GPRMC" :
		if len(data) != 13 : continue
		if data[2] == 'V' : continue

		#lat
		if data[3] and data[4] :
			lat_deg = int(data[3][0:2])
			lat_min = int(data[3][2:])
			lat_ele = str(data[4])

		#long
		if data[5] and data[6] :
			lat_deg = int(data[5][0:3])
			lat_min = int(data[5][3:])
			lat_ele = str(data[6])

	elif data[0] == "$GPGGA" :
		if len(data) != 15 : continue
		if data[6] == '0' : continue
		if data[7] == '00' : continue

		#lat
		if data[2] and data[3] :
			lat_deg = int(data[2][0:2])
			lat_min = int(data[2][2:])
			lat_ele = str(data[3])

		#long
		if data[4] and data[5] :
			lat_deg = int(data[4][0:3])
			lat_min = int(data[4][3:])
			lat_ele = str(data[5])

	elif data[0] == "$GPGLL" :
		if len(data) != 8 : continue
		if data[6] == 'V' : continue

		#lat
		if data[1] and data[2] :
			lat_deg = int(data[1][0:2])
			lat_min = int(data[1][2:])
			lat_ele = str(data[2])

		#long
		if data[3] and data[4] :
			lat_deg = int(data[3][0:3])
			lat_min = int(data[3][3:])
			lat_ele = str(data[4])

	#print
	print("lat : ", end='')
	if lat_deg != -1 and lat_min != -1.0 and lat_ele :
		print(lat_deg, end=char(248))
		print(lat_min, end='\' ')
		print(lat_ele, end=' ')
	else : print("unknown", end=' ')

	print("long : ", end='')
	if long_deg != -1 and long_min != -1.0 and long_ele :
		print(long_deg, end=char(248))
		print(long_min, end='\' ')
		print(long_ele, end=' ')
	else : print("unknown", end=' ')

	print('time : ', end='')
	print(time.ctime())