"""tests of adv_2023_14"""

import pytest

import test_utils as tu
import solutions.adv_2023_14 as sol


_INPUTS = tu.get_inputs(14, {"small", "p"})

_SMALL = {
    (1, 1): "#",
    (2, 1): "O",
    (3, 1): "O",
    (4, 1): ".",
    (5, 1): ".",
    (6, 1): "#",
    (7, 1): ".",
    (8, 1): ".",
    (9, 1): ".",
    (10, 1): ".",
    (1, 2): "#",
    (2, 2): ".",
    (3, 2): ".",
    (4, 2): ".",
    (5, 2): ".",
    (6, 2): "#",
    (7, 2): "#",
    (8, 2): "#",
    (9, 2): ".",
    (10, 2): ".",
    (1, 3): ".",
    (2, 3): ".",
    (3, 3): ".",
    (4, 3): ".",
    (5, 3): ".",
    (6, 3): ".",
    (7, 3): ".",
    (8, 3): "O",
    (9, 3): ".",
    (10, 3): ".",
    (1, 4): ".",
    (2, 4): ".",
    (3, 4): "O",
    (4, 4): ".",
    (5, 4): ".",
    (6, 4): "#",
    (7, 4): "O",
    (8, 4): ".",
    (9, 4): ".",
    (10, 4): "O",
    (1, 5): "O",
    (2, 5): ".",
    (3, 5): "#",
    (4, 5): ".",
    (5, 5): ".",
    (6, 5): "O",
    (7, 5): ".",
    (8, 5): "#",
    (9, 5): ".",
    (10, 5): "#",
    (1, 6): ".",
    (2, 6): "O",
    (3, 6): ".",
    (4, 6): ".",
    (5, 6): ".",
    (6, 6): ".",
    (7, 6): ".",
    (8, 6): "O",
    (9, 6): "#",
    (10, 6): ".",
    (1, 7): "O",
    (2, 7): "O",
    (3, 7): ".",
    (4, 7): "#",
    (5, 7): "O",
    (6, 7): ".",
    (7, 7): ".",
    (8, 7): ".",
    (9, 7): ".",
    (10, 7): "O",
    (1, 8): ".",
    (2, 8): ".",
    (3, 8): ".",
    (4, 8): ".",
    (5, 8): ".",
    (6, 8): "#",
    (7, 8): "#",
    (8, 8): ".",
    (9, 8): ".",
    (10, 8): ".",
    (1, 9): "O",
    (2, 9): ".",
    (3, 9): "O",
    (4, 9): "O",
    (5, 9): "#",
    (6, 9): ".",
    (7, 9): ".",
    (8, 9): ".",
    (9, 9): ".",
    (10, 9): "#",
    (1, 10): "O",
    (2, 10): ".",
    (3, 10): ".",
    (4, 10): ".",
    (5, 10): ".",
    (6, 10): "#",
    (7, 10): ".",
    (8, 10): ".",
    (9, 10): ".",
    (10, 10): ".",
}
_X_SMALL = 10
_Y_SMALL = 10


def test_parse_input():
    """tests parse_input with example data"""
    assert sol.parse_input(_INPUTS.inputs["small"]) == (_SMALL, _X_SMALL, _Y_SMALL)


@pytest.mark.parametrize(
    ("x_pos", "y_pos", "expected"),
    [
        (1, 10, 10),
        (1, 9, 9),
        (1, 7, 8),
        (2, 7, 10),
        (5, 7, 8),
    ],
)
def test_find_empty_north(x_pos, y_pos, expected):
    """tests find_empty_north"""
    assert sol.find_empty_north(_SMALL, _Y_SMALL, x_pos, y_pos) == expected


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b), {"small": (136, 64), "p": (109385, 93102)}
)
