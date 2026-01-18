"""tests of adv_2023_16"""

import test_utils as tu
import solutions.adv_2023_16 as sol

_INPUTS = tu.get_inputs(16, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b), {"small": (46, 51), "p": (7979, 8437)}
)
