"""tests of adv_2023_04"""

import test_utils as tu
import solutions.adv_2023_04 as sol

_INPUTS = tu.get_all_inputs(4, {"small", "p"})

test_solve_a, test_solve_b = tu.get_solve_tests(
    sol.solve_a,
    {"small": 13, "p": 32001},
    sol.solve_b,
    {"small": 30, "p": 5037841},
    _INPUTS,
)
