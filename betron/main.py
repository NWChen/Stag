import math
from Point import Point
from tkinter import *

def build_point(p, color='black', size=1):
	print(type(p.x), type(p.y))
	canvas.create_oval(p.x-size, p.y-size, p.x+size, p.y+size, fill=color, outline=color)

'''
def get_control_points(x0, y0, x1, y1, x2, y2, k):
	d1 = math.sqrt(math.pow(x1-x0, 2)+math.pow(y1-y0, 2))
	d2 = math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))
	kt1 = k*d1/(d1+d2) #scaling factor for triangle 1
	kt2 = k*d2/(d1+d2) #scaling factor for triangle 2
	t1x, t1y = kt1*(x2-x0), kt1*(y2-y0) #base, height of t1
	t2x, t2y = kt2*(x2-x0), kt2*(y2-y0) #base, height of t2
	cx0, cy0 = x1-t1x, y1-t1y #coordinates of c0
	cx1, cy1 = x2-t2x, y2-t2x #coordinates of c1
	return [cx0, cy0, cx1, cy1]
'''

def get_control_points(a, b, c, scaling_factor):
	d1 = math.sqrt(float(math.pow(a.x-b.x, 2)+math.pow(a.y-b.y, 2)))
	d2 = math.sqrt(float(math.pow(b.x-c.x, 2)+math.pow(b.y-c.y, 2)))
	t1 = (scaling_factor*d1)/float(d1+d2)
	t2 = (scaling_factor*d2)/float(d1+d2)
	r1 = Point(b.x-(t1*(c.x-a.x)), b.y-(t1*(c.y-a.y)))
	r2 = Point(b.x-(t2*(c.x-a.x)), b.y-(t2*(c.y-a.y)))
	build_point(r1, 'blue', 2)
	build_point(r2, 'blue', 2)
	return [r1, r2]

def find_control_points(s1, s2, s3):
       dx1 = s1.x - s2.x
       dy1 = s1.y - s2.y
       dx2 = s2.x - s3.x
       dy2 = s2.y - s3.y
       l1 = math.sqrt(dx1*dx1 + dy1*dy1)
       l2 = math.sqrt(dx2*dx2 + dy2*dy2)
       m1 = [(s1.x + s2.x) / 2.0, (s1.y + s2.y) / 2.0]
       m2 = [(s2.x + s3.x) / 2.0, (s2.y + s3.y) / 2.0]
       dxm = (m1[0] - m2[0])
       dym = (m1[1] - m2[1])
       k = l2 / (l1 + l2)
       cm = [m2[0] + dxm*k, m2[1] + dym*k]
       tx = s2.x - cm[0]
       ty = s2.y - cm[1]
       c1 = Point(m1[0] + tx, m1[1] + ty)
       c2 = Point(m2[0] + tx, m2[1] + ty)
       return [c1, c2]

'''
def get_bezier_coordinates(x0, y0, x1, y1, a0, b0, a1, b1, k):
	coordinates, x, y = [], 0, 0
	for t in range(0, k):
		t /= float(k)
		x = ((1-t)**3)*x0 + 3*t*((1-t)**2)*a0 + 3*(t**2)*(1-t)*a1 + (t**3)*x1
		y = ((1-t)**3)*y0 + 3*t*((1-t)**2)*b0 + 3*(t**2)*(1-t)*b1 + (t**3)*y1
		coordinates.append([x, y])
	return coordinates
'''

def get_bezier_coordinates(a, b, c1, c2, step):
	coordinates, x, y = [], 0, 0
	for t in range(0, step):
		t /= float(step)
		k = 1-t
		x = math.pow(k,3)*a.x + 3*t*math.pow(k,2)*c1.x + 3*k*math.pow(t,2)*c2.x + math.pow(t,3)*b.x
		y = math.pow(k,3)*a.y + 3*t*math.pow(k,2)*c1.y + 3*k*math.pow(t,2)*c2.y + math.pow(t,3)*b.y
		coordinates.append(Point(x, y))
		#coordinates.append(casteljau(a, c1, c2, b, step))
	return coordinates

def nCr(n, r):
	f = math.factorial
	return f(n)/f(r)/f(n-r)

gui = Tk()
width, height, bg = 800, 800, "white"
canvas = Canvas(gui, width=width, height=height, bg=bg)
canvas.grid(row=0, column=0)

#cp = get_control_points(100, 300, 200, 100, 300, 400, 1)
a, b, c, d = Point(320, 360), Point(300, 264), Point(450, 200), Point(500, 600)
build_point(a, 'red', 3)
build_point(b, 'red', 3)
build_point(c, 'red', 3)
build_point(d, 'red', 3)
#cp = get_control_points(a, b, c, 0.1)
#cp2 = get_control_points(b, c, d, 1)
cp = find_control_points(a, b, c)
cp2 = find_control_points(b, c, d)

for t in get_bezier_coordinates(a, b, cp[0], cp[1], 1000):
	build_point(t, 'black')
	print(t.x, t.y)

for t in get_bezier_coordinates(b, c, cp2[0], cp2[1], 1000):
	build_point(t, 'black')
	print(t.x, t.y)

gui.mainloop()