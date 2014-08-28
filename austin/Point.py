class Point(object):
	def __init__(self, x=0, y=0, canvas=None, radius=6):
		self.x = x
		self.y = y
		if(canvas!=None): 
			self.dot = canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="black")
			
	def __repr__(self):
		return "<Point>: (%s,%s)" % (str(self.x), str(self.y))

	def __str__(self):
		return "(%s,%s)" % (str(self.x), str(self.y))
