import libs.solver as solver
import libs.sudoku as sudoku

def generate_empty_data(type, n):
    return [[type() for i in range(n)] for j in range(n)]

# Returns True if the constraint propagation algorithm could resolve the grid, False otherwise
def solve(m):
    return False

class grid:
    def __init__(self):
        self._data = generate_empty_data(block, 3)

    def fill(self, m):
        for x in range(len(m[0])):
            for y in range(len(m[1])):
                i = m[x][y]
                self.fill_cell(i, (x, y))

    def fill_cell(self, i, c):
        b = (c[0] // 3, c[1] // 3)
        c = (c[0] % 3, c[1] % 3)

        self._data[b[0]][b[1]].fill(i, c)

    def get_data(self):
        return [[self.get_cell_data((x, y)) for y in range (0, 9)] for x in range (0, 9)]

    def get_cell_data(self, c):
        b = (c[0] // 3, c[1] // 3)
        c = (c[0] % 3, c[1] % 3)

        return self._data[b[0]][b[1]].get_cell_data(c)
    

class block:
    def __init__(self):
        self._data = generate_empty_data(cell, 3)

    def fill(self, i, c):
        self._data[c[0]][c[1]].fill(i)

    def get_cell_data(self, c):
        return self._data[c[0]][c[1]].get_data()
        

class cell:
    def __init__(self):
        self._data = 0
        self._candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def fill(self, i):
        self._data = i
        self._candidates = 0

    def get_data(self):
        return self._data