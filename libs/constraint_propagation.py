import libs.solver as solver
import libs.sudoku as sudoku

def generate_empty_data(type, n):
    return [[type() for i in range(n)] for j in range(n)]

# Returns True if the constraint propagation algorithm could resolve the grid, False otherwise
def solve(m):
    sudoku = grid()
    sudoku.fill(m)

    j = 2
    # Let j = 2 so that each constraint has the time to propagate over the full grid
    while j > 0:
        for x in range(0, 9):
            for y in range(0, 9):
                if sudoku.get_cell_data((x, y)) == 0:
                    c = sudoku._data[x // 3][y // 3]._data[x % 3][y % 3]
                    for i in c._candidates:
                        if i in sudoku.get_column_values(y) or i in sudoku.get_row_values(x) or i in sudoku.get_block_values((x // 3, y //3)):
                            c._candidates.remove(i)
                            j += 1
                
                    if len(c._candidates) == 1:
                        c._data = c._candidates[0]

        j -= 1

    m = sudoku.get_data()
    return solver.is_grid_valid(m)

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

    def get_row_values(self, r):
        row = []
        for i in range(0, 9):
            row.append(self.get_cell_data((r, i)))
          
        return row

    def get_column_values(self, c):
        col = []
        for i in range(0, 9):
            col.append(self.get_cell_data((i, c)))

        return col

    def get_block_values(self, b):
        r = []
        for i in range(0, 3):
            for j in range(0, 3):
                r.append(self._data[b[0]][b[1]].get_cell_data((i, j)))

        return r

    
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
        if i != 0:
            self._candidates = [i]

    def get_data(self):
        return self._data