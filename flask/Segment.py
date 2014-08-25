class Segment(object):
	def __init__(self, Point a=None, Point b=None):
		self.a = a
		self.b = b
		self.x1 = a.x
		self.y1 = a.y
		self.x2 = b.x
		self.y2 = b.y
