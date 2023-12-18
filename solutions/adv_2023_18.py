"""solution of adv_2023_18"""

import collections

Command = collections.namedtuple("Command", ["dir", "step", "color"])


def parse_input(in_str: str):
    """parses the input into list of Commands"""

    def _proc_single_line(in_line: str):
        direction, step, color = in_line.split()
        color = color[1:-1]
        return Command(direction, int(step), color)

    return [_proc_single_line(_) for _ in in_str.splitlines()]


def _parse_color(in_str):
    assert in_str[0] == "#"
    step = int("0x" + in_str[1:-1], 0)
    direction = {"0": "R", "1": "D", "2": "L", "3": "U"}[in_str[-1]]
    return Command(direction, step, None)


_L = (-1, 0)
_R = (1, 0)
_U = (0, 1)
_D = (0, -1)

_STR_TO_DIR = {"U": _U, "D": _D, "L": _L, "R": _R}


def _shift(in_pos, in_dir, in_step):
    return tuple(_p + in_step * _s for _p, _s in zip(in_pos, in_dir))


def _area(positions):
    return 0.5 * abs(
        sum(x0 * y1 - x1 * y0 for ((x0, y0), (x1, y1)) in _segments(positions))
    )


def _segments(positions):
    return zip(positions, positions[1:] + [positions[0]])


def _positions(in_plan):
    cur_pos = (0, 0)
    res = [cur_pos]

    for cur_command in in_plan:
        cur_pos = _shift(cur_pos, _STR_TO_DIR[cur_command.dir], cur_command.step)
        res.append(cur_pos)
    return res


def _edge_size(in_plan):
    return sum(_.step for _ in in_plan)


def _compute_total_area(in_plan):
    positions = _positions(in_plan)

    edge_size = _edge_size(in_plan)

    interior_pts = _area(positions) + 1 - edge_size / 2
    return int(interior_pts + edge_size)


def solve_a(in_str: str):
    """returns the solution for part_a"""
    return _compute_total_area(parse_input(in_str))


def solve_b(in_str: str):
    """returns the solution for part_b"""
    plan_a = parse_input(in_str)
    plan_b = [_parse_color(_.color) for _ in plan_a]
    return _compute_total_area(plan_b)
