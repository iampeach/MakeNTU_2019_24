import serial

#init
gps = serial.Serial('/dev/ttyS0', baudrate = 9600, timeout = 0.5)
#gps.xonxoff = 1

#run
#gps.open()
if gps.isOpen() :
	print('success to open.')
	while True :
		print(gps.readline())
else :
	print('fail to open gps.')