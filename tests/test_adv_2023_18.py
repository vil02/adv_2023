"""tests of adv_2023_18"""

import test_utils as tu
import solutions.adv_2023_18 as sol


_INPUTS = tu.get_inputs(18, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {"small": (62, 952408144115), "p": (68115, 71262565063800)},
)
