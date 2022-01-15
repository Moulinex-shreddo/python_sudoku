import libs.test_sudoku_solver as test_sudoku_solver
import libs.test_constaint_propagation as test_constraint_propagation
import libs.test_generator as test_generator
import libs.ansi as ansi

if __name__ == '__main__':
    b = True

    b &= test_sudoku_solver.test_sudoku_solver()
    b &= test_constraint_propagation.test_constraint_propagation()
    #b &= test_generator.test_generator()

    if b:
        print(ansi.GREEN + "Global Status : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "Global Status : FAIL" + ansi.RESET)