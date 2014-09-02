'''
	*B
*--------------*
A              D
		*C
'''

#linear interpolation, de Casteljau's
def casteljau(a, b, c, d, C, t):
	ab = bc = cd = abbc = bccd = Point()
	lerp(a, b, ab, t)
	lerp(b, c, bc, t)
	lerp(c, d, cd, t)
	lerp(ab, bc, abbc, t)
	lerp(bc, cd, bccd, t)
	lerp(abbc, bccd, C, t)

def main():
	a, b, c, d = Point(120, 160), Point(35, 200), Point(220, 260), Point(220, 40)
	for i in range(0, 1000):
		t = float(i)/999
		p = Point()
		casteljau(a, b, c, d, p, t)
		build_point(casteljau, p.x, p.y)
		print p.x, p.y