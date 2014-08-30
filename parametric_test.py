from Tkinter import *
import math

gui = Tk()

circle = Canvas(gui, width=400, height=400, bg="white")
circle.pack(side=LEFT)
cubic = Canvas(gui, width=400, height=400, bg="white")
cubic.pack(side=RIGHT)
x, y = 0, 0

def nCr(n, r):
	f = math.factorial
	return f(n)/f(r)/f(n-r)

#circle based on {x=sin(t), y=cos(t)}
for t in range(0, 31):
	t /= float(5)
	x = 100*math.sin(t)+200
	y = 100*math.cos(t)+200
	circle.create_oval(x-2, y-2, x+2, y+2, fill='black', outline='black')

#parametric cubic bezier curve
for t in range(0, 31):
	t /= float(5)

	#starting, control 1, control 2, ending
	coords = [[120, 160], [35, 200], [220, 260], [220, 40]]

	for i in range(0, 4):
		x += nCr(3, i) * coords[i][0] * ((1-t)**(3-i))
		y += nCr(3, i) * coords[i][1] * ((1-t)**(3-i)) 
		print x, y

	x, y = 0, 0

	cubic.create_oval(x-2, y-2, x+2, y+2, fill='black', outline='black')

gui.mainloop()