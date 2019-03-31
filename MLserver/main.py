import os
from flask import Flask, flash, request, redirect, url_for
import sys
from utils import Detector
import requests
import numpy as np
from PIL import Image

WEB_SERVER_URL = 'http://10.20.2.99:3000/data'

upload_folder = './upload'
if not os.path.exists(upload_folder):
	os.mkdir(upload_folder)

app = Flask(__name__)
detector = Detector()
 

@app.route("/data", methods=['POST'])
def predict():
	file = request.files.get('file')
	save_path = os.path.join(upload_folder, file.filename)
	file.save(save_path)
	image = np.asarray(Image.open(save_path))
	prediction = detector.predict(image)
	if not prediction:
		requests.post(
			WEB_SERVER_URL, 
			files=request.files,
			data =request.form,
		)
	return 'OK'

if __name__ == "__main__":
	app.run(host='0.0.0.0', threaded = True)
