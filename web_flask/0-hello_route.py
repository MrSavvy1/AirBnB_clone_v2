#!/usr/bin/python3
"""
This will start a simple web application using flask
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def start():
	"""
	This defination will perform just a string 'Hello HBNH!'
	"""
	return 'Hello HBNH!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
