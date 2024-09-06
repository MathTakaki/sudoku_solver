import os
import time

import numpy as np

from src.possible import is_possible


def print_grid(grid, title="Sudoku"):
    os.system(
        "cls" if os.name == "nt" else "clear"
    )  # Clear the console (Windows uses 'cls', Unix-based uses 'clear')
    print(title)
    for row in grid:
        print(" ".join(str(cell) if cell != 0 else "." for cell in row))
    print()


def solver(grid):

    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if is_possible(n, y, x, grid):
                        grid[y][x] = n
                        print_grid(grid)
                        # time.sleep(0.1)
                        if solver(grid):
                            return True
                        print_grid(grid)
                        # time.sleep(0.1)
                        grid[y][x] = 0
                return
    return True

    # plot_grid(grid, ax, fig, title="Solved Sudoku")
