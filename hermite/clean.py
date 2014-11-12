import math
import time
from Derivative import Derivative
from Point import Point
from tkinter import *

#draw a point
def build_point(p, color='black', size=1):
	canvas.create_oval(p.x-size, height-(p.y-size), p.x+size, height-(p.y+size), fill=color, outline=color)

#draw the tangent line at a given point
def build_tangent(p, derivative, color='black'):
	x1, x2 = p.x + derivative.dx, p.x - derivative.dx
	y1, y2 = height-(p.y + derivative.dy), height-(p.y - derivative.dy)
	canvas.create_line(p.x, height-p.y, x1, y1, fill=color)
	canvas.create_line(p.x, height-p.y, x2, y2, fill=color)
	return

#converts a vector to a derivative
def convert_to_derivative(angle, magnitude):
	angle = (angle*math.pi)/180
	y = magnitude*math.sin(angle)
	x = magnitude*math.cos(angle)
	return Derivative(y, x)

#interpolate a cubic hermite spline
def cubic_interpolate(p1, p2, t1, t2, steps):
	sequence = []
	for t in range(0, steps):
		s = t/float(steps)
		h1 = 2*s*s*s - 3*s*s + 1
		h2 = -2*s*s*s + 3*s*s
		h3 = s*s*s - 2*s*s + s
		h4 = s*s*s - s*s
		p = Point(h1*p1.x + h2*p2.x + h3*t1.dx + h4*t2.dx, 
			h1*p1.y + h2*p2.y + h3*t1.dy + h4*t2.dy)
		sequence.append(p)
	return sequence

#interpolate a quintic hermite spline
def quintic_interpolate(p1, p2, d1, d2, dd1, dd2, steps):
	for t in range(0, steps):
		s = t/float(steps)
		h0 = 1-(10*math.pow(s,2))+(15*math.pow(t,4))-(6*math.pow(t,5))
		h1 = s-(6*math.pow(s,3))+(8*math.pow(s,4))-(3*math.pow(s,5))
		h2 = (0.5*math.pow(s,2))-(1.5*math.pow(s,3))+(1.5*math.pow(s,4))-(0.5*math.pow(t,5))
		h3 = (0.5*math.pow(s,3))-(math.pow(s,4))+(0.5*math.pow(s,5))
		h4 = (-4*math.pow(s,3))+(7*math.pow(s,4))-(3*math.pow(s,5))
		h5 = (10*math.pow(s,3))-(15*math.pow(s,4))+(6*math.pow(s,5))
		p = Point(h0*p1.x + h1*d1)
		#Finish this up
	return

#draw a sequence of points
def draw_sequence(sequence, color="black"):
	for p in sequence:
		build_point(p, color)
	return

#offset a curve to be parallel to the base curve
def offset_cubic(sequence, offset):
	output_sequence, s = [], 0
	for step in range(0, len(sequence)-1):
		s = step/float(len(sequence))
		p = sequence[step]
		build_tangent(p, n_derive(sequence, step), 'blue')
	return output_sequence

#differentiate at a step using predetermined points
def derive(sequence, step):
	if(len(sequence)<2): 
		return 0
	dx, dy = sequence[step+1].x-sequence[step].x, sequence[step+1].y-sequence[step].y
	print(dy, dx)
	return Derivative(dy*10, dx*10)

#find the normal to the derivative
def n_derive(sequence, step):
	if(len(sequence)<2):
		return 0
	dydx = derive(sequence, step)
	return Derivative(-dydx.dx*10, dydx.dy*10)

gui = Tk()
width, height, bg = 800, 800, "white"
canvas = Canvas(gui, width=width, height=height, bg=bg)
canvas.grid(row=0, column=0)

a, b, c = Point(300, 200), Point(300, 500), Point(200, 500)
ta, tb, tc = [200, 400], [400, 600], [135, 500]
build_point(a, 'red', 3)
build_point(b, 'red', 3)
build_point(c, 'red', 3)
build_tangent(a, convert_to_derivative(ta[0], ta[1]), 'red')
build_tangent(b, convert_to_derivative(tb[0], tb[1]), 'green')
build_tangent(c, convert_to_derivative(tc[0], tc[1]), 'blue')

draw_sequence(cubic_interpolate(a, b, convert_to_derivative(ta[0], ta[1]), convert_to_derivative(tb[0], tb[1]), 100))
draw_sequence(cubic_interpolate(b, c, convert_to_derivative(tb[0], tb[1]), convert_to_derivative(tc[0], tc[0]), 100))
offset_cubic(cubic_interpolate(a, b, convert_to_derivative(ta[0], ta[1]), convert_to_derivative(tb[0], tb[1]), 100), 10)
offset_cubic(cubic_interpolate(b, c, convert_to_derivative(tb[0], tb[1]), convert_to_derivative(tc[0], tc[0]), 100), 10)

gui.mainloop()
