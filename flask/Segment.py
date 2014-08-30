class Segment(object):
	def __init__(self, a=None, b=None):
		self.a = a
		self.b = b
		self.x1 = a.x
		self.y1 = a.y
		self.x2 = b.x
		self.y2 = b.y

	def __eq__(self, other):
		return self.a==other.a and self.b==other.b

	def __repr__(self):
		return "<Segment>: %s, %s" % (self.a, self.b)

	def __str__(self):
		return "%s, %s" % (self.a, self.b)