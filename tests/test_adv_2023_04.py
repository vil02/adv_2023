"""tests of adv_2023_04"""

import test_utils as tu
import solutions.adv_2023_04 as sol

_INPUTS = tu.get_inputs(4, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {"small": (13, 30), "p": (32001, 5037841)},
)
