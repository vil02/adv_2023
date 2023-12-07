"""tests of adv_2023_07"""
import pytest

import test_utils as tu
import solutions.adv_2023_07 as sol


@pytest.mark.parametrize(
    "in_hand, expected",
    [
        ("AAAAA", "five of kind"),
        ("AA8AA", "four of kind"),
        ("23332", "full house"),
        ("TTT98", "three of kind"),
        ("23432", "two pair"),
        ("A23A4", "one pair"),
        ("23456", "high card"),
        ("32T3K", "one pair"),
        ("KK677", "two pair"),
        ("KTJJT", "two pair"),
        ("T55J5", "three of kind"),
        ("QQQJA", "three of kind"),
    ],
)
def test_get_hand_type(in_hand, expected):
    """tests get_hand_type"""
    assert sol.get_hand_type(in_hand) == expected


@pytest.mark.parametrize(
    "in_hand, expected",
    [
        ("QJJQ2", "four of kind"),
        ("T55J5", "four of kind"),
        ("KTJJT", "four of kind"),
        ("QQQJA", "four of kind"),
    ],
)
def test_get_best_hand_type(in_hand, expected):
    """tests get_best_hand_type"""
    assert sol.get_best_hand_type(in_hand) == expected


_INPUTS = tu.get_inputs(7, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b), {"small": (6440, 5905), "p": (250453939, 248652697)}
)
