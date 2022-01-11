import libs.brute_force as brute_force
import libs.constraint_propagation as constraint_propagation
from libs.sudoku import *

# Returns a solution of the given 9x9 matrix, 0-filled matrix if there is no solution
def solve(m):
    if brute_force.solve(m):
        return m

    return generate_empty_data(9)

# Returns True if the matrix describes a solvable Sudoku and False if not
def is_solvable(m):
    # Make a copy of the matrix to not solve it, for this is not this function's purpose
    n = m
    return constraint_propagation.solve(n)

# Returns True is the matrix describes a Sudoku with multiple possible solutions and False if not
def has_multiple_solutions(m):
    if 1:
        return True
    return False

# Returns True if the number n can be placed in the cell of the Sudoku represented by the 9x9 matrix m
def is_number_valid(m, n, cell):
    # Check row
    for i in range(len(m[0])):
        if m[cell[0]][i] == n and cell[1] != i:
            return False

    # Check column
    for i in range(len(m[1])):
        if m[i][cell[1]] == n and cell[0] != i:
            return False

    #Check block
    b = (cell[0] // 3, cell[1] // 3)

    for i in range(b[0] * 3, b[0] * 3 + 3):
        for j in range(b[1] * 3, b[1] * 3 + 3):
            if m[i][j] == n and (i, j) != cell:
                return False

    return True

# Returns True if the 9x9 matrix represents a solved sudoku, False otherwise
def is_grid_valid(m):
    for x in range(len(m[0])):
        for y in range(len(m[1])):
            if not is_number_valid(m, m[x][y], (x, y)):
                return False
                
    return True