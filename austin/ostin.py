from Tkinter import *
from Point import Point
from Segment import Segment
import math

class App:

	#constructor
	def __init__(self, tk):
		self.tk = tk
		
		self.tk.bind('<Motion>', self.motion)
		
		self.size = 1000
		self.canvas = Canvas(self.tk, width=self.size, height=self.size, cursor="crosshair", bg="white")
		self.canvas.bind('<Button-1>', self.canvas_click)
		self.canvas.grid(row=0, column=0)

		self.listbox = Listbox(tk, selectmode=SINGLE)
		self.listbox.grid(row=0, column=1)
		self.listbox.bind('<Double-Button-1>', self.listbox_click)
		self.scrollbar = Scrollbar(tk)
		self.scrollbar.grid(row=0, column=2)
		self.listbox.config(yscrollcommand=self.scrollbar.set)
		self.scrollbar.config(command=self.listbox.yview)
		self.delete_buttons = []

		self.tag = 0
		self.x = 0
		self.y = 0
		self.num_waypoints = 0
		self.points = []
		self.segments = []

	#callback when mouse moves
	def motion(self, event):
		self.x = event.x
		self.y = event.y

	#callback when left mouse button clicked
	def canvas_click(self, event): 
		self.add_point(Point(self.x, self.y, self.canvas))

	#highlight a point
	def highlight(self, point):
		bound = 8
		circle = self.canvas.create_oval(point.x-bound, point.y-bound, point.x+bound, point.y+bound, outline='red', width=bound/4)
		self.canvas.itemconfig(circle, tags=(str(self.tag)))

	#callback when left mouse button clicked
	def listbox_click(self, event):
		click_index = map(int, self.listbox.curselection())
		if(len(click_index)>0):
			if self.points[click_index[0]].selected == False:
				#draw bounding circle
				self.points[click_index[0]].selected = True
				self.highlight(self.points[click_index[0]])
				self.tag += 1
			else:
				self.points[click_index[0]].selected = False
				self.delete_point(self.points[click_index[0]], self.tag)
				self.tag -= 1

	#add a Point to the canvas and points list
	def add_point(self, point):
		radius = 3
		self.canvas.create_oval(self.x-radius, self.y-radius, self.x+radius, self.y+radius, fill="black")
		self.points.append(point)
		self.listbox.insert(END, str(point))
		self.num_waypoints += 1
		self.build_segments()

	#delete a Point
	def delete_point(self, point, tag):
		self.canvas.delete(str(tag))
		self.points.remove(point)
		self.listbox.delete(0, END)
		for point in self.points:
			self.listbox.insert(END, str(point))

	#segments
	def build_segments(self):
		self.canvas.delete("segments")
		for i in range(0, len(self.points)-1):
			self.segments.append(Segment(self.points[i], self.points[i+1]))
		for segment in self.segments:
			self.canvas.create_line(segment.x1, segment.y1, segment.x2, segment.y2, fill="gray", width=3, tags="segments")

	#tags
	def get_point_tag(self):
		return "POINT_" + str(self.point_tag)

	def get_highlight_tag(self):
		return "HIGHLIGHT_" + str(self.highlight_tag)

	#main function
	def mainloop(self):
		tk.mainloop()

tk = Tk()
app = App(tk)
app.mainloop()