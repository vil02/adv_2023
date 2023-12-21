"""solution of adv_2023_21"""


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
        for x_pos, char in enumerate(row):
            res[_to_pos(x_pos, y_pos)] = char
            if char == "S":
                s_pos = _to_pos(x_pos, y_pos)
    return res, x_size, y_size, s_pos


def _shift(in_pos, in_dir):
    return tuple(_p + _s for _p, _s in zip(in_pos, in_dir))


_W = (-1, 0)
_E = (1, 0)
_N = (0, -1)
_S = (0, 1)


def _gen_all_shifted(getter, in_pos, visited, cur_step):
    for shift in [_W, _E, _N, _S]:
        cur_pos = _shift(in_pos, shift)
        if getter(cur_pos) in {".", "S"} and (cur_pos, cur_step - 1) not in visited:
            yield cur_pos


def count_accessible(getter, in_start_pos, in_steps):
    """returns the number of filelds which can be reached in given number of steps"""
    assert getter(in_start_pos) == "S"
    visited = {(in_start_pos, in_steps)}
    reached = set()
    positions = [(in_start_pos, in_steps)]
    while positions:
        cur_pos, cur_step = positions.pop()
        if cur_step == 0:
            reached.add(cur_pos)
            continue
        visited.add((cur_pos, cur_step))

        for new_pos in _gen_all_shifted(getter, cur_pos, visited, cur_step):
            positions.append((new_pos, cur_step - 1))

    return len(reached)


def get_getter(in_plan, in_x_size, in_y_size):
    """returns a getter for infinite plan"""

    def _get(in_pos):
        in_x, in_y = in_pos
        return in_plan[_to_pos(in_x % in_x_size, in_y % in_y_size)]

    return _get


def solve_a(in_str: str):
    """returns the solution for part_a"""
    plan, x_size, y_size, start_pos = parse_input(in_str)
    getter = get_getter(plan, x_size, y_size)

    return count_accessible(getter, start_pos, 64)


def _single_iteration(in_a, in_b, in_c):
    res_c = in_c
    res_b = in_b + res_c
    res_a = in_a + res_b
    return res_a, res_b, res_c


def _iterate(initial_vals, in_iterations):
    cur_vals = initial_vals
    for _ in range(in_iterations):
        cur_vals = _single_iteration(*cur_vals)
    return cur_vals


def _compute_diffs(in_vals):
    diff_0 = in_vals[-2] - in_vals[-3]
    res_b = in_vals[-1] - in_vals[-2]
    res_c = res_b - diff_0
    return in_vals[-1], res_b, res_c


def solve_b(in_str: str):
    """returns the solution for part_b"""
    plan, x_size, y_size, start_pos = parse_input(in_str)
    getter = get_getter(plan, x_size, y_size)
    assert x_size == y_size

    steps = 26501365
    rem = steps % x_size
    quot = (steps - rem) // x_size
    assert steps == rem + quot * x_size
    vals = [count_accessible(getter, start_pos, rem + _ * x_size) for _ in range(3)]
    # vals = [3867, 34253, 94909]
    initial_vals = _compute_diffs(vals)
    return _iterate(initial_vals, quot - 2)[0]
