"""tests of adv_2023_00"""

import test_utils as tu
import solutions.adv_2023_00 as sol

_INPUTS = tu.get_inputs(0, {"small", "p"})

test_solve_a_single = _INPUTS.get_test(sol.solve_a, {"small": 10, "p": 11})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b), {"small": (10, 20), "p": (11, 22)}
)
