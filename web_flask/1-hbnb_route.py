#!/usr/bin/python3
"""
This will start a simple web application using flask
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_splashes = False

@app.route('/')
def start():
	"""
	This defination will perform just a string 'Hello HBNB!'
	"""
	return 'Hello HBNB!'

@app.route('/hbnb/')
def hbnb():
	"""
	different
	"""
	retirni
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
