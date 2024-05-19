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
	return "HBNB"

@app.route('/c/<text>')
def parms(text):
	"""
	params formating
	"""
	fparams = text.replace('_', ' ')
	return "c {}".format(fparams)


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def no_text(text):
	"""
	with params and text
	"""
	with_text = text.replace('_', ' ')
	return "Python {}".format(with_text)

@app.route('/number/<int:n>')
def nums(n):
	"""
	identify a number /int
	"""
	return "{} is a number".format(n)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
