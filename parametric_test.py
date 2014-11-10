from Point import Point
from tkinter import *
import math

gui = Tk()

width, height, bg = 400, 400, "white"
circle = Canvas(gui, width=width, height=height, bg=bg)
circle.grid(row=0, column=0)
cubic = Canvas(gui, width=width, height=height, bg=bg)
cubic.grid(row=0, column=1)
bezier = Canvas(gui, width=width, height=height, bg=bg)
bezier.grid(row=1, column=0)
castel = Canvas(gui, width=width, height=height, bg=bg)
castel.grid(row=1, column=1)
x, y = 0, 0
xb, yb = 0, 0

def build_point(canvas, x, y):
	canvas.create_oval(x-2, y-2, x+2, y+2, fill='black', outline='black')

def build_line(canvas, x1, y1, x2, y2):
	canvas.create_line(x1, y2, x2, y2, fill="gray", width=3)

def nCr(n, r):
	f = math.factorial
	return f(n)/f(r)/f(n-r)

#circle based on {x=sin(t), y=cos(t)}
for t in range(0, 7000):
	xb, yb = x, y
	t /= float(999)
	x = 100*math.sin(t)+200
	y = 100*math.cos(t)+200
	build_point(circle, x, y)
	#build_line(circle, x, y, xb, yb)

#parametric cubic bezier curve
for t in range(0, 1000):
	x, y = 0, 0
	t /= float(999)
	#starting, control 1, control 2, ending
	coords = [[120, 160], [35, 200], [220, 260], [220, 40]]
	for i in range(0, 4):
		x += nCr(3, i) * coords[i][0] * ((1-t)**(3-i)) * (t**i)
		y += nCr(3, i) * coords[i][1] * ((1-t)**(3-i)) * (t**i)
	build_point(cubic, x, y)

#hardcoded bezier curve
for t in range(0, 1000):
	x, y = 0, 0
	t /= float(999)
	x = (120*(1-t)**3) + (35*3*t*(1-t)**2) + (220*3*(t**2)*(1-t)) + (220*(t**3))
	y = (160*(1-t)**3) + (200*3*t*(1-t)**2) + (260*3*(t**2)*(1-t)) + (40*(t**3))
	build_point(bezier, x, y)

'''
#cubic bezier curve using de Casteljau's
for t in range(0, 1000):
	x, y = 0, 0
	t /= float(999)
	#starting, ending
	coords = [[10, 10], [390, 390]]
	Px = (1-t)*coords[0][0] + t*coords[1][0]
	Py = (1-t)*coords[0][1] + t*coords[1][1]
	build_point(casteljau, Px, Py)
'''

#LERP
def lerp(a, b, c, t):
	c.x = a.x + (b.x-a.x)*t #0<=t<=1; certain point on x axis
	c.y = a.y + (b.y-a.y)*t #0<=t<=1; certain point on y axis

'''
	*B
*--------------*
A              D
		*C
'''

#linear interpolation, de Casteljau's
def casteljau(a, b, c, d, C, t):
	ab, bc, cd, abbc, bccd = Point(), Point(), Point(), Point(), Point() #multiple assignment to same variable apparently is assignment by reference, so this is necessary
	lerp(a, b, ab, t)
	lerp(b, c, bc, t)
	lerp(c, d, cd, t)
	lerp(ab, bc, abbc, t)
	lerp(bc, cd, bccd, t)
	lerp(abbc, bccd, C, t)

def main():
	a, b, c, d = Point(120, 160), Point(35, 200), Point(220, 260), Point(220, 40)
	for i in range(0, 1000):
		t = float(i)/999
		p = Point()
		casteljau(a, b, c, d, p, t)
		build_point(castel, p.x, p.y)
		#print p.x, p.y

castel.bind('<Button-1>', main())
gui.mainloop()