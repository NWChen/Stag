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
		self.inCanvas = True

		self.listbox = Listbox(tk, selectmode=SINGLE)
		self.listbox.grid(row=0, column=1)
		self.scrollbar = Scrollbar(tk)
		self.scrollbar.grid(row=0, column=2)
		self.listbox.config(yscrollcommand=self.scrollbar.set)
		self.scrollbar.config(command=self.listbox.yview)

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
		self.add_point(Point(self.x, self.y, self.canvas))

	#add a Point to the canvas and points list
	def add_point(self, point):
		self.points.append(point)
		self.listbox.insert(END, str(point))
		self.num_waypoints += 1

	#delete a Point
	def delete_point(self, point):
		self.points.remove(point)
		#self.listbox.delete()

	#main function
	def mainloop(self):
		tk.mainloop()

tk = Tk()
app = App(tk)
app.mainloop()