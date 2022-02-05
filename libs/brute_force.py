from pydoc import doc
import sys

import libs.solver as solver
import libs.lcg as lcg

# Returns True if the matrix could be solved with brute_force algorithm, False otherwise
def solve(m):
    return recursive_solve(m)

# recursive_solve is a separate function for clarity purpose
def recursive_solve(m):

    for x in range(len(m[0])):
        for y in range(len(m[1])):
            if m[x][y] == 0:

                for i in range(1, 10):
                    if solver.is_number_valid(m, i, (x, y)):
                        m[x][y] = i
                        if recursive_solve(m):
                            return True
                        else:
                            m[x][y] = 0

                # If no valid number was found for (x, y) cell, then the sudoku is not solvable with
                # the actual configuration and we need to backtrack
                return False

    return solver.is_grid_valid(m)

# Returns a randomly generated grid
# It's more or less the same algorithm as the brute_force solver on an empty grid (and randomly applied)
def generate():
    m = solver.generate_empty_data(9)

    # Recursive generation algorithm is deprecated since it overflows C stack.
    # Uncomment if you want to toy with stack overflows.
    recursive_generate(m)
    #recursive_remove_cells(m)
    #iterative_remove_cells(m)

    return m

# Recursively generates a sudoku grid.
def recursive_generate(m):
    # This algorithm exceeds recursion stack limit so we first need to increase it a bit.
    # This will eventually lead to stack overflow.
    sys.setrecursionlimit(5000)

    while not solver.is_grid_filled(m):
        # We need to make copies of every randomly generated number in order to check if we iterate over every possible cell/value per cell
        x = lcg.randrange(0, 9)
        y = 1 # y is not randomly generated, this would slow the algorithm down by too much
        s = coordinates(x, y)

        # Looking for an empty cell to fill, starting from a random one
        while m[s._x][s._y] != 0:
            
            s._x += 1
            if s._x == 9:
                s._x = 0
                s._y = s._y + 1

                if s._y == 9:
                    s._y = 0

        r = lcg.randrange(1, 9)
        i = r
        while True:
            if solver.is_number_valid(m, i, (s._x, s._y)):
                m[s._x][s._y] = i
                if recursive_generate(m):
                    return True
                else:
                    m[s._x][s._y] = 0

            i += 1
            if i == 10:
                i = 0
            
            if i == r:
                return False

    return solver.is_grid_valid(m)

# Removes random cells, but keeps the sudoku grid solvable.
# Recursive remove_cells algorithm overflows C stack (Python virtual machine runs C code).
def recursive_remove_cells(m):

    while solver.is_solvable(m):
        x = lcg.randrange(0, 9)
        y = lcg.randrange2(0, 9)
        s = coordinates(x, y)

        while m[s._x][s._y] == 0:
            s._x += 1
            if s._x == 9:
                s._x = 0
                s._y = s._y + 1

                if s._y == 9:
                    s._y = 0

        i = m[s._x][s._y]
        m[s._x][s._y] = 0

        if recursive_remove_cells(m):
            return True
        else:
            m[s._x][s._y] = i
            return solver.is_solvable(m)

    return solver.is_solvable(m)

# Removes random cells, but keeps the sudoku grid solvable.
# Iterative algorith keeps stack size reasonable
def iterative_remove_cells(m):
    i = 0
    s = coordinates(lcg.randrange(0, 9), lcg.randrange2(0, 9))

    while solver.is_solvable(m):
        while m[s._x][s._y] == 0:
            s._x = lcg.randrange(0, 9)
            s._y = lcg.randrange2(0, 9)

        i = m[s._x][s._y]
        m[s._x][s._y] = 0
    
    m[s._x][s._y] = i

    return solver.is_solvable(m)

# We need a class here because tuples are not mutable and structures do not exist
class coordinates:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y