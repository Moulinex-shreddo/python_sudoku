import libs.ansi as ansi
import libs.brute_force as brute_force
from libs.test_sudoku_solver import test_brute_force_solver

def test_generator():
    b = True

    b &= test_brute_force_generator()

    if b:
        print(ansi.GREEN + "test_generator : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_generator : FAIL" + ansi.RESET)

    return b

def test_brute_force_generator():
    b = True

    m = brute_force.generate()

    if b:
        print(ansi.GREEN + "test_generator/brute_force_generator : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_generator/brute_force_generator : FAIL" + ansi.RESET)

    return b