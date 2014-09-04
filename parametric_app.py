from Point import Point
from Tkinter import *
import math

'''
	*B
*--------------*
A              D
		*C
'''

class App(object):

	def __init__(self, gui):
		self.gui = gui
		self.points = []

	#LERP
	def lerp(self, a, b, c, t):
		c.x = a.x + (b.x-a.x)*t #0<=t<=1; certain point on x axis
		c.y = a.y + (b.y-a.y)*t #0<=t<=1; certain point on y axis

	#linear interpolation, de Casteljau's
	def casteljau(self, a, b, c, d, C, t):
		ab = bc = cd = abbc = bccd = Point()
		self.lerp(a, b, ab, t)
		self.lerp(b, c, bc, t)
		self.lerp(c, d, cd, t)
		self.lerp(ab, bc, abbc, t)
		self.lerp(bc, cd, bccd, t)
		self.lerp(abbc, bccd, C, t)

	def main(self):
		a, b, c, d = Point(120, 160), Point(35, 200), Point(220, 260), Point(220, 40)
		for i in range(0, 1000):
			t = float(i)/999
			p = Point()
			casteljau(a, b, c, d, p, t)
			#build_point(casteljau, p.x, p.y)
			print p.x, p.y

	def mainloop(self):
		gui.mainloop()

tk = Tk()
app = App(tk)
app.mainloop()