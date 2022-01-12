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