"""tests of adv_2023_20"""

import test_utils as tu
import solutions.adv_2023_20 as sol


_INPUTS = tu.get_inputs(20, {"small_a", "small_b", "p"})

test_solve_a = _INPUTS.get_test(
    sol.solve_a, {"small_a": 32000000, "small_b": 11687500, "p": 791120136}
)

test_solve_b = _INPUTS.get_test(sol.solve_b, {"p": 215252378794009})
