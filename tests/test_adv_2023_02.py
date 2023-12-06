"""tests of adv_2023_02"""
import pytest

import test_utils as tu
import solutions.adv_2023_02 as sol


_GAME_1 = sol.Game(
    1,
    [
        {"red": 4, "green": 0, "blue": 3},
        {"red": 1, "green": 2, "blue": 6},
        {"red": 0, "green": 2, "blue": 0},
    ],
)

_GAME_2 = sol.Game(
    2,
    [
        {"red": 0, "green": 2, "blue": 1},
        {"red": 1, "green": 3, "blue": 4},
        {"red": 0, "green": 1, "blue": 1},
    ],
)

_GAME_3 = sol.Game(
    3,
    [
        {"red": 20, "green": 8, "blue": 6},
        {"red": 4, "green": 13, "blue": 5},
        {"red": 1, "green": 5, "blue": 0},
    ],
)

_GAME_4 = sol.Game(
    4,
    [
        {"red": 3, "green": 1, "blue": 6},
        {"red": 6, "green": 3, "blue": 0},
        {"red": 14, "green": 3, "blue": 15},
    ],
)


@pytest.mark.parametrize(
    "input_str,expected",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            _GAME_1,
        ),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", _GAME_2),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            _GAME_3,
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            _GAME_4,
        ),
    ],
)
def test_parse_single_game(input_str, expected):
    """
    tests parse_single_game against example input
    """
    assert sol.parse_single_game(input_str) == expected


@pytest.mark.parametrize(
    "in_game",
    [_GAME_1, _GAME_2],
)
def test_is_possible_positive(in_game):
    """
    poitive tests of is_possible
    """
    assert sol.is_possible(in_game)


@pytest.mark.parametrize(
    "in_game",
    [_GAME_3, _GAME_4],
)
def test_is_possible_negative(in_game):
    """
    negative tests of is_possible
    """
    assert not sol.is_possible(in_game)


@pytest.mark.parametrize(
    "in_game, expected",
    [
        (_GAME_1, {"red": 4, "green": 2, "blue": 6}),
        (_GAME_2, {"red": 1, "green": 3, "blue": 4}),
        (_GAME_3, {"red": 20, "green": 13, "blue": 6}),
        (_GAME_4, {"red": 14, "green": 3, "blue": 15}),
    ],
)
def test_compute_smallest_hist(in_game, expected):
    """
    tests compute_smallest_hist
    """
    assert sol.compute_smallest_hist(in_game) == expected


_INPUTS = tu.get_inputs(2, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {"small": (8, 2286), "p": (2810, 69110)},
)
