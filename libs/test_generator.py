import libs.ansi as ansi
import libs.brute_force as brute_force
import libs.solver as solver

def test_generator():
    b = True

    b &= test_brute_force_recursive_generate()
    b &= test_brute_force_recursive_remove_cells()
    #b &= test_brute_force_iterative_generate()
    b &= test_brute_force_iterative_remove_cells()

    if b:
        print(ansi.GREEN + "test_generator : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_generator : FAIL" + ansi.RESET)

    return b

def test_brute_force_recursive_generate():
    b = True

    # Increase range to run burn tests, it may take a while though.
    for i in range(1):
        m = solver.generate_empty_data(9)
        brute_force.recursive_generate(m)
        b &= solver.is_grid_valid(m)

    if b:
        print(ansi.GREEN + "test_generator/brute_force_recursive_generate : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_generator/brute_force_recursive_generate : FAIL" + ansi.RESET)

    return b

def test_brute_force_recursive_remove_cells():
    b = True
    m = brute_force.generate()
    b &= solver.is_solvable(m)

    if b:
        print(ansi.GREEN + "test_generator/brute_force_recursive_remove_cells : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_generator/brute_force_recursive_remove_cells : FAIL" + ansi.RESET)

    return b

#def test_brute_force_iterative_generate():
    b = True

    for i in range(100): # Burn tests
        m = solver.generate_empty_data(9)
        brute_force.iterative_generate(m)
        b &= solver.is_grid_valid(m)

    if b:
        print(ansi.GREEN + "test_generator/brute_force_iterative_generate : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_generator/brute_force_iterative_generate : FAIL" + ansi.RESET)

    return b

def test_brute_force_iterative_remove_cells():
    b = True

    for i in range(1):
        m = brute_force.generate()
        b &= solver.is_solvable(m)

    if b:
        print(ansi.GREEN + "test_generator/brute_force_iterative_remove_cells : PASS" + ansi.RESET)
    else:
        print(ansi.RED + "test_generator/brute_force_iterative_remove_cells : FAIL" + ansi.RESET)

    return b