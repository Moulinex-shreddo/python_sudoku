import libs.solver as solver
import libs.sudoku as sudoku

def generate_empty_data(type, n):
    return [[type for i in range(n)] for j in range(n)]

# Returns True if the constraint propagation algorithm could resolve the grid, False otherwise
def solve(m):
    return False

class grid:
    def __init__(self, m):
        self._data = generate_empty_data(block, 3)

    def fill(self, i, c):
        #b = 
        c = (c(0) // 3, c(1) // 3)

        self._data[block(0)][block(1)].fill(i)

class block:
    def __init__(self):
        self._data = generate_empty_data(cell, 3)

    def fill(self, i, c):
        self._data[cell(0)][cell(1)].fill(i)

class cell:
    def __init__(self):
        self._data = 0
        self._candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def fill(self, i):
        self._data = i
        self._candidates = 0