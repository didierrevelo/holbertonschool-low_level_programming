#!/usr/bin/python3
"""
    Create a function def island_perimeter(grid):
    that returns the perimeter of the island described in grid:

grid is a list of list of integers:
0 represents a water zone
1 represents a land zone
One cell is a square with side length 1
Grid cells are connected horizontally/vertically (not diagonally).
Grid is rectangular, width and height don’t exceed 100
Grid is completely surrounded by water, and there is one island (or nothing).
The island doesn’t have “lakes”
(water inside that isn’t connected to the water around the island).
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    perimeter = 0
    if grid is None or len(grid) == 0 or len(grid[0]) == 0:
        return perimeter
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 and grid[i][j] == 1:
                perimeter += 1
            if j == 0 and grid[i][j] == 1:
                perimeter += 1
            if j == len(grid[0]) - 1 and grid[i][j] == 1:
                perimeter += 1
            if i == len(grid) - 1 and grid[i][j] == 1:
                perimeter += 1
            if i != len(grid) - 1 and grid[i][j] == 1 and grid[i + 1][j] == 0:
                perimeter += 1
            if i != 0 and grid[i][j] == 1 and grid[i - 1][j] == 0:
                perimeter += 1
            if j != len(grid[i]) - 1 and grid[i][j] == 1\
            and grid[i][j + 1] == 0:
                perimeter += 1
            if j != 0 and grid[i][j] == 1 and grid[i][j - 1] == 0:
                perimeter += 1
            if j == 100:
                break
        if i == 100:
            break
    return perimeter
