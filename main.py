import matplotlib.pyplot as plt
import numpy as np

from src.solver import solver, solver_once


def main():
    grid = np.array(
        [
            [0, 0, 0, 0, 2, 0, 0, 0, 7],
            [9, 0, 0, 6, 0, 0, 0, 0, 0],
            [0, 4, 0, 0, 0, 9, 1, 0, 8],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 8, 0, 1, 0, 0, 6, 0, 0],
            [0, 0, 0, 0, 4, 0, 5, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 3, 5, 0, 2, 0, 4],
            [3, 7, 9, 0, 0, 2, 0, 0, 0],
        ]
    )

    if solver_once(grid):
        print("Sudoku solved:")
        print(np.matrix(grid))
    else:
        print("No solution exists.")


if __name__ == "__main__":
    main()
