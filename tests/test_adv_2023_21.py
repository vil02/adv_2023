"""tests of adv_2023_21"""

import pytest

import test_utils as tu
import solutions.adv_2023_21 as sol


_INPUTS = tu.get_inputs(21, {"small", "p"})

_SMALL_PLAN = {
    (0, 0): ".",
    (1, 0): ".",
    (2, 0): ".",
    (3, 0): ".",
    (4, 0): ".",
    (5, 0): ".",
    (6, 0): ".",
    (7, 0): ".",
    (8, 0): ".",
    (9, 0): ".",
    (10, 0): ".",
    (0, 1): ".",
    (1, 1): ".",
    (2, 1): ".",
    (3, 1): ".",
    (4, 1): ".",
    (5, 1): "#",
    (6, 1): "#",
    (7, 1): "#",
    (8, 1): ".",
    (9, 1): "#",
    (10, 1): ".",
    (0, 2): ".",
    (1, 2): "#",
    (2, 2): "#",
    (3, 2): "#",
    (4, 2): ".",
    (5, 2): "#",
    (6, 2): "#",
    (7, 2): ".",
    (8, 2): ".",
    (9, 2): "#",
    (10, 2): ".",
    (0, 3): ".",
    (1, 3): ".",
    (2, 3): "#",
    (3, 3): ".",
    (4, 3): "#",
    (5, 3): ".",
    (6, 3): ".",
    (7, 3): ".",
    (8, 3): "#",
    (9, 3): ".",
    (10, 3): ".",
    (0, 4): ".",
    (1, 4): ".",
    (2, 4): ".",
    (3, 4): ".",
    (4, 4): "#",
    (5, 4): ".",
    (6, 4): "#",
    (7, 4): ".",
    (8, 4): ".",
    (9, 4): ".",
    (10, 4): ".",
    (0, 5): ".",
    (1, 5): "#",
    (2, 5): "#",
    (3, 5): ".",
    (4, 5): ".",
    (5, 5): "S",
    (6, 5): "#",
    (7, 5): "#",
    (8, 5): "#",
    (9, 5): "#",
    (10, 5): ".",
    (0, 6): ".",
    (1, 6): "#",
    (2, 6): "#",
    (3, 6): ".",
    (4, 6): ".",
    (5, 6): "#",
    (6, 6): ".",
    (7, 6): ".",
    (8, 6): ".",
    (9, 6): "#",
    (10, 6): ".",
    (0, 7): ".",
    (1, 7): ".",
    (2, 7): ".",
    (3, 7): ".",
    (4, 7): ".",
    (5, 7): ".",
    (6, 7): ".",
    (7, 7): "#",
    (8, 7): "#",
    (9, 7): ".",
    (10, 7): ".",
    (0, 8): ".",
    (1, 8): "#",
    (2, 8): "#",
    (3, 8): ".",
    (4, 8): "#",
    (5, 8): ".",
    (6, 8): "#",
    (7, 8): "#",
    (8, 8): "#",
    (9, 8): "#",
    (10, 8): ".",
    (0, 9): ".",
    (1, 9): "#",
    (2, 9): "#",
    (3, 9): ".",
    (4, 9): ".",
    (5, 9): "#",
    (6, 9): "#",
    (7, 9): ".",
    (8, 9): "#",
    (9, 9): "#",
    (10, 9): ".",
    (0, 10): ".",
    (1, 10): ".",
    (2, 10): ".",
    (3, 10): ".",
    (4, 10): ".",
    (5, 10): ".",
    (6, 10): ".",
    (7, 10): ".",
    (8, 10): ".",
    (9, 10): ".",
    (10, 10): ".",
}
_SMALL_X = 11
_SMALL_Y = 11
_SMALL_START_POS = (5, 5)


def test_parse_input():
    """tests parse input with example data"""
    assert sol.parse_input(_INPUTS.inputs["small"]) == (
        _SMALL_PLAN,
        _SMALL_X,
        _SMALL_Y,
        _SMALL_START_POS,
    )


_SMALL_GETTER = sol.get_getter(_SMALL_PLAN, _SMALL_X, _SMALL_Y)


@pytest.mark.parametrize(
    ("in_steps", "expected"),
    [
        (6, 16),
        (10, 50),
        (50, 1594),
        (100, 6536),
    ],
)
def test_count_accessible(in_steps, expected):
    """tests count_accessible with example data"""
    assert sol.count_accessible(_SMALL_GETTER, _SMALL_START_POS, in_steps) == expected


@pytest.mark.parametrize(
    ("in_steps", "expected"),
    [
        (50, 1594),
        (100, 6536),
        (500, 167004),
        (1000, 668697),
        (5000, 16733044),
    ],
)
def test_count_accessible_with_extrapolation(in_steps, expected):
    """tests count_accessible_with_extrapolation with example data"""
    assert (
        sol.count_accessible_with_extrapolation(
            _SMALL_GETTER, _SMALL_X, _SMALL_START_POS, in_steps
        )
        == expected
    )


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b), {"p": (3751, 619407349431167)}
)
