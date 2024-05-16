"""solution of adv_2023_10"""

import matplotlib.path


def _to_pos(in_x, in_y):
    return (in_x, in_y)


def parse_input(in_str):
    """parses the input into a dict and find the position of S"""
    res = {}
    s_pos = None
    for y_pos, row in enumerate(in_str.splitlines()[::-1]):
        for x_pos, char in enumerate(row):
            res[_to_pos(x_pos, y_pos)] = char
            if char == "S":
                assert s_pos is None
                s_pos = _to_pos(x_pos, y_pos)
    assert s_pos is not None
    return res, s_pos


def _change_dir(in_pipe, in_dir):
    pipes = {
        "F": {(0, 1): (1, 0), (-1, 0): (0, -1)},
        "L": {(0, -1): (1, 0), (-1, 0): (0, 1)},
        "7": {(0, 1): (-1, 0), (1, 0): (0, -1)},
        "J": {(0, -1): (-1, 0), (1, 0): (0, 1)},
    }
    if in_pipe in pipes:
        return pipes[in_pipe][in_dir]

    straigth_pipes = {"-": {(-1, 0), (1, 0)}, "|": {(0, -1), (0, 1)}}
    assert in_dir in straigth_pipes[in_pipe]
    return in_dir


def _shift(in_pos, in_dir):
    return tuple(_p + _s for _p, _s in zip(in_pos, in_dir))


def initial_dir(in_pipes, in_s_pos):
    """returns one of the possible initial loop dirs"""
    checks = {
        (0, 1): {"7", "F", "|"},
        (0, -1): {"J", "L", "|"},
        (1, 0): {"7", "J", "-"},
        (-1, 0): {"F", "L", "-"},
    }
    for cur_dir, pipes in checks.items():
        if in_pipes[_shift(in_s_pos, cur_dir)] in pipes:
            return cur_dir
    return None


def _find_loop(in_pipes, in_s_pos):
    assert in_pipes[in_s_pos] == "S"
    cur_dir = initial_dir(in_pipes, in_s_pos)
    cur_pos = _shift(in_s_pos, cur_dir)
    loop = []
    while in_pipes[cur_pos] != "S":
        loop.append(cur_pos)
        cur_dir = _change_dir(in_pipes[cur_pos], cur_dir)
        cur_pos = _shift(cur_pos, cur_dir)
    loop.append(in_s_pos)
    return loop


def solve_a(in_str):
    """returns the solution for part_a"""
    pipes, s_pos = parse_input(in_str)
    loop = _find_loop(pipes, s_pos)
    assert len(loop) % 2 == 0
    return len(loop) / 2


def solve_b(in_str):
    """returns the solution for part_b"""
    pipes, s_pos = parse_input(in_str)
    loop = _find_loop(pipes, s_pos)

    path = matplotlib.path.Path([_ for _ in loop if pipes[_] not in {"-", "|"}])
    loop_as_set = set(loop)
    return len(
        list(_ for _ in pipes if _ not in loop_as_set and path.contains_point(_))
    )
