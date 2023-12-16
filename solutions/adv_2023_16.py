"""solution of adv_2023_16"""

import collections


def _to_pos(in_x: int, in_y: int) -> tuple[int, int]:
    return (in_x, in_y)


def parse_input(in_str: str):
    """parses the input into a dict"""
    lines = in_str.splitlines()
    assert lines
    y_size = len(lines)
    x_size = len(lines[0])
    res = {}
    for y_pos, row in enumerate(lines):
        assert x_size == len(row)
        for x_pos, c in enumerate(row):
            res[_to_pos(x_pos, y_pos)] = c
    return res, x_size, y_size


State = collections.namedtuple("State", ["pos", "dir"])


def _shift(in_pos, in_dir):
    return tuple(_p + _s for _p, _s in zip(in_pos, in_dir))


_LEFT = (-1, 0)
_RIGHT = (1, 0)
_UP = (0, -1)
_DOWN = (0, 1)

_FLIPS = {
    "/": {_UP: _RIGHT, _LEFT: _DOWN, _RIGHT: _UP, _DOWN: _LEFT},
    "\\": {_UP: _LEFT, _RIGHT: _DOWN, _DOWN: _RIGHT, _LEFT: _UP},
}


def _flip_dir(in_dir, in_char):
    return _FLIPS[in_char][in_dir]


def _is_horizontal(in_dir):
    return in_dir in {_LEFT, _RIGHT}


def _is_vertical(in_dir):
    return in_dir in {_UP, _DOWN}


def _next_state(in_state):
    return State(_shift(in_state.pos, in_state.dir), in_state.dir)


def _is_simple_move(in_char, in_dir):
    if in_char == ".":
        return True
    if in_char == "-" and _is_horizontal(in_dir):
        return True
    if in_char == "|" and _is_vertical(in_dir):
        return True
    return False


def _propagate_beam(in_plan, in_start_state):
    stack = []

    def _append_if_needed(in_state):
        if in_state.pos in in_plan:
            stack.append(in_state)

    _append_if_needed(in_start_state)
    known_states = set()
    while stack:
        cur_state = stack.pop()
        if cur_state in known_states:
            continue
        known_states.add(cur_state)
        cur_char = in_plan[cur_state.pos]
        if cur_char in _FLIPS:
            new_dir = _flip_dir(cur_state.dir, cur_char)
            _append_if_needed(_next_state(State(cur_state.pos, new_dir)))
        elif _is_simple_move(cur_char, cur_state.dir):
            _append_if_needed(_next_state(cur_state))
        else:
            new_dirs = {"-": [_LEFT, _RIGHT], "|": [_UP, _DOWN]}
            for new_dir in new_dirs[cur_char]:
                _append_if_needed(_next_state(State(cur_state.pos, new_dir)))

    return {_.pos for _ in known_states}


def _count_energized(in_plan, in_start_state):
    return len(_propagate_beam(in_plan, in_start_state))


def solve_a(in_str: str) -> int:
    """returns the solution for part_a"""
    plan, _, _ = parse_input(in_str)
    return _count_energized(plan, State((0, 0), _RIGHT))


def _gen_all_start_states(x_size, y_size):
    for x_pos in range(x_size):
        yield State((x_pos, 0), _DOWN)
        yield State((x_pos, y_size - 1), _UP)
    for y_pos in range(y_size):
        yield State((0, y_pos), _RIGHT)
        yield State((x_size - 1, y_pos), _LEFT)


def solve_b(in_str: str) -> int:
    """returns the solution for part_b"""
    plan, x_size, y_size = parse_input(in_str)

    return max(_count_energized(plan, _) for _ in _gen_all_start_states(x_size, y_size))
