from flask import Flask, flash, request, redirect, url_for
import sys
app = Flask(__name__)
 
@app.route("/")
def hello():
	app.logger.error(request)
	app.logger.error(request.data, file=sys.stderr)
	return "Hello World!"
 
if __name__ == "__main__":
	app.run(host='0.0.0.0', threaded = True)
