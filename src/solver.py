import os
import time

import numpy as np

from src.possible import is_possible


def print_grid(grid, title="Sudoku"):
    os.system(
        "cls" if os.name == "nt" else "clear"
    )  # Clear the console (Windows uses 'cls', Unix-based uses 'clear')
    print(title)
    print(np.matrix(grid))
    # for row in grid:
    # print(" ".join(str(cell) if cell != 0 else "." for cell in row))
    print()


def solver_once(grid):

    possibilities = []
    old_grid = grid

    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if is_possible(n, y, x, grid):
                        possibilities.append(n)

                if len(possibilities) == 1:

                    grid[y][x] = possibilities[0]

                    # print_grid(grid)
                    # time.sleep(0.1)
                    solver_once(grid)
                    #    return True
                    # print_grid(grid)
                    # time.sleep(0.1)
                    grid[y][x] = 0
                possibilities = []
                # return
    if np.any(grid == 0) and old_grid.all() != grid.all():
        # print_grid(grid)
        solver_once(grid)
    elif old_grid.all() == grid.all():
        solver(grid)
    return True

    # plot_grid(grid, ax, fig, title="Solved Sudoku"


def solver(grid):

    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if is_possible(n, y, x, grid):
                        grid[y][x] = n
                        # print_grid(grid)
                        # time.sleep(0.1)
                        if solver(grid):
                            return True
                        # print_grid(grid)
                        # time.sleep(0.1)
                        grid[y][x] = 0
                return

    return True
