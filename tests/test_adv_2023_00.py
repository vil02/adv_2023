"""tests of adv_2023_00"""

import test_utils as tu
import solutions.adv_2023_00 as sol

_INPUTS = tu.get_all_inputs(0, {"small", "p"})

test_solve_a_single = tu.get_test(sol.solve_a, {"small": 10, "p": 11}, _INPUTS)

test_solve_a, test_solve_b = tu.get_solve_tests(
    sol.solve_a, {"small": 10, "p": 11}, sol.solve_b, {"small": 20, "p": 22}, _INPUTS
)
