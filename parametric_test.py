from Tkinter import *
import math

gui = Tk()

canvas = Canvas(gui, width=100, height=100, bg="white")
canvas.pack()

for t in range(0, 7):
	x = 100*math.sin(t)
	y = 100*math.cos(t)
	print x, y
	canvas.create_oval(x-2, y-2, x+2, y+2, outline='red')

gui.mainloop()