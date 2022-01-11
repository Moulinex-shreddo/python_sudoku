from libs.sudoku import *
from libs.solver import *
from libs.brute_force import *
from libs.constraint_propagation import *
import libs.ansi as ansi

dummy_matrix = generate_empty_data(9)
dummy_matrix[0][0] = 1

dummy_valid_matrix = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

dummy_unsolved_matrix = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Returns True if all sudoku_solver unit tests are PASS, False, otherwise
def test_sudoku_solver():
    b = True

    b &= test_valid_number()
    b &= test_invalid_row()
    b &= test_invalid_col()
    b &= test_invalid_block()
    b &= test_valid_grid()
    b &= test_invalid_grid()
    b &= test_brute_force_solver()
    b &= test_constaint_propagation_solver()

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

# Returns True if we can valid the dummy_valid_grid, False otherwise
def test_valid_grid():
    b = is_grid_valid(dummy_valid_matrix)

    if b:
        print(ansi.GREEN + "test_sudoku_solver/valid_grid : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_sudoku_solver/valid_grid : FAIL" + ansi.RESET)

    return b

# Returns True if we fail to valid an invalid grid, False otherwise
def test_invalid_grid():
    m = dummy_valid_matrix
    m[0][0] = 3

    b = not is_grid_valid(m)

    if b:
        print(ansi.GREEN + "test_sudoku_solver/invalid_grid : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_sudoku_solver/invalid_grid : FAIL" + ansi.RESET)

    return b

# Returns True if the brute_force algorithm finds a solution to the unsolved matrix, False otherwise
def test_brute_force_solver():
    # Copy the matrix before because we need it unsolved for other unit tests
    m = dummy_unsolved_matrix
    b = brute_force.solve(m)

    if b:
        print(ansi.GREEN + "test_sudoku_solver/brute_force_solver : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_sudoku_solver/brute_force_solver : FAIL" + ansi.RESET)

    return b

# Returns True if the constraint_propagation algorithm finds a solution to the unsolved matrix, False otherwise
def test_constaint_propagation_solver():
    m = dummy_unsolved_matrix
    b = constraint_propagation.solve(m)

    if b:
        print(ansi.GREEN + "test_sudoku_solver/constraint_propagation_solver : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_sudoku_solver/constraint_propagation_solver : FAIL" + ansi.RED)

    return b