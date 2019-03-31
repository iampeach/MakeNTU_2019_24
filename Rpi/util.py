import time


def getTime():
	return time.strftime("%H%M%S", time.localtime()) 

def getDate():
	return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def makelog(data) :
	return getTime() + " : " + data