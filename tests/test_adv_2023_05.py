"""tests of adv_2023_05"""

import test_utils as gu
import solutions.adv_2023_05 as sol

_INPUTS = gu.get_all_inputs(5, {"small", "p"})

test_solve_a, test_solve_b = gu.get_solve_tests(
    sol.solve_a,
    {"small": 35, "p": 650599855},
    sol.solve_b,
    {"small": 46, "p": 1240035},
    _INPUTS,
)
