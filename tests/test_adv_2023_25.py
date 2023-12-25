"""tests of adv_2023_25"""

import test_utils as tu
import solutions.adv_2023_25 as sol


_INPUTS = tu.get_inputs(25, {"small", "p"})

test_solve_a = _INPUTS.get_test(sol.solve_a, {"small": 54, "p": 591890})
