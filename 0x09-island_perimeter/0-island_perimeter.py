#!/usr/bin/python3
"""
island_perimeter function that returns the perimeter of
the island described in grid
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Assume all four sides are exposed
                perimeter += 4

                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1

                # Check bottom neighbor
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1

                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1

                # Check right neighbor
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter
