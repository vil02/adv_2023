"""tests of adv_2023_03"""

import test_utils as tu
import solutions.adv_2023_03 as sol

_INPUTS = tu.get_inputs(3, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b), {"small": (4361, 467835), "p": (525911, 75805607)}
)
