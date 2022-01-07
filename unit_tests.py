import libs.test_sudoku_solver as test_sudoku_solver
import libs.ansi as ansi

if __name__ == '__main__':
    if (test_sudoku_solver.test_sudoku_solver()):
        print(ansi.GREEN + "Global Status : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "Global Status : FAIL" + ansi.RESET)