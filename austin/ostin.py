from Tkinter import *
from Point import Point
import math

class App:

	#constructor
	def __init__(self, tk):
		self.tk = tk
		
		self.tk.bind('<Motion>', self.motion)
		self.tk.bind('<Button-1>', self.click)
		
		self.size = 1000
		self.canvas = Canvas(self.tk, width=self.size, height=self.size, cursor="crosshair", bg="white")
		self.canvas.grid(row=0, column=0)
		
		self.

		self.x = 0
		self.y = 0
		self.num_waypoints = 0
		self.points = []

	#callback when mouse moves
	def motion(self, event):
		self.x = event.x
		self.y = event.y
		print(self.x, self.y)

	#callback when left mouse button clicked
	def click(self, event):
		self.add_point(self.x, self.y)

	#add a Point to the canvas and points list
	def add_point(self, x, y):
		point = Point(self.x, self.y, self.canvas)
		self.points.append(point)
		self.num_waypoints += 1

	#main function
	def mainloop(self):
		tk.mainloop()

tk = Tk()
app = App(tk)
app.mainloop()