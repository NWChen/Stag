import math
import time
from Point import Point
from tkinter import *

def build_point(p, color='black', size=1):
	canvas.create_oval(p.x-size, height-(p.y-size), p.x+size, height-(p.y+size), fill=color, outline=color)

def build_curve(p1, p2, t1, t2, steps):
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
	if x>2000:
		up = False
	elif x<-2000:
		up = True
	print(x)
	build_curve(Point(300, 400), Point(400, 400), x, 500, 100)
	canvas.after(20)
	canvas.update()
	canvas.delete("all")

gui.mainloop()
