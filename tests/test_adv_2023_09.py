"""tests of adv_2023_09"""

import pytest

import test_utils as tu
import solutions.adv_2023_09 as sol


@pytest.mark.parametrize(
    ("in_list", "expected"),
    [
        ([0, 3, 6, 9, 12, 15], 18),
        ([1, 3, 6, 10, 15, 21], 28),
        ([10, 13, 16, 21, 30, 45], 68),
    ],
)
def test_extrapolate_right(in_list, expected):
    """tests extrapolate_right"""
    assert sol.extrapolate_right(in_list) == expected


@pytest.mark.parametrize(
    ("in_list", "expected"),
    [
        ([0, 2, 4, 6], -2),
        ([3, 3, 5, 9, 15], 5),
        ([10, 13, 16, 21, 30, 45], 5),
        ([1, 3, 6, 10, 15, 21], 0),
        ([0, 3, 6, 9, 12, 15], -3),
    ],
)
def test_extrapolate_left(in_list, expected):
    """tests extrapolate_left"""
    assert sol.extrapolate_left(in_list) == expected


_INPUTS = tu.get_inputs(9, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b), {"small": (114, 2), "p": (1696140818, 1152)}
)
