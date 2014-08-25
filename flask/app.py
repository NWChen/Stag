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
from flask import Flask, redirect, url_for, session, jsonify, request, render_template
from Point import Point
from Segment import Segment

points = []
segments = []
app = Flask(__name__)

def segmentize():
	segments = []
	for index in range(0, len(points)-1):
		segments.append(Segment(points[index], points[index+1]))

@app.route('/add_point')
def add_point():
	global point_index
	x = request.args.get('row', 0, type=int)
	y = request.args.get('col', 0, type=int)
	points.append(Point(x, y))
	segmentize()
	return jsonify(result='add (' + str(x) + ', ' + str(y) + ')') #find adjacents and add to segments

@app.route('/remove_point')
def remove_point():
	x = request.args.get('row', 0, type=int)
	y = request.args.get('col', 0, type=int)
	for point in points:
		if point.x==x and point.y==y:
			points.remove(point)
	segmentize()
	return jsonify(result='remove (' + str(x) + ', ' + str(y) + ')')

@app.route('/')
def build_grid():
	rows, cols = [], []
	for i in xrange(0, 20):
		rows.append(i+1)
		cols.append(i+1)
	return render_template("index.html", rows=rows, cols=cols)

if __name__ == '__main__':
	app.run(debug=True)