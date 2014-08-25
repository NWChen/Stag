'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

if __name__ == '__main__':
	app.debug = True
	app.run()
'''

import os
from flask import Flask, redirect, url_for, session
from flask import render_template
from flask import request

app = Flask(__name__)
points = {}
segments = {}
point_index = 0

@app.route('/add_point')
def add_point():
	x = request.args.get('col', 0, type=int)
	y = request.args.get('row', 0, type=int)
	points[str(x) + '_' + str(y)] = [point_index, Point(x, y)]
	point_index += 1

	#find adjacents and add to segments

	return

@app.route('/')
def build_grid():
	rows, cols = [], []
	for i in xrange(0, 20):
		rows.append(i+1)
		cols.append(i+1)
	return render_template("index.html", rows=rows, cols=cols)

if __name__ == '__main__':
	app.run(debug=True)