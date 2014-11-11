from Point import Point

class Derivative(Point):

	def __init__(self, dy, dx, magnitude=1):
		self.dy = dy
		self.dx = dx
		self.magnitude = magnitude