"""tests of adv_2023_08"""

import test_utils as tu
import solutions.adv_2023_08 as sol


_INPUTS = tu.get_inputs(8, {"small", "small_a", "small_b", "p"})

test_solve_a_single = _INPUTS.get_test(
    sol.solve_a, {"small": 2, "small_a": 6, "p": 16271}
)

test_solve_b_single = _INPUTS.get_test(sol.solve_b, {"small_b": 6, "p": 14265111103729})
