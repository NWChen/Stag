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
from flask import Flask, redirect, url_for, session, jsonify
from flask import render_template
from flask import request

from Point import Point

points = []
segments = []
point_index = 0
app = Flask(__name__)

@app.route('/add_point')
def add_point():
	global point_index
	x = request.args.get('col', 0, type=int)
	y = request.args.get('row', 0, type=int)
	points.append([point_index, Point(x, y)])
	point_index += 1
	return jsonify(result=str(y) + '_' + str(x)) #find adjacents and add to segments

@app.route('/remove_point')
def remove_point():
	x = request.args.get('col', 0, type=int)
	y = request.args.get('row', 0, type=int)

@app.route('/')
def build_grid():
	rows, cols = [], []
	for i in xrange(0, 20):
		rows.append(i+1)
		cols.append(i+1)
	return render_template("index.html", rows=rows, cols=cols)

if __name__ == '__main__':
	app.run(debug=True)