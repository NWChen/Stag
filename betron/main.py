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

def make_control_points(a, b, c, d, smooth_value=1):
	x0, y0 = a.x, a.y
	x1, y1 = b.x, b.y
	x2, y2 = c.x, c.y
	x3, y3 = d.x, d.y
	xc1 = (x0 + x1)/2.0 
	yc1 = (y0 + y1)/2.0 
	xc2 = (x1 + x2)/2.0 
	yc2 = (y1 + y2)/2.0 
	xc3 = (x2 + x3)/2.0 
	yc3 = (y2 + y3)/2.0 

	len1 = math.sqrt((x1-x0)*(x1-x0) + (y1-y0)*(y1-y0)) 
	len2 = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)) 
	len3 = math.sqrt((x3-x2)*(x3-x2) + (y3-y2)*(y3-y2)) 

	k1 = len1/(len1 + len2) 
	k2 = len2/(len2 + len3) 

	xm1 = xc1 + (xc2 - xc1)*k1 
	ym1 = yc1 + (yc2 - yc1)*k1 

	xm2 = xc2 + (xc3 - xc2)*k2 
	ym2 = yc2 + (yc3 - yc2)*k2 

	ctrl1_x = xm1 + (xc2 - xm1)*smooth_value + x1 - xm1
	ctrl1_y = ym1 + (yc2 - ym1)*smooth_value + y1 - ym1 
	ctrl2_x = xm2 + (xc2 - xm2)*smooth_value + x2 - xm2 
	ctrl2_y = ym2 + (yc2 - ym2)*smooth_value + y2 - ym2  

	c0, c1 = Point(ctrl1_x, ctrl1_y), Point(ctrl2_x, ctrl2_y)
	return [c0, c1]

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
a, b, c, d, e, f = Point(320, 360), Point(300, 264), Point(450, 200), Point(500, 600), Point(300, 600), Point(200, 590)
build_point(a, 'red', 3)
build_point(b, 'red', 3)
build_point(c, 'red', 3)
build_point(d, 'red', 3)
build_point(e, 'red', 3)
build_point(f, 'red', 3)

sf = 0.25
'''
cp = get_control_points(a, b, c, sf)
cp2 = get_control_points(b, c, d, sf)
cp3 = get_control_points(c, d, e, sf)
cp4 = get_control_points(d, e, f, sf)
cp = find_control_points(a, b, c)
cp2 = find_control_points(b, c, d)
cp3 = find_control_points(c, d, e)
cp4 = find_control_points(d, e, f)
'''
cp = make_control_points(a, a, b, c, sf)
cp2 = make_control_points(b, c, d, e, sf)
cp3 = make_control_points(c, d, e, f, sf)
cp4 = make_control_points(d, e, f, f, sf)

for t in get_bezier_coordinates(a, b, cp[0], cp[1], 100):
	build_point(t, 'black')
	print(t.x, t.y)

for t in get_bezier_coordinates(b, c, cp2[0], cp2[1], 100):
	build_point(t, 'black')
	print(t.x, t.y)

for t in get_bezier_coordinates(c, d, cp3[0], cp3[1], 100):
	build_point(t, 'black')
	print(t.x, t.y)

for t in get_bezier_coordinates(d, e, cp4[0], cp4[1], 100):
	build_point(t, 'black')
	print(t.x, t.y)

gui.mainloop()