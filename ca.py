import tkinter as tk
import random


CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
DELAY = 100

class CellularAutomata(tk.Canvas):
    def __init__(self, master):
        width = GRID_WIDTH * CELL_SIZE
        height = GRID_HEIGHT * CELL_SIZE
        super().__init__(master, width=width, height=height, bg="white")
        self.pack()

        self.grid = [[random.choide([0, 1]) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

        self.draw_grid()
        self.after(DELAY, self.update_automaton)

    def draw_grid(self):
        self.delete("all")

        for x in range(0, GRID_WIDTH * CELL_SIZE, CELL_SIZE):
            self.create_line(x, 0, x, GRID_HEIGHT * CELL_SIZE, fill="gray")
        for y in range(0, GRID_HEIGHT * CELL_SIZE, CELL_SIZE):
            self.create_line(0, y, GRID_WIDTH * CELL_SIZE, y, fill="gray")

        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if self.grid[row][col] == 1:
                    self.create_rectangle(
                        col * CELL_SIZE, row * CELL_SIZE,
                        (col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE,
                        fill="black"
                    )
    
    def update_automaton(self):
        new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                alive_neighbors = sum(
                    self.grid[(row + i) % GRID_HEIGHT][(col + j) % GRID_WIDTH]
                    for i in (-1, 0, 1) for j in (-1, 0, 1)
                    if not (i == 0 and j == 0)
                )

                if self.grid[row][col] == 1:
                    if alive_neighbors in (2, 3):
                        new_grid[row][col] = 1
                    else:
                        new_grid[row][col] = 0
                else:
                    if alive_neighbors == 3:
                        new_grid[row][col] = 1

        self.grid = new_grid
        self.draw_grid()
        self.after(DELAY, self.update_automaton)

root = tk.Tk()
root.title("Cellular Automata")
automaton = CellularAutomata(root)
root.mainloop()