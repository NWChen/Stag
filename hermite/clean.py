import math
import time
from Derivative import Derivative
from Point import Point
from tkinter import *

main_sequence = []

#draw a point
def build_point(p, color='black', size=1):
	canvas.create_oval(p.x-size, height-(p.y-size), p.x+size, height-(p.y+size), fill=color, outline=color)

#draw the tangent line at a given point
def build_tangent(p, derivative, color='black'):
	x = p.x + derivative.dx
	y = height-(p.y + derivative.dy)
	canvas.create_line(p.x, height-p.y, x, y, fill=color)
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

#find the slope of the line tangent to a cubic spline at a given point
def derive(p, s):
	x = p.x*(6*s*s - 6*s + 1)
	y = p.y*(6*s*s - 6*s + 1)
	return Derivative(x, y)

'''
#derive using 2 consecutive points
def rough_derive(sequence, step):
	if(len(sequence)<2):
		return 0
	else:
		return Derivative(sequence[step+1].y-sequence[step].y, sequence[step+1].x-sequence[step].x)
'''

#draw a sequence of points
def draw_sequence(sequence, color="black"):
	for p in sequence:
		build_point(p, color)
	return

#offset a curve to be parallel to the base curve
def offset_cubic(p1, sequence, offset):
	output_sequence, s = [], 0
	for step in range(0, len(sequence)):
		s = step/float(len(sequence))
		p = sequence[step]
		f = p1.x*(2*s*s*s - 3*s*s + s + 1)
		fp = p1.x*(6*s*s - 6*s + 1)
		g = p1.y*(2*s*s*s - 3*s*s + s + 1)
		gp = p1.y*(6*s*s - 6*s + 1)
		x = f+((offset*gp)/math.sqrt(fp*fp + gp*gp))
		#xdown = f-((offset*gp)/math.sqrt(fp*fp + gp*gp))
		y = g+((offset*fp)/math.sqrt(fp*fp + gp*gp))
		#ydown = g-((offset*fp)/math.sqrt(fp*fp + gp*gp))
		output_sequence.append(Point(x, y))
		print(x, y)
	return output_sequence

gui = Tk()
width, height, bg = 800, 800, "white"
canvas = Canvas(gui, width=width, height=height, bg=bg)
canvas.grid(row=0, column=0)

a, b, c = Point(300, 200), Point(600, 300), Point(200, 500)
ta, tb, tc = [60, 800], [40, 1000], [90, 500]
build_point(a, 'red', 3)
build_point(b, 'red', 3)
build_point(c, 'red', 3)
#build_tangent(a, convert_to_derivative(ta[0], ta[1]), 'red')
build_tangent(b, convert_to_derivative(tb[0], tb[1]), 'green')
build_tangent(c, convert_to_derivative(tc[0], tc[1]), 'blue')
s=0

main_sequence.extend(cubic_interpolate(a, b, convert_to_derivative(ta[0], ta[1]), convert_to_derivative(tb[0], tb[1]), 1000))
main_sequence.extend(cubic_interpolate(b, c, convert_to_derivative(tb[0], tb[1]), convert_to_derivative(tc[0], tc[0]), 1000))

draw_sequence(main_sequence)

'''
x, up = 0, True
while(True):
	if up==True:
		x += 10
	else:
		x -= 10
	if x>200:
		up = False
	elif x<(-200):
		up = True
	dx, dy = x, x
	a, b = Point(300, 400), Point(600, 400)
	cubic_interpolate(a, b, convert_to_derivative(a, b, 100), Derivative(0, 1000), 100)
	#build_tangent(a, convert_to_derivative(a, b, 90), 'red')
	canvas.after(60)
	canvas.update()
	canvas.delete("all")
'''

gui.mainloop()
