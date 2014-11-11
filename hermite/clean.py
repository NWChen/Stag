import math
import time
from Derivative import Derivative
from Point import Point
from tkinter import *

def build_point(p, color='black', size=1):
	canvas.create_oval(p.x-size, height-(p.y-size), p.x+size, height-(p.y+size), fill=color, outline=color)

def cubic_interpolate(p1, p2, t1, t2, steps):
	for t in range(0, steps):
		s = t/float(steps)
		h1 = 2*s*s*s - 3*s*s + 1
		h2 = -2*s*s*s + 3*s*s
		h3 = s*s*s - 2*s*s + s
		h4 = s*s*s - s*s
		p = Point(h1*p1.x + h2*p2.x + h3*t1.dx + h4*t2.dx,
			h1*p1.y + h2*p2.y + h3*t1.dy + h4*t2.dy)
		build_point(p)
	return

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

def build_tangent(p, slope, color='black'):
	x = p.x
	y = (slope/500)*x + (height-p.y)
	x, y = x+100, y-100
	canvas.create_line(p.x, p.y, x, y)

gui = Tk()
width, height, bg = 800, 800, "white"
canvas = Canvas(gui, width=width, height=height, bg=bg)
canvas.grid(row=0, column=0)

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
	cubic_interpolate(Point(300, 400), Point(600, 400), Derivative(-1000, x), Derivative(0, 1000), 100)
	build_tangent(Point(300, 400), x)
	canvas.after(15)
	canvas.update()
	canvas.delete("all")

gui.mainloop()
