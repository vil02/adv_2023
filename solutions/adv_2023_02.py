"""solution of adv_2023_02"""

import collections
import functools

Game = collections.namedtuple("Game", ["id", "counts"])

_LIMITS = {"red": 12, "green": 13, "blue": 14}

_COLORS = list(_LIMITS.keys())


def _parse_into_dict(in_str):
    res = {_: 0 for _ in _COLORS}
    for _ in in_str.split(", "):
        num, color = _.split(" ")
        res[color] += int(num)
    return res


def _parse_counts(in_str):
    res = []
    for _ in in_str.split("; "):
        res.append(_parse_into_dict(_))
    return res


def _parse_game_str(in_str):
    _, id_str = in_str.split(" ")
    assert _ == "Game"
    return int(id_str)


def parse_single_game(in_str):
    """
    parses a game string into a Game
    """
    game_str, counts_str = in_str.split(": ")

    return Game(id=_parse_game_str(game_str), counts=_parse_counts(counts_str))


def _parse_input(in_str):
    return [parse_single_game(_) for _ in in_str.splitlines()]


def _check_single_dict(in_color_dict):
    return all(in_color_dict[_] <= _LIMITS[_] for _ in _COLORS)


def is_possible(in_game):
    """checks if the game is possible having number of cubes as in _LIMITS"""
    return all(_check_single_dict(_) for _ in in_game.counts)


def solve_a(in_str):
    """returns the solution for part_a"""
    return sum(_.id for _ in _parse_input(in_str) if is_possible(_))


def _get_max(in_dicts, in_key):
    return max(_[in_key] for _ in in_dicts)


def compute_smallest_hist(in_game):
    """
    returns the minimal number of each cube for a game
    """
    return {_: _get_max(in_game.counts, _) for _ in _COLORS}


def _compute_power(in_dict):
    return functools.reduce(lambda a, b: a * b, in_dict.values(), 1)


def solve_b(in_str):
    """returns the solution for part_b"""
    return sum(_compute_power(compute_smallest_hist(_)) for _ in _parse_input(in_str))
