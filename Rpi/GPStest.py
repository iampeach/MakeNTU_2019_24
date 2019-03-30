import serial

#init
gps = serial.Serial('/dev/ttyS0', baudrate = 9600, timeout = 0.5)

#run
while True:
	data = gps.readline()
	if not data or data == '\n' or data[0:6] == '$GPTXT': continue
	print(data)
	data = data.split(',')
	for d in data : 
		if d : print(d)
	print('-----')