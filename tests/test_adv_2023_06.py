"""tests of adv_2023_06"""

import pytest

import test_utils as gu
import solutions.adv_2023_06 as sol

_RACE_1 = sol.Race(7, 9)
_RACE_2 = sol.Race(15, 40)
_RACE_3 = sol.Race(30, 200)
_RACE_B = sol.Race(71530, 940200)


@pytest.mark.parametrize(
    "in_race, expected",
    [
        (_RACE_1, 4),
        (_RACE_2, 8),
        (_RACE_3, 9),
        (_RACE_B, 71503),
    ],
)
def test_count_ways_to_win(in_race, expected):
    """tests count_ways_to_win"""
    assert sol.count_ways_to_win(in_race) == expected


_INPUTS = gu.get_all_inputs(6, {"small", "p"})


def test_parse_input_a():
    """tests parse_input_b agains example data"""
    assert sol.parse_input_a(_INPUTS["small"]) == [_RACE_1, _RACE_2, _RACE_3]


def test_parse_input_b():
    """tests parse_input_b agains example data"""
    assert sol.parse_input_b(_INPUTS["small"]) == _RACE_B


test_solve_a, test_solve_b = gu.get_solve_tests(
    sol.solve_a,
    {"small": 288, "p": 5133600},
    sol.solve_b,
    {"small": 71503, "p": 40651271},
    _INPUTS,
)
