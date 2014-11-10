import math
import time
from Point import Point
from tkinter import *

def build_point(p, color='black', size=1):
	canvas.create_oval(p.x-size, height-(p.y-size), p.x+size, height-(p.y+size), fill=color, outline=color)

def cubic_interpolate(p1, p2, t1, t2, steps):
	for t in range(0, steps):
		s = t/float(steps)
		h1 = (2*math.pow(s,3.0)) - (3*math.pow(s,2)) + 1
		h2 = (-2*math.pow(s,3)) + (3*math.pow(s,2))
		h3 = (math.pow(s,3)) - (2*math.pow(s,2)) + s
		h4 = (math.pow(s,3)) - (math.pow(s,2))
		p = Point(h1*p1.x + h2*p2.x + h3*t1 + h4*t2,
			h1*p1.y + h2*p2.y + h3*t1 + h4*t2)
		build_point(p)
	return

def quintic_interpolate(p1, p2, t1, t2, steps):
	for t in range(0, steps):
		s = t/float(steps)
		h0 = 1-(10*math.pow(s,2))+(15*math.pow(t,4))-(6*math.pow(t,5))
		h1 = s-(6*math.pow(s,3)+(8*math.pow(s,4))-(3*math.pow(s,5))
		h2 = (0.5*math.pow(s,2))-(1.5*math.pow(s,3))+(1.5*math.pow(s,4))-(0.5*math.pow(t,5))
		h3 = (0.5*math.pow(s,3))-(math.pow(s,4))+(0.5*math.pow(s,5))
		h4 = (-4*math.pow(s,3))+(7*math.pow(s,4))-(3*math.pow(s,5))
		h5 = (10*math.pow(s,3))-(15*math.pow(s,4))+(6*math.pow(s,5))

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
	if x>500:
		up = False
	elif x<-500:
		up = True
	cubic_interpolate(Point(300, 400), Point(400, 400), x, 0, 100)
	build_tangent(Point(300, 400), x)
	canvas.after(60)
	canvas.update()
	canvas.delete("all")

gui.mainloop()
