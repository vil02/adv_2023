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
def test_get_hand_type(in_hand: str, expected: str) -> None:
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
def test_get_best_hand_type(in_hand: str, expected: str) -> None:
    """tests get_best_hand_type"""
    assert sol.get_best_hand_type(in_hand) == expected


# ordering in a: 32T3K, KTJJT, KK677, T55J5, QQQJA
@pytest.mark.parametrize(
    "weaker, stronger",
    [
        ("32T3K", "KK677"),
        ("32T3K", "KTJJT"),
        ("KTJJT", "KK677"),
        ("KTJJT", "T55J5"),
        ("KTJJT", "QQQJA"),
        ("KK677", "T55J5"),
        ("KK677", "QQQJA"),
        ("T55J5", "QQQJA"),
    ],
)
def test_cmp_a(weaker: str, stronger: str) -> None:
    """tests cmp_a"""
    assert sol.cmp_a(weaker, stronger) == -1
    assert sol.cmp_a(stronger, weaker) == 1
    assert sol.cmp_a(weaker, weaker) == 0
    assert sol.cmp_a(stronger, stronger) == 0


# ordering in b: 32T3K, KK677, T55J5, QQQJA, KTJJT
@pytest.mark.parametrize(
    "weaker, stronger",
    [
        ("32T3K", "KTJJT"),
        ("QQQJA", "KTJJT"),
        ("T55J5", "KTJJT"),
        ("KK677", "KTJJT"),
        ("T55J5", "QQQJA"),
        ("KK677", "QQQJA"),
        ("32T3K", "QQQJA"),
        ("32T3K", "KK677"),
    ],
)
def test_cmp_b(weaker: str, stronger: str) -> None:
    """tests cmp_b"""
    assert sol.cmp_b(weaker, stronger) == -1
    assert sol.cmp_b(stronger, weaker) == 1
    assert sol.cmp_b(weaker, weaker) == 0
    assert sol.cmp_b(stronger, stronger) == 0


_INPUTS = tu.get_inputs(7, {"small", "p", "r"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {"small": (6440, 5905), "p": (250453939, 248652697), "r": (6592, 6839)},
)
