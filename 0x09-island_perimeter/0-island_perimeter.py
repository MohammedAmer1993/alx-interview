#!/usr/bin/python3
''' function to calculate the primeter of the island asuming that
    there is know lakes inside the island
    the island is represented by 1 and the water is represented by 0
'''


def island_perimeter(grid):
    ''' calculate the priemeter of the island
    Args:
            grid: 2d array of int
            max size of the grid is 100 * 100
    Return: int
            the priemeter
    '''
    visitied_squares = []
    for i in range(len(grid)):
        for x in range(len(grid[i])):
            if grid[i][x] == 1:
                return rec(i, x, visitied_squares,
                           grid, len(grid) - 1, len(grid[i]) - 1)
    return 0


def rec(i, x, visited, grid, maxI, maxX):
    '''
    rec - recursive function to evaluate the area
    Args:
        i (int): the i coordinate
        x (int): the x coordinate
        visitiec: array of all visited points
        grid: the grid we are going throw
        maxI (int): the end of the grid in i direction
        maxX (int): the end of the grid in x direction
    Return:
        the priemeter of the island
    '''
    if [i, x] in visited:
        return 0
    else:
        res = 0
        visited.append([i, x])
        if i-1 >= 0:
            if grid[i-1][x] == 0:
                res += 1
            else:
                res += rec(i-1, x, visited, grid, maxI, maxX)
        else:
            res += 1
        if i+1 <= maxI:
            if grid[i+1][x] == 0:
                res += 1
            else:
                res += rec(i+1, x, visited, grid, maxI, maxX)
        else:
            res += 1
        if x-1 >= 0:
            if grid[i][x-1] == 0:
                res += 1
            else:
                res += rec(i, x-1, visited, grid, maxI, maxX)
        else:
            res += 1
        if x+1 <= maxX:
            if grid[i][x+1] == 0:
                res += 1
            else:
                res += rec(i, x+1, visited, grid, maxI, maxX)
        else:
            res += 1
    return res
