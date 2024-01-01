"""tests of adv_2023_23"""

import test_utils as tu
import solutions.adv_2023_23 as sol


_INPUTS = tu.get_inputs(23, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b), {"small": (94, 154), "p": (2326, 6574)}
)
