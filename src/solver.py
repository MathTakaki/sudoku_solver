import matplotlib.pyplot as plt
import numpy as np

from src.possible import is_possible


def init_plot():
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.matshow(np.ones((9, 9)) * -1, cmap="Greys", vmin=-1, vmax=1)

    # Draw grid lines
    for i in range(10):
        lw = 1.5 if i % 3 == 0 else 0.5
        ax.axhline(i - 0.5, color="black", lw=lw)
        ax.axvline(i - 0.5, color="black", lw=lw)

    return fig, ax


def plot_grid(grid, ax, fig, title="Sudoku"):
    ax.clear()  # Clear the previous plot
    ax.matshow(np.ones_like(grid) * -1, cmap="Greys", vmin=-1, vmax=1)

    # Draw grid lines
    for i in range(10):
        lw = 1.5 if i % 3 == 0 else 0.5
        ax.axhline(i - 0.5, color="black", lw=lw)
        ax.axvline(i - 0.5, color="black", lw=lw)

    # Add numbers to the grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                ax.text(j, i, str(grid[i][j]), va="center", ha="center", fontsize=14)

    plt.title(title)
    plt.gca().invert_yaxis()
    plt.draw()  # Update the plot
    plt.pause(0.001)  # Pause to make sure the plot updates


def solver(grid, ax, fig):

    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if is_possible(n, y, x, grid):
                        grid[y][x] = n
                        # plot_grid(grid, ax, fig, title=f"Placing {n} at ({y}, {x})")
                        solver(grid, ax, fig)
                        # plot_grid(grid, ax, fig, title=f"Placing {n} at ({y}, {x})")
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    # plot_grid(grid, ax, fig, title="Solved Sudoku")
