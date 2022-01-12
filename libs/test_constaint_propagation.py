import libs.ansi as ansi
import libs.constraint_propagation as constraint_propagation

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

def test_constraint_propagation():
    b = True

    b &= test_fill_grid()
    b &= test_get_row_values()
    b &= test_get_col_values()
    b &= test_get_block_values()

    if b:
        print(ansi.GREEN + "test_constraint_propagation : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_constraint_propagation : FAIL" + ansi.RESET)

    return b

def test_fill_grid():
    b = True
    m = dummy_valid_matrix

    grid = constraint_propagation.grid()
    grid.fill(m)
    n = grid.get_data()

    b &= m == n

    if b:
        print(ansi.GREEN + "test_constraint_propagation/fill_grid : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_constraint_propagation/fill_grid : FAIL" + ansi.RESET)

    return b

def test_get_row_values():
    m = dummy_valid_matrix

    grid = constraint_propagation.grid()
    grid.fill(m)

    valid_row = [5, 3, 4, 6, 7, 8, 9, 1, 2]

    b = valid_row == grid.get_row_values(0)

    if b:
        print(ansi.GREEN + "test_constraint_propagation/get_row_values : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_constraint_propagation/get_row_values : FAIL" + ansi.RESET)

    return b

def test_get_col_values():
    m = dummy_valid_matrix

    grid = constraint_propagation.grid()
    grid.fill(m)

    valid_col = [5, 6, 1, 8, 4, 7, 9, 2, 3]

    b = valid_col == grid.get_column_values(0)

    if b:
        print(ansi.GREEN + "test_constraint_propagation/get_col_values : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_constraint_propagation/get_col_values : FAIL" + ansi.RESET)

    return b

def test_get_block_values():
    m = dummy_valid_matrix

    grid = constraint_propagation.grid()
    grid.fill(m)

    valid_block = [5, 3, 4, 6, 7, 2, 1, 9, 8]
    
    b = valid_block == grid.get_block_values((0, 0))

    if b:
        print(ansi.GREEN + "test_constraint_propagation/get_block_values : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_constraint_propagation/get_block_values : FAIL" + ansi.RESET)

    return b