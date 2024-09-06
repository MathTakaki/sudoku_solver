#####################################################
# this code check if is possible to fit a number in #
# a given location on the grid                      #
#                                                   #
# input:                                            #
#   n: int from(1 to 9)                             #
#   y: int position y on the grid                   #
#   x: int position x on the grid                   #
#####################################################


def is_possible(n, y, x, grid):

    for i in range(0, 9):
        if grid[y][i] == n:
            return False
        if grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True
