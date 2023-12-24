"""tests of adv_2023_24"""
import pytest
import test_utils as tu
import solutions.adv_2023_24 as sol

_SMALL_MIN = 7
_SMALL_MAX = 27


@pytest.mark.parametrize(
    "heil_a, heil_b, expected",
    [
        (
            sol.Heil([19, 13, 30], [-2, 1, -2]),
            sol.Heil([18, 19, 22], [-1, -1, -2]),
            True,
        ),
        (
            sol.Heil([19, 13, 30], [-2, 1, -2]),
            sol.Heil([20, 25, 34], [-2, -2, -4]),
            True,
        ),
        (
            sol.Heil([19, 13, 30], [-2, 1, -2]),
            sol.Heil([12, 31, 28], [-1, -2, -1]),
            False,
        ),
        (
            sol.Heil([19, 13, 30], [-2, 1, -2]),
            sol.Heil([20, 19, 15], [1, -5, -3]),
            False,
        ),
        (
            sol.Heil([18, 19, 22], [-1, -1, -2]),
            sol.Heil([20, 25, 34], [-2, -2, -4]),
            False,
        ),
        (
            sol.Heil([20, 25, 34], [-2, -2, -4]),
            sol.Heil([12, 31, 28], [-1, -2, -1]),
            False,
        ),
        (
            sol.Heil([20, 25, 34], [-2, -2, -4]),
            sol.Heil([20, 19, 15], [1, -5, -3]),
            False,
        ),
    ],
)
def test_do_cross_xy(heil_a, heil_b, expected):
    """tests do_cross_xy"""
    assert sol.do_cross_xy(heil_a, heil_b, _SMALL_MIN, _SMALL_MAX) == expected
    assert sol.do_cross_xy(heil_b, heil_a, _SMALL_MIN, _SMALL_MAX) == expected


_INPUTS = tu.get_inputs(24, {"small", "p"})


def test_count_crossing():
    """tests count_crossing agains example data"""
    assert (
        sol.count_crossing(
            sol.parse_input(_INPUTS.inputs["small"]), _SMALL_MIN, _SMALL_MAX
        )
        == 2
    )


test_solve_a = _INPUTS.get_test(sol.solve_a, {"p": 11995})

test_solve_b = _INPUTS.get_test(sol.solve_b, {"small": 47, "p": 983620716335751})
