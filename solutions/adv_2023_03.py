"""solution of adv_2023_03"""

import typing

Position: typing.TypeAlias = tuple[int, int]
Data: typing.TypeAlias = dict[Position, str]


def parse_input(in_str: str) -> Data:
    """parses the input into dict"""
    res = {}
    for _y, _r in enumerate(in_str.splitlines()):
        for _x, _c in enumerate(_r):
            res[(_x, _y)] = _c
    return res


def _get_symbol_positions(
    in_data: Data, in_is_symbol: typing.Callable[[str], bool]
) -> set[Position]:
    return {_p for _p, _c in in_data.items() if in_is_symbol(_c)}


def _get_positions_around(
    in_data: Data, in_pos: Position
) -> typing.Generator[tuple[int, int], None, None]:
    _x, _y = in_pos
    for _ in [
        (_x, _y + 1),
        (_x + 1, _y + 1),
        (_x + 1, _y),
        (_x + 1, _y - 1),
        (_x, _y - 1),
        (_x - 1, _y - 1),
        (_x - 1, _y),
        (_x - 1, _y + 1),
    ]:
        assert _ in in_data
        yield _


def _find_numbers_around(in_data: Data, in_pos: Position) -> dict[Position, int]:
    res = {}
    for _ in _get_positions_around(in_data, in_pos):
        if in_data[_].isdigit():
            num, pos = _get_number(in_data, _)
            res[pos] = num
    return res


def _get_x_start(in_data: Data, in_pos: Position) -> int:
    x_pos = in_pos[0]
    while x_pos >= 0 and in_data[(x_pos, in_pos[1])].isdigit():
        x_pos -= 1
    return x_pos + 1


def _get_number(in_data: Data, in_pos: Position) -> tuple[int, tuple[int, int]]:
    assert in_data[in_pos].isdigit()
    x_start = _get_x_start(in_data, in_pos)
    res = ""
    cur_x = x_start
    while (cur_x, in_pos[1]) in in_data and in_data[(cur_x, in_pos[1])].isdigit():
        res += in_data[(cur_x, in_pos[1])]
        cur_x += 1
    return int(res), (x_start, in_pos[1])


def _get_all_parts(in_data: Data) -> typing.Iterable[int]:
    res = {}
    for _ in _get_symbol_positions(in_data, lambda c: not c.isdigit() and c != "."):
        for _p, _n in _find_numbers_around(in_data, _).items():
            res[_p] = _n
    return res.values()


def solve_a(in_str: str) -> int:
    """returns the solution for part_a"""
    return sum(_get_all_parts(parse_input(in_str)))


def _get_all_gears(in_data: Data) -> list[list[int]]:
    res = []
    for gear_pos in _get_symbol_positions(in_data, lambda c: c == "*"):
        nums = list(_find_numbers_around(in_data, gear_pos).values())
        if len(nums) == 2:
            res.append(nums)
    return res


def solve_b(in_str: str) -> int:
    """returns the solution for part_b"""
    return sum(_[0] * _[1] for _ in _get_all_gears(parse_input(in_str)))
