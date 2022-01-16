import sys
import time

import libs.solver as solver
import libs.sudoku as sudoku

# Returns True if the matrix could be solved with brute_force algorithm, False otherwise
def solve(m):
    return recursive_solve(m)

# recursive_solve is a separate function for clarity purpose
def recursive_solve(m):

    for x in range(len(m[0])):
        for y in range(len(m[1])):
            if m[x][y] == 0:

                for i in range(1, 10): # Python range does not include last element
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
    sys.setrecursionlimit(1500)
    m = sudoku.generate_empty_data(9)

    recursive_generate(m)

    return m

# Recursively generates a sudoku grid
def recursive_generate(m):
    while not solver.is_grid_filled(m):
        # We need to make copies of every randomly generated number in order to check if we iterate over every possible cell/value per cell
        x = randrange(0, 9)
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

        r = randrange(1, 10)
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

# We need our own random generating number function because the random python module is not that good
# Returns a integer between a and b, b excluded
def randrange(a, b):
    return time.time_ns()%b + a

# We need a class here because tuples are not mutable and structures do not exist
class coordinates:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y