"""tests of adv_2023_22"""

import test_utils as tu
import solutions.adv_2023_22 as sol

_INPUTS = tu.get_inputs(22, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b), {"small": (5, 7), "p": (395, 64714)}
)
