class Waypoint(object):
	def __init__(self, x=0, y=0, selected=False, tag=None):
		self.x = x
		self.y = y
		self.selected = selected
		self.tag = tag
 
	def __repr__(self):
		return "<Point>: (%s,%s)" % (str(self.x), str(self.y))

	def __str__(self):
		return "(%s,%s)" % (str(self.x), str(self.y))

