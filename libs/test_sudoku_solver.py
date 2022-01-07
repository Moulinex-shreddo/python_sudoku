from libs.sudoku import *
from libs.solver import *

dummy_matrix = generate_empty_data()
dummy_matrix[0][0] = 1

# Returns True if all sudoku_solver unit tests are PASS, False, otherwise
def test_sudoku_solver():
    b = (test_valid_number()
    and test_invalid_row()
    and test_invalid_col()
    and test_invalid_block())

    if b:
        print("test_sudoku_solver : PASS")
    else:
        print("test_sudoku_solver : FAIL")

    return b


# Returns True if we can add a valid number in the cell, False otherwise
def test_valid_number():
    b = is_number_valid(dummy_matrix, 1, (1, 1))

    if b:
        print("test_sudoku_solver/valid_number : PASS")
    else:
        print("test_sudoku_solver/valid_number : FAIL")
    
    return b

# Returns True if we fail to add an invalid number in a row, False otherwise
def test_invalid_row():
    b = is_number_valid(dummy_matrix, 1, (0, 10))

    if not b:
        print("test_sudoku_solver/invalid_row : PASS")
    else:
        print("test_sudoku_solver/invalid_row : FAIL")
    
    return not b

# Returns True if we fail to add an invalid number in a column, False otherwise
def test_invalid_col():
    b = is_number_valid(dummy_matrix, 1, (10, 0))

    if not b:
        print("test_sudoku_solver/invalid_col : PASS")
    else:
        print("test_sudoku_solver/invalid_col : FAIL")

    return not b

# Returns True if we fail to add an invalid number in a block, False otherwise
def test_invalid_block():
    b = is_number_valid(dummy_matrix, 1, (1, 1))

    if not b:
        print("test_sudoku_solver/invalid_block : PASS")
    else:
        print("test_sudoku_solver/invalid_block : FAIL")
    
    return not b
