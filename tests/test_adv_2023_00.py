"""tests of adv_2023_00"""

import pytest
import general_utils as gu
import solutions.adv_2023_00 as sol

_DAY_NUM = 0


def _data_small():
    return gu.read_input(_DAY_NUM, "small")


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 10, id="small"),
        pytest.param(_data_p(), 11, id="p"),
    ],
)
def test_solve_a(input_str, expected):
    """tests solve_a"""
    assert sol.solve_a(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param(_data_small(), 20, id="small"),
        pytest.param(_data_p(), 22, id="p"),
    ],
)
def test_solve_b(input_str, expected):
    """tests solve_b"""
    assert sol.solve_b(input_str) == expected
