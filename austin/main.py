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
		self.canvas.pack()
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
		temp = self.get_nearest_point(self.x, self.y)
		print("nearest: ", temp.x, temp.y)
		self.add_point(self.x, self.y)

	#radar scan for closest point
	def get_nearest_point(self, x, y):
		for scan_radius in range(0, self.size):
			for theta in range(0, 361):
				radian = float(theta)*math.pi/180
				for point in self.points:
					x2 = x+(scan_radius*math.cos(radian))
					y2 = y+(scan_radius*math.sin(radian))
					if abs(point.x-x2)<=1 and abs(point.y-y2)<=1:
						return point
		return Point(-1, -1)

	#add a Point to the canvas and points list
	def add_point(self, x, y):
		point = Point(self.x, self.y, self.canvas)
		self.points.append(point)
		self.num_waypoints += 1

	#delete a Point from the canvas and points list
	def delete_point(self):
		for point in self.points:
			if self.x==point.x and self.y==point.y:
				print "shit done"
				self.canvas.delete(point.dot)
				self.points.remove(point)

	#main function
	def mainloop(self):
		tk.mainloop()

tk = Tk()
app = App(tk)
app.mainloop()