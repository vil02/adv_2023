"""tests of adv_2023_13"""

import pytest

import test_utils as tu
import solutions.adv_2023_13 as sol


_INPUTS = tu.get_inputs(13, {"small", "p", "r"})

_IMG_A = {
    (1, 1): "#",
    (2, 1): ".",
    (3, 1): "#",
    (4, 1): "#",
    (5, 1): ".",
    (6, 1): ".",
    (7, 1): "#",
    (8, 1): "#",
    (9, 1): ".",
    (1, 2): ".",
    (2, 2): ".",
    (3, 2): "#",
    (4, 2): ".",
    (5, 2): "#",
    (6, 2): "#",
    (7, 2): ".",
    (8, 2): "#",
    (9, 2): ".",
    (1, 3): "#",
    (2, 3): "#",
    (3, 3): ".",
    (4, 3): ".",
    (5, 3): ".",
    (6, 3): ".",
    (7, 3): ".",
    (8, 3): ".",
    (9, 3): "#",
    (1, 4): "#",
    (2, 4): "#",
    (3, 4): ".",
    (4, 4): ".",
    (5, 4): ".",
    (6, 4): ".",
    (7, 4): ".",
    (8, 4): ".",
    (9, 4): "#",
    (1, 5): ".",
    (2, 5): ".",
    (3, 5): "#",
    (4, 5): ".",
    (5, 5): "#",
    (6, 5): "#",
    (7, 5): ".",
    (8, 5): "#",
    (9, 5): ".",
    (1, 6): ".",
    (2, 6): ".",
    (3, 6): "#",
    (4, 6): "#",
    (5, 6): ".",
    (6, 6): ".",
    (7, 6): "#",
    (8, 6): "#",
    (9, 6): ".",
    (1, 7): "#",
    (2, 7): ".",
    (3, 7): "#",
    (4, 7): ".",
    (5, 7): "#",
    (6, 7): "#",
    (7, 7): ".",
    (8, 7): "#",
    (9, 7): ".",
}
_SMALL_SIZE = 9, 7

_IMG_B = {
    (1, 1): "#",
    (2, 1): ".",
    (3, 1): ".",
    (4, 1): ".",
    (5, 1): "#",
    (6, 1): "#",
    (7, 1): ".",
    (8, 1): ".",
    (9, 1): "#",
    (1, 2): "#",
    (2, 2): ".",
    (3, 2): ".",
    (4, 2): ".",
    (5, 2): ".",
    (6, 2): "#",
    (7, 2): ".",
    (8, 2): ".",
    (9, 2): "#",
    (1, 3): ".",
    (2, 3): ".",
    (3, 3): "#",
    (4, 3): "#",
    (5, 3): ".",
    (6, 3): ".",
    (7, 3): "#",
    (8, 3): "#",
    (9, 3): "#",
    (1, 4): "#",
    (2, 4): "#",
    (3, 4): "#",
    (4, 4): "#",
    (5, 4): "#",
    (6, 4): ".",
    (7, 4): "#",
    (8, 4): "#",
    (9, 4): ".",
    (1, 5): "#",
    (2, 5): "#",
    (3, 5): "#",
    (4, 5): "#",
    (5, 5): "#",
    (6, 5): ".",
    (7, 5): "#",
    (8, 5): "#",
    (9, 5): ".",
    (1, 6): ".",
    (2, 6): ".",
    (3, 6): "#",
    (4, 6): "#",
    (5, 6): ".",
    (6, 6): ".",
    (7, 6): "#",
    (8, 6): "#",
    (9, 6): "#",
    (1, 7): "#",
    (2, 7): ".",
    (3, 7): ".",
    (4, 7): ".",
    (5, 7): ".",
    (6, 7): "#",
    (7, 7): ".",
    (8, 7): ".",
    (9, 7): "#",
}


def test_parse_input():
    """tests parse_input with example data"""
    assert sol.parse_input(_INPUTS.inputs["small"]) == [
        (_IMG_A, *_SMALL_SIZE),
        (_IMG_B, *_SMALL_SIZE),
    ]


@pytest.mark.parametrize(
    "in_img, in_size_x, in_size_y, expected",
    [
        (_IMG_A, *_SMALL_SIZE, 5),
        (_IMG_B, *_SMALL_SIZE, 400),
        (*sol.parse_input(_INPUTS.inputs["p"])[0], 9),
        (*sol.parse_input(_INPUTS.inputs["p"])[1], 400),
        (*sol.parse_input(_INPUTS.inputs["p"])[2], 1000),
        (*sol.parse_input(_INPUTS.inputs["p"])[3], 400),
        (*sol.parse_input(_INPUTS.inputs["p"])[4], 14),
        (*sol.parse_input(_INPUTS.inputs["p"])[5], 600),
        (*sol.parse_input(_INPUTS.inputs["p"])[6], 200),
        (*sol.parse_input(_INPUTS.inputs["p"])[7], 1400),
    ],
)
def test_compute_sym_score(in_img, in_size_x, in_size_y, expected):
    """tests compute_sym_socre"""
    assert sol.compute_sym_score(in_img, in_size_x, in_size_y) == expected


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {"small": (405, 400), "p": (40006, 28627), "r": (709, 1400)},
)


def test_find_smuge_with_wrong_input():
    """tests find_smuge with input leading to None"""
    assert sol.find_smuge({}, 0, 0) is None
