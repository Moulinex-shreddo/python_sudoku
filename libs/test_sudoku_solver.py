from libs.sudoku import *
from libs.solver import *
import libs.ansi as ansi

dummy_matrix = generate_empty_data()
dummy_matrix[0][0] = 1

# Returns True if all sudoku_solver unit tests are PASS, False, otherwise
def test_sudoku_solver():
    b = True

    b &= test_valid_number()
    b &= test_invalid_row()
    b &= test_invalid_col()
    b &= test_invalid_block()

    if b:
        print(ansi.GREEN + "test_sudoku_solver : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_sudoku_solver : FAIL" + ansi.RESET)

    return b


# Returns True if we can add a valid number in the cell, False otherwise
def test_valid_number():
    b = is_number_valid(dummy_matrix, 5, (1, 1))

    if b:
        print(ansi.GREEN + "test_sudoku_solver/valid_number : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_sudoku_solver/valid_number : FAIL" + ansi.RESET)

    return b

# Returns True if we fail to add an invalid number in a row, False otherwise
def test_invalid_row():
    b = not is_number_valid(dummy_matrix, 1, (0, 5))

    if b:
        print(ansi.GREEN + "test_sudoku_solver/invalid_row : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_sudoku_solver/invalid_row : FAIL" + ansi.RESET)

    return b

# Returns True if we fail to add an invalid number in a column, False otherwise
def test_invalid_col():
    b = not is_number_valid(dummy_matrix, 1, (5, 0))

    if b:
        print(ansi.GREEN + "test_sudoku_solver/invalid_col : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_sudoku_solver/invalid_col : FAIL" + ansi.RESET)

    return b

# Returns True if we fail to add an invalid number in a block, False otherwise
def test_invalid_block():
    b = not is_number_valid(dummy_matrix, 1, (1, 1))

    if b:
        print(ansi.GREEN + "test_sudoku_solver/invalid_block : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_sudoku_solver/invalid_block : FAIL" + ansi.RESET)

    return b
