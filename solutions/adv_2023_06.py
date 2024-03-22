"""solution of adv_2023_06"""

import collections
import functools

Race = collections.namedtuple("Race", ["time", "dist"])


def _parse_line_num(in_line: str, in_name: str) -> list[str]:
    pieces = in_line.split()
    assert pieces[0] == in_name
    return pieces[1:]


def parse_input_a(in_str: str) -> list[Race]:
    """parses the input into list of races"""
    time_line, dist_line = in_str.splitlines()
    res = []
    for _t, _d in zip(
        _parse_line_num(time_line, "Time:"), _parse_line_num(dist_line, "Distance:")
    ):
        res.append(Race(int(_t), int(_d)))

    return res


def _solve_quadratic(in_a: int, in_b: int, in_c: int) -> tuple[float, float]:
    delta = in_b**2 - 4 * in_a * in_c
    assert delta > 0
    sqrt_delta = delta**0.5
    return (-in_b - sqrt_delta) / (2 * in_a), (-in_b + sqrt_delta) / (2 * in_a)


def _race_round(in_val: float) -> int:
    int_val = int(in_val)
    if in_val == int_val:
        return int_val - 1
    return int_val


def count_ways_to_win(in_race: Race) -> int:
    """returns the number of ways one can win given race"""
    end, start = _solve_quadratic(-1, in_race.time, -in_race.dist)
    assert start < end
    return _race_round(end) - int(start)


def solve_a(in_str: str) -> int:
    """returns the solution for part_a"""
    data = parse_input_a(in_str)
    ways = [count_ways_to_win(_) for _ in data]
    return functools.reduce(lambda a, b: a * b, ways, 1)


def _join_to_int(in_str_list: list[str]) -> int:
    return int("".join(in_str_list))


def parse_input_b(in_str: str) -> Race:
    """parses the input as in part b"""
    time_line, dist_line = in_str.splitlines()

    return Race(
        _join_to_int(_parse_line_num(time_line, "Time:")),
        _join_to_int(_parse_line_num(dist_line, "Distance:")),
    )


def solve_b(in_str: str) -> int:
    """returns the solution for part_b"""
    return count_ways_to_win(parse_input_b(in_str))
