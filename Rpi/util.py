import time
import imutils
import cv2
import numpy as np


def getTime():
	return time.strftime("%H%M%S", time.localtime()) 


class Detector():

	def __init__(
		self,
		config='./custom/yolov3-tiny.cfg',
		weights='./backup/yolov3-tiny_20000.weights',
		):
		self.net = cv2.dnn.readNet(weights, config, framework='darknet')

	def predict(self, image: np.array):
		image = self._preprocess(image)
		print(image.shape)
		blob = cv2.dnn.blobFromImage(image)
		self.net.setInput(blob)
		outs = self.net.forward(self._getOutputsNames())
		predictions = []
		for out in outs: 
			for detection in out:
			#each detection  has the form like this [center_x center_y width height obj_score class_1_score class_2_score ..]
				scores = detection[5:]#classes scores starts from index 5
				class_id = np.argmax(scores)
				confidence = scores[class_id]
				if confidence > 0.5:
					predictions.append({
						'class_id': class_id,
						'confidence': confidence,
					})
		return predictions

	@staticmethod
	def _preprocess(frame):
		# resize the frame (so we can process it faster)
		frame = imutils.resize(frame, width=600)
		return cv2.resize(frame, (416,416))
	
	def _getOutputsNames(self):
		layersNames = self.net.getLayerNames()
		return [layersNames[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]


if __name__ == "__main__":
	detector = Detector()
	cap = cv2.VideoCapture(0)
	_, input_image = cap.read()
	predictions = detector.predict(input_image)
	print(predictions)
