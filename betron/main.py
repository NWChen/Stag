import math

def getControlPoints(x0, y0, x1, y1, x2, y2, k):
	d1 = math.sqrt(math.pow(x1-x0, 2)+math.pow(y1-y0, 2))
	d2 = math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))
	kt1 = k*d1/(d1+d2) #scaling factor for triangle 1
	kt2 = k*d2/(d1+d2) #scaling factor for triangle 2
	t1x, t1y = kt1*(x2-x0), kt1*(y2-y0) #base, height of t1
	t2x, t2y = kt2*(x2-x0), kt2*(y2-y0) #base, height of t2
	x0, y0 = x1-t1x, y1-t1y #coordinates of c0
	x1, y1 = x2-t2x, y2-t2x #coordinates of c1
	return [x0, y0, x1, y1]
