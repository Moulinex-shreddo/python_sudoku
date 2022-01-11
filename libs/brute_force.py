import libs.solver as solver

# Returns True if the matrix could be solved with brute_force algorithm, False otherwise
def solve(m):
    return recursive_solve(m)

# recursive_solve is a separate function for clarity purpose
def recursive_solve(m):

    for x in range(len(m[0])):
        for y in range(len(m[1])):
            if m[x][y] == 0:

                for i in range(1, 10): # Python range does not include last element
                    if solver.is_number_valid(m, i, (x, y)):
                        m[x][y] = i
                        if recursive_solve(m):
                            return True
                        else:
                            m[x][y] = 0

                # If no valid number was found for (x, y) cell, then the sudoku is not solvable with
                # the actual configuration and we need to backtrack
                return False

    return solver.is_grid_valid(m)
    