import imutils
import cv2

def preprocess(frame):
	# resize the frame (so we can process it faster)
	frame = imutils.resize(frame, width=600)
	return cv2.resize(origin_frame, (416,416))
