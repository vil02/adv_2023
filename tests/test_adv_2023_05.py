"""tests of adv_2023_05"""

import pytest

import test_utils as tu
import solutions.adv_2023_05 as sol


@pytest.mark.parametrize(
    "in_interval",
    [sol.Interval(1, 2), sol.Interval(0, 10)],
)
def test_is_not_empty_positive(in_interval):
    """positive tests of is_not_empty"""
    assert sol.is_not_empty(in_interval)


@pytest.mark.parametrize(
    "in_interval",
    [sol.Interval(0, 0), sol.Interval(2, 1)],
)
def test_is_not_empty_negative(in_interval):
    """negative tests of is_not_empty"""
    assert not sol.is_not_empty(in_interval)


_INTERVAL_SHIFT = sol.IntervalShift(5, 10, 4)


@pytest.mark.parametrize(
    "in_seed, expected",
    [(10, 5), (11, 6), (12, 7), (13, 8), (14, 9)],
)
def test_interval_shif(in_seed, expected):
    """checks if IntervalShift mapps properly"""
    assert _INTERVAL_SHIFT(in_seed) == expected


@pytest.mark.parametrize(
    "in_seed",
    [9, 15],
)
def test_interval_shif_raises_error(in_seed):
    """checks if IntervalShift if the input is outside the interval"""
    with pytest.raises(Exception):
        _INTERVAL_SHIFT(in_seed)


@pytest.mark.parametrize(
    "in_interval, expected",
    [
        (
            sol.Interval(10, 14),
            (sol.Interval(10, 10), sol.Interval(10, 14), sol.Interval(14, 14)),
        ),
        (
            sol.Interval(9, 12),
            (sol.Interval(9, 10), sol.Interval(10, 12), sol.Interval(14, 12)),
        ),
        (
            sol.Interval(11, 12),
            (sol.Interval(11, 10), sol.Interval(11, 12), sol.Interval(14, 12)),
        ),
        (
            sol.Interval(13, 15),
            (sol.Interval(13, 10), sol.Interval(13, 14), sol.Interval(14, 15)),
        ),
    ],
)
def test_interval_shif_split(in_interval, expected):
    """checks IntervalShift.split"""
    assert _INTERVAL_SHIFT.split(in_interval) == expected


def test_interval_shif_last_source():
    """tests the last_source method of IntervalShift"""
    assert _INTERVAL_SHIFT.last_source() == 14


_INPUTS = tu.get_inputs(5, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {"small": (35, 46), "p": (650599855, 1240035)},
)
