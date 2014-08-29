from Tkinter import *
from Waypoint import Waypoint
from Segment import Segment
import math

class App:

	#constructor
	def __init__(self, tk):
		self.tk = tk
		
		self.tk.bind('<Motion>', self.motion)
		
		self.size = 500
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

		self.x = 0
		self.y = 0
		self.waypoints = []
		self.outlines = []
		self.segments = []
		self.waypoint_tag = "w0"
		self.outline_tag = "o0"

	#callback when mouse moves
	def motion(self, event):
		self.x = event.x
		self.y = event.y

	#callback when left mouse button clicked
	def canvas_click(self, event): 
		self.add_waypoint(Waypoint(self.x, self.y, self.canvas))

	#outline a point
	def gen_outline(self, point):
		bound = 8
		circle = self.canvas.create_oval(point.x-bound, point.y-bound, point.x+bound, point.y+bound, outline='red', width=bound/4)
		self.canvas.itemconfig(circle, tags=(self.gen_outline_tag()))

	#callback when left mouse button clicked
	def listbox_click(self, event):
		click_index = map(int, self.listbox.curselection())
		if(len(click_index)>0):
			if self.waypoints[click_index[0]].selected == False:
				self.waypoints[click_index[0]].selected = True
				self.gen_outline(self.waypoints[click_index[0]])
			else:
				self.waypoints[click_index[0]].selected = False
				self.canvas.delete(self.outlines[click_index[0]])
				self.outlines.remove(self.outlines[click_index[0]]) 
				#delete outline

	#add a Waypoint to the canvas and points list
	def add_waypoint(self, waypoint):
		RADIUS = 3
		dot = self.canvas.create_oval(self.x-RADIUS, self.y-RADIUS, self.x+RADIUS, self.y+RADIUS, fill="black")
		waypoint.tag = self.gen_waypoint_tag()
		self.canvas.itemconfig(dot, tags=waypoint.tag)
		self.waypoints.append(waypoint)
		self.listbox.insert(END, str(waypoint))
		self.build_segments()

	#delete a Waypoint
	def delete_point(self, waypoint):
		self.canvas.delete(self.point_tag)
		self.points.remove(waypoint)
		self.listbox.delete(0, END)
		for point in self.points:
			self.listbox.insert(END, str(point))

	#segments
	def build_segments(self):
		self.canvas.delete("segments")
		for i in range(0, len(self.waypoints)-1):
			self.segments.append(Segment(self.waypoints[i], self.waypoints[i+1]))
		for segment in self.segments:
			self.canvas.create_line(segment.x1, segment.y1, segment.x2, segment.y2, fill="gray", width=3, tags="segments")

	#build a waypoint tag
	def gen_waypoint_tag(self):
		tag = "w" + str(int(self.waypoint_tag[1:])+1)
		self.outlines.append(tag)
		return tag

	#build an outline tag
	def gen_outline_tag(self):
		return "o" + str(int(self.outline_tag[1:])+1)

	#main function
	def mainloop(self):
		tk.mainloop()

tk = Tk()
app = App(tk)
app.mainloop()