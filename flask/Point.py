class Point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __repr__(self):
		reeturn str(self.x) + '_' + str(self.y)