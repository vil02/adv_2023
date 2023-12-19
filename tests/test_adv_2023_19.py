"""tests of adv_2023_19"""

import test_utils as tu
import solutions.adv_2023_19 as sol


_INPUTS = tu.get_inputs(19, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {"small": (19114, 167409079868000), "p": (480738, 131550418841958)},
)
