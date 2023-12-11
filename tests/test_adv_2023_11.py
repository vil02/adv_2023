"""tests of adv_2023_11"""

import pytest

import test_utils as tu
import solutions.adv_2023_11 as sol


_INPUTS = tu.get_inputs(11, {"small", "p"})

_SMALL_IMAGE = {(7, 1), (1, 5), (4, 9), (9, 6), (0, 9), (6, 4), (3, 0), (0, 2), (7, 8)}
_SMALL_X_MAX = 10
_SMALL_Y_MAX = 10
_SMALL_EMPTY_ROWS = {3, 7}
_SMALL_EMPTY_COLS = {2, 5, 8}


def test_parse_input():
    """checks parse_input with example data"""
    assert sol.parse_input(_INPUTS.inputs["small"]) == (
        _SMALL_IMAGE,
        _SMALL_X_MAX,
        _SMALL_Y_MAX,
    )


def test_get_empty_rows():
    """checks get_empty_rows with example data"""
    assert (
        sol.get_empty_rows(_SMALL_IMAGE, _SMALL_X_MAX, _SMALL_Y_MAX)
        == _SMALL_EMPTY_ROWS
    )


def test_get_empty_cols():
    """checks get_empty_cols with example data"""
    assert (
        sol.get_empty_cols(_SMALL_IMAGE, _SMALL_X_MAX, _SMALL_Y_MAX)
        == _SMALL_EMPTY_COLS
    )


@pytest.mark.parametrize(
    "in_pos_a, in_pos_b, in_empty_size, expected",
    [
        ((1, 5), (4, 9), 2 - 1, 9),
        ((3, 0), (7, 8), 2 - 1, 15),
        ((0, 8), (4, 8), 2 - 1, 5),
        ((0, 8), (4, 8), 10 - 1, 13),
        ((0, 8), (4, 8), 100 - 1, 103),
    ],
)
def test_compute_dist(in_pos_a, in_pos_b, in_empty_size, expected):
    """checks compute_dist with example data"""
    assert (
        sol.compute_dist(
            in_pos_a, in_pos_b, _SMALL_EMPTY_ROWS, _SMALL_EMPTY_COLS, in_empty_size
        )
        == expected
    )
    assert (
        sol.compute_dist(
            in_pos_b, in_pos_a, _SMALL_EMPTY_ROWS, _SMALL_EMPTY_COLS, in_empty_size
        )
        == expected
    )


@pytest.mark.parametrize(
    "in_empty_size, expected",
    [(2 - 1, 374), (10 - 1, 1030), (100 - 1, 8410)],
)
def test_compute_sum_of_dists(in_empty_size, expected):
    """tests compute_sum_of_dists with example data"""
    assert sol.compute_sum_of_dists(_INPUTS.inputs["small"], in_empty_size) == expected


test_solve_a = _INPUTS.get_test(sol.solve_a, {"small": 374, "p": 9550717})

test_solve_b = _INPUTS.get_test(sol.solve_b, {"p": 648458253817})
