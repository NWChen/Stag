from Tkinter import *
from Point import Point

class App:

	def __init__(self, tk):
		self.tk = tk
		self.tk.bind('<Motion>', self.motion)
		self.tk.bind('<Button-1>', self.click)
		self.canvas = Canvas(self.tk, width=1000, height=1000, cursor="crosshair", bg="white")
		self.canvas.pack()
		self.x = 0
		self.y = 0
		self.num_waypoints = 0
		self.points = []

	def motion(self, event):
		self.x = event.x
		self.y = event.y
		print self.x, self.y

	def click(self, event):
		self.add_point(self.x, self.y)

	def add_point(self, x, y):
		point = Point(self.x, self.y, self.canvas)
		self.num_waypoints += 1

	def delete_point(self, x, y):
		for point in points:
			if x==point.x and y==point.y:
				points.remove(point)

	def mainloop(self):
		tk.mainloop()

tk = Tk()
app = App(tk)
app.mainloop()