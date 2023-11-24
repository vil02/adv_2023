"""tests of adv_2023_00"""

import general_utils as gu
import solutions.adv_2023_00 as sol

_INPUTS = gu.get_all_inputs(0, {"small", "p"})

test_solve_a_single = gu.get_test(sol.solve_a, {"small": 10, "p": 11}, _INPUTS)

test_solve_a, test_solve_b = gu.get_solve_tests(
    sol.solve_a, {"small": 10, "p": 11}, sol.solve_b, {"small": 20, "p": 22}, _INPUTS
)
