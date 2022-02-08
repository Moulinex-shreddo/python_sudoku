import sys

import libs.config as config
import libs.solver as solver
import libs.lcg as lcg

# Returns True if the matrix could be solved with brute_force algorithm, False otherwise.
def solve(m):
    return recursive_solve(m)

# recursive_solve is a separate function for clarity purpose.
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
                # the actual configuration and we need to backtrack.
                return False

    return solver.is_grid_valid(m)

# Returns a randomly generated grid.
# It's more or less the same algorithm as the brute_force solver on an empty grid (and randomly applied).
def generate():
    m = solver.generate_empty_data(9)

    # Recursive generation algorithm.
    recursive_generate(m)
    #recursive_remove_cells(m)

    # Iterative generation algorithm.
    #iterative_generate(m)
    iterative_remove_cells(m)

    return m

# Recursively generates a sudoku grid.
def recursive_generate(m):
    # This algorithm exceeds recursion stack limit so we first need to increase it a bit.
    sys.setrecursionlimit(5000)

    while not solver.is_grid_filled(m):
        # We need to make copies of every randomly generated number in order to check if we iterate over every possible cell/value per cell.
        x = lcg.randrange_light(0, 9)
        y = 1 # y is not randomly generated, this would slow the algorithm down by too much.
        s = coordinates(x, y)

        # Looking for an empty cell to fill, starting from a random one.
        while m[s._x][s._y] != 0:
            
            s._x += 1
            if s._x == 9:
                s._x = 0
                s._y = s._y + 1

                if s._y == 9:
                    s._y = 0

        r = lcg.randrange_light(1, 9)
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
                i = 1
            
            if i == r:
                return False

    return solver.is_grid_valid(m)

# Removes random cells, but keeps the sudoku grid solvable.
def recursive_remove_cells(m):
    sys.setrecursionlimit(5000)

    while solver.is_solvable(m):
        x = lcg.randrange_light(0, 9)
        y = lcg.randrange_light(0, 9)
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


# Iteratively generates a sudoku grid, keeping stack size reasonable.
def iterative_generate(m):
    # This lifo will be stocked in the heap, so we will not have stack overflow.
    lifo = []
    while not solver.is_grid_filled(m):
        x = lcg.randrange_light(0, 9)
        y = lcg.randrange_light(0, 9)

        # Looking for an empty cell to fill, starting from a random one.
        while m[x][y] != 0:
            
            x += 1
            if x == 9:
                x = 0
                y = y + 1

                if y == 9:
                    y = 0

        r = lcg.randrange_light(1, 9)
        c = cell_possibilities(x, y, r, r)

        # There is no default LIFO class in Python so we will simulate it with an array.
        # We always insert data at index 0 and pop index 0 whenever we need to remove it.
        lifo.insert(0, c)

        while True:
            if solver.is_number_valid(m, lifo[0]._i, (lifo[0]._x, lifo[0]._y)):
                m[lifo[0]._x][lifo[0]._y] = lifo[0]._i
                print(m)
                break

            while True:
                lifo[0]._i += 1

                if lifo[0]._i == 10:
                    lifo[0]._i = 1

                if lifo[0]._i == lifo[0]._r:
                    m[lifo[0]._x][lifo[0]._y] = 0
                    lifo.pop(0)
                else:
                    break

    return solver.is_grid_valid(m)

# Removes random cells, but keeps the sudoku grid solvable.
# Iterative algorith keeps stack size reasonable.
def iterative_remove_cells(m):
    difficulty = config.get_difficulty()
    i = 0
    s = coordinates(lcg.randrange_light(0, 9), lcg.randrange_light(0, 9))

    while difficulty > 0:
        while solver.is_solvable(m):
            while m[s._x][s._y] == 0:
                s._x = lcg.randrange_light(0, 9)
                s._y = lcg.randrange_light(0, 9)

            i = m[s._x][s._y]
            m[s._x][s._y] = 0
    
        m[s._x][s._y] = i
        difficulty -= 1

    return solver.is_solvable(m)

# We need a class here because tuples are not mutable and structures do not exist.
class coordinates:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

# We need another class for the iterative generation algorithm, again, because tuples are not mutable.
class cell_possibilities:
    def __init__(self, x, y, r, i) -> None:
        self._x = x
        self._y = y
        self._r = r
        self._i = i