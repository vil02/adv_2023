"""tests of adv_2023_01"""

import test_utils as tu
import solutions.adv_2023_01 as sol

_INPUTS = tu.get_inputs(1, {"small", "small_2", "p", "m"})

test_solve_a = _INPUTS.get_test(sol.solve_a, {"small": 142, "p": 54667, "m": 54388})

test_solve_b = _INPUTS.get_test(
    sol.solve_b, {"small": 142, "small_2": 281, "p": 54203, "m": 53515}
)
