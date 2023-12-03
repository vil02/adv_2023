"""solution of adv_2023_03"""


def parse_input(in_str):
    """parses the input into dict"""
    res = {}
    for _y, _r in enumerate(in_str.splitlines()):
        for _x, _c in enumerate(_r):
            res[(_x, _y)] = _c
    return res


def _get_x_start(in_data, in_pos):
    x_pos = in_pos[0]
    while x_pos >= 0 and in_data[(x_pos, in_pos[1])].isdigit():
        x_pos -= 1
    return x_pos + 1


def _get_number(in_data, in_pos):
    assert in_data[in_pos].isdigit()
    x_start = _get_x_start(in_data, in_pos)
    res = ""
    cur_x = x_start
    while (cur_x, in_pos[1]) in in_data and in_data[(cur_x, in_pos[1])].isdigit():
        res += in_data[(cur_x, in_pos[1])]
        cur_x += 1
    return res, (x_start, in_pos[1])


def _get_positions_nearby(in_data, in_start_pos):
    def _yield_vertical(in_x, center_y, in_shifts):
        for _ in in_shifts:
            cur_pos = (in_x, center_y + _)
            if cur_pos in in_data:
                yield cur_pos

    _x, _y = in_start_pos
    yield from _yield_vertical(_x - 1, _y, [-1, 0, 1])

    while (_x, _y) in in_data and in_data[(_x, _y)].isdigit():
        yield from _yield_vertical(_x, _y, [-1, 1])
        _x += 1

    yield from _yield_vertical(_x, _y, [-1, 0, 1])


def _is_near(data, in_start_pos, is_interesting):
    for _ in _get_positions_nearby(data, in_start_pos):
        if is_interesting(data[_]):
            return True, _
    return False, None


def _get_engine_parts(in_data):
    res = {}
    for _ in in_data:
        if in_data[_].isdigit():
            num, pos = _get_number(in_data, _)
            if pos not in res:
                res[pos] = num
    return res


def solve_a(in_str):
    """returns the solution for part_a"""
    data = parse_input(in_str)
    engine_parts = _get_engine_parts(data)
    return sum(
        int(_n)
        for _p, _n in engine_parts.items()
        if _is_near(data, _p, lambda c: c != ".")[0]
    )


def _get_all_gears(in_data):
    engine_parts = _get_engine_parts(in_data)
    res = {}
    for pos, num in engine_parts.items():
        is_near_gear, gear_pos = _is_near(in_data, pos, lambda c: c == "*")
        if is_near_gear:
            if gear_pos not in res:
                res[gear_pos] = []
            res[gear_pos].append(int(num))
    return res


def solve_b(in_str):
    """returns the solution for part_b"""
    gears = _get_all_gears(parse_input(in_str))
    return sum(_[0] * _[1] for _ in gears.values() if len(_) == 2)
