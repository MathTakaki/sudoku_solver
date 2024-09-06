import numpy as np

from src.possible import is_possible


def solver(grid):

    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if is_possible(n, y, x, grid):
                        grid[y][x] = n
                        solver(grid)
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
