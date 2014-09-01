from Tkinter import *
import math

gui = Tk()

width, height, bg = 400, 400, "white"
circle = Canvas(gui, width=width, height=height, bg=bg)
circle.grid(row=0, column=0)
cubic = Canvas(gui, width=width, height=height, bg=bg)
cubic.grid(row=0, column=1)
bezier = Canvas(gui, width=width, height=height, bg=bg)
bezier.grid(row=1, column=0)
casteljau = Canvas(gui, width=width, height=height, bg=bg)
casteljau.grid(row=1, column=1)
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
	build_line(circle, x, y, xb, yb)

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

#cubic bezier curve using de Casteljau's
for t in range(0, 1000):
	x, y = 0, 0
	t /= float(999)
	#starting, ending
	coords = [[10, 10], [390, 390]]
	Px = (1-t)*coords[0][0] + t*coords[1][0]
	Py = (1-t)*coords[0][1] + t*coords[1][1]
	build_point(casteljau, Px, Py)

#inefficient! recursive interpolation
def casteljau(p0, p1, p2, t):
	pFinal = []


gui.mainloop()