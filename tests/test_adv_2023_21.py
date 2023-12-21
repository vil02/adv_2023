"""tests of adv_2023_21"""

import pytest

import test_utils as tu
import solutions.adv_2023_21 as sol


_INPUTS = tu.get_inputs(21, {"small", "p"})


@pytest.mark.parametrize(
    "in_steps, expected",
    [
        (6, 16),
        # (10, 50),
        # (50, 1594),
        # (100, 6536),
        # (500, 167004),
        # (1000, 668697),
        # (5000, 16733044),
    ],
)
def test_count_accessible(in_steps, expected):
    """tests count_accessible with example data"""
    plan, x_size, y_size, start_pos = sol.parse_input(_INPUTS.inputs["small"])
    getter = sol.get_getter(plan, x_size, y_size)
    assert sol.count_accessible(getter, start_pos, in_steps) == expected


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b), {"p": (3751, 619407349431167)}
)
