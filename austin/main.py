from Tkinter import *


gui = Tk()

class App:
	def __init__(self, parent):
		self.tk = parent

	def callback(self):
		print 'click'

	def build_grid(self, grid_size, cell_size):
		grid = []
		for row in range(0, grid_size):
			grid.append([])
			for column in range(0, grid_size):
				grid[row].append(Button(self.tk, bg="#dadfe1", activebackground="#2d2d2d", relief=FLAT, height=cell_size/2, width=cell_size, command=self.callback))
				grid[row][-1].bind('<Button-1>', self.click(grid[row][-1]))
				grid[row][-1].grid(row=row, column=column, padx=1, pady=1)

	def click(self, event):
		if self.button['bg']=="#dadfe1":
			button.configure(bg="#000000")
		else:
			button.configure(bg="#dadfe1")

app = App(gui)
app.build_grid(20, 6)
mainloop()