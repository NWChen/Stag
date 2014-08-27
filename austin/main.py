from Tkinter import *

gui = Tk()

def callback():
	print 'click'

def build_grid(grid_size, cell_size):
	grid = []
	for row in range(0, grid_size):
		grid.append([])
		for column in range(0, grid_size):
			grid[row].append(Button(gui, bg="#dadfe1", relief=FLAT, height=cell_size/2, width=cell_size, command=callback))
			grid[row][-1].grid(row=row+1, column=column+1, padx=1, pady=1)

build_grid(20, 6)
mainloop()