"""tests of adv_2023_17"""

import test_utils as tu
import solutions.adv_2023_17 as sol

_INPUTS = tu.get_inputs(17, {"small", "small_b", "p"})

test_solve_a = _INPUTS.get_test(sol.solve_a, {"small": 102, "p": 1246})
test_solve_b = _INPUTS.get_test(sol.solve_b, {"small": 94, "small_b": 71, "p": 1389})
