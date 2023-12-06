"""tests of adv_2023_01"""

import test_utils as tu
import solutions.adv_2023_01 as sol

_INPUTS = tu.get_all_inputs(1, {"small", "small_2", "p", "m"})

test_solve_a_single = tu.get_test(
    sol.solve_a, {"small": 142, "p": 54667, "m": 54388}, _INPUTS
)

test_solve_b_single = tu.get_test(
    sol.solve_b, {"small": 142, "small_2": 281, "p": 54203, "m": 53515}, _INPUTS
)
