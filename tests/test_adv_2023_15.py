"""tests of adv_2023_15"""

import pytest

import test_utils as tu
import solutions.adv_2023_15 as sol


@pytest.mark.parametrize(
    ("in_str", "expected"),
    [
        ("rn=1", 30),
        ("cm-", 253),
        ("qp=3", 97),
        ("cm=2", 47),
        ("qp-", 14),
        ("pc=4", 180),
        ("ot=9", 9),
        ("ab=5", 197),
        ("pc-", 48),
        ("pc=6", 214),
        ("ot=7", 231),
    ],
)
def test_out_hash(in_str, expected):
    """tests hash with example data"""
    assert sol.our_hash(in_str) == expected


_INPUTS = tu.get_inputs(15, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b), {"small": (1320, 145), "p": (510792, 269410)}
)
