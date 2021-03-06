import math
from Point import Point
from tkinter import *
from Vector import Vector

points, current_point = [], -1
total_sequence = []
clicked, x, y = False, -1, -1

def click(event):
	global clicked, x, y
	clicked, x, y = True, event.x, event.y

def drag(event):
	global clicked, x, y, canvas, line_to_cursor
	#build_line(Point(x, y), Point(event.x, event.y))
	canvas.coords(line_to_cursor, x, y, event.x, event.y)
	canvas.coords(line_to_cursor_origin, x-2, y-2, x+2, y+2)

def release(event):
	bb = 10
	global x, y, points, current_point, velocity
	points.append(Vector(Point(x, y), Point(event.x, event.y)))
	if len(points)>1:
		current_point += 1
		a, b = points[current_point].start, points[current_point+1].start
		at, bt = points[current_point], points[current_point+1]
		draw(interpolate(a, b, at, bt, 100))
		#draw(offset(interpolate(a, b, at, bt, 250), 30), "red")
		#draw(offset(interpolate(a, b, at, bt, 250), -30), "red")
		print(current_point)

	for i in range(0, len(total_sequence)-1):
		point = total_sequence[i]
		dx, dy = total_sequence[i+1].x-total_sequence[i].x, total_sequence[i+1].y-total_sequence[i].y
		speed = str('%.2f'%math.sqrt(dx*dx+dy*dy))
		velocity.config(text=speed+" ft/s")
		canvas.coords(robot, point.x-bb, point.y-bb, point.x+bb, point.y+bb)
		canvas.after(10)
		canvas.update()
	

def build_point(p, color="black", size=1, shape="circle"):
	if shape=="rectangle":
		canvas.create_rectangle(p.x-size, p.y-size, p.x+size, p.y+size, fill=color, outline=color)
	canvas.create_oval(p.x-size, p.y-size, p.x+size, p.y+size, fill=color, outline=color)

def build_line(p, _p, color="blue"):
	canvas.create_line(p.x, p.y, _p.x, _p.y, fill=color)

def interpolate(p1, p2, t1, t2, steps):
	global total_sequence
	sequence = []
	for t in range(0, steps):
		s = t/float(steps)
		h1 = 2*s*s*s - 3*s*s + 1
		h2 = -2*s*s*s + 3*s*s
		h3 = s*s*s - 2*s*s + s
		h4 = s*s*s - s*s
		p = Point(h1*p1.x + h2*p2.x + h3*(t1.end.x-t1.start.x) + h4*(t2.end.x-t2.start.x),
			h1*p1.y + h2*p2.y + h3*(t1.end.y-t1.start.y) + h4*(t2.end.y-t2.start.y))
		sequence.append(p)
		total_sequence.append(p)
	return sequence

def offset(sequence, k):
	k_sequence = []
	for t in range(0, len(sequence)-1):
		s = t/float(len(sequence))
		f, g = sequence[t].x, sequence[t].y
		fp, gp = sequence[t+1].x, sequence[t+1].y
		x, y = f + (k*gp)/math.sqrt(fp*fp + gp*gp), g - (k*fp)/math.sqrt(fp*fp + gp*gp)
		k_sequence.append(Point(x, y))
	return k_sequence

def bad_offset(sequence, k):
	k_sequence = []
	for t in range(0, len(sequence)-1):
		dy = sequence[t+1].y - sequence[t].y
		dx = sequence[t+1].x - sequence[t].x
		if math.sin(math.atan(float(dy)/dx)) < 0:
			#inside is  
			return
		a, b = sequence[t].x, sequence[t].y
		x = (sequence[t].x+sequence[t+1].x)/2
		y = math.sqrt(k*k - (x-a)*(x-a)) + b
		k_sequence.append(Point(x, y))
	return k_sequence

def draw(sequence, color="black"):
	for point in sequence:
		build_point(point, color)

gui = Tk()
width, height, bg = 2000, 1000, "white"
canvas = Canvas(gui, width=width, height=height, bg=bg)
canvas.grid(row=0, column=0)
label = Label(canvas, text="spline path builder for robots", fg="white", bg="#121212", font=("Montserrat",20))
label2 = Label(canvas, text="FRC Team 2601", fg="white", bg="#E74C3C", font=("Lato",15))
velocity = Label(canvas, text="0 ft/s", fg="black", bg="white", font=("Lato", 24))
label.pack()
label2.pack()
velocity.pack()
canvas.create_window(1000, 20, window=label)
canvas.create_window(1000, 55, window=label2)
canvas.create_window(width-200, 100, window=velocity)

line_to_cursor_origin = canvas.create_rectangle(-1, -1, -1, -1, fill="red", outline="red")
line_to_cursor = canvas.create_line(-1, -1, -1, -1)
robot = canvas.create_rectangle(-1, -1, -1, -1, fill="green", outline="black")
gui.bind('<Button-1>', click)
gui.bind('<B1-Motion>', drag)
gui.bind('<ButtonRelease-1>', release)

'''
a, b, c = Point(300, 200), Point(600, 400), Point(200, 700)
_a, _b, _c = Point(800, 800), Point(800, 800), Point(800, 800)
at, bt, ct = Vector(a, _a), Vector(b, _b), Vector(c, _c)
resolution = 50

draw(interpolate(a, b, at, bt, resolution))
draw(interpolate(b, c, bt, ct, resolution))

k_offset = 20
draw(offset(interpolate(a, b, at, bt, resolution), k_offset), "red")
draw(offset(interpolate(a, b, at, bt, resolution), -k_offset), "red")
draw(offset(interpolate(b, c, bt, ct, resolution), k_offset), "red")
draw(offset(interpolate(b, c, bt, ct, resolution), -k_offset), "red")
build_point(a, "red", 3, "rectangle")
build_point(b, "red", 3, "rectangle")
build_point(c, "red", 3, "rectangle")
canvas.create_line(a.x, a.y, _a.x, _a.y, fill="blue")
canvas.create_line(b.x, b.y, _b.x, _b.y, fill="blue")
canvas.create_line(c.x, c.y, _c.x, _c.y, fill="blue")
'''

gui.mainloop()
