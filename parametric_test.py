from Tkinter import *
import math

gui = Tk()

canvas = Canvas(gui, width=400, height=400, bg="white")
canvas.pack()
x, y = 0, 0

for t in range(0, 30):
	t /= float(5)
	x = 100*math.sin(t)+200
	y = 100*math.cos(t)+200
	print x, y
	canvas.create_oval(x-2, y-2, x+2, y+2, fill='black', outline='black')

gui.mainloop()