import serial

#init
gps = serial.Serial('/dev/ttyS0', baudrate = 9600, timeout = 0.5)

#run
while True:
	try:
		data = gps.readline()
	except Exception as e:
		print(e)
		gps.close()
		gps = serial.Serial('/dev/ttyS0', baudrate = 9600, timeout = 0.5)
		continue

	if data == '\n' : continue
	if data[0:6] == "$GPTXT" : continue

	print(data[:-1])