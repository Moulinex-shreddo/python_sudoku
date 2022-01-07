import libs.solver as solver

# 9x9 matrix filled with 0
def generate_empty_data():
    return [[0 for i in range(9)] for j in range(9)]

# 9x9 matrix containing a sudoku
def generate_sudoku():
    m = [[0 for i in range(9)] for j in range(9)]


class sudoku:
    def __init__(self):
        # Generate 9x9 empty matrix
        self._complete = generate_empty_data()
        self._partial = self.hide(self._complete)

    # Returns the generated 9x9 matrix
    def complete(self):
        return self._complete

    # Returns the partially hidden 9x9 matrix (may be modified by the user)
    def partial(self):
        return self._partial