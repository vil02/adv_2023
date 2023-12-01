"""tests of adv_2023_01"""

import test_utils as gu
import solutions.adv_2023_01 as sol

_INPUTS = gu.get_all_inputs(1, {"small", "small_2", "p"})

test_solve_a_single = gu.get_test(sol.solve_a, {"small": 142, "p": 54667}, _INPUTS)

test_solve_b_single = gu.get_test(
    sol.solve_b, {"small": 142, "small_2": 281, "p": 54203}, _INPUTS
)
