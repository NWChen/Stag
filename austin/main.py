from Tkinter import *

class App:

	def __init__(self, tk):
		self.tk = tk
		self.tk.bind('<Motion>', self.motion)
		self.tk.bind('<Button-1>', self.click)
		self.canvas = Canvas(self.tk, width=1000, height=1000, cursor="crosshair", bg="white")
		self.canvas.pack()
		self.x = 0
		self.y = 0

	def motion(self, event):
		self.x = event.x
		self.y = event.y
		print self.x, self.y

	def click(self, event):
		self.canvas.create_rectangle()

	def mainloop(self):
		tk.mainloop()

tk = Tk()
app = App(tk)
app.mainloop()