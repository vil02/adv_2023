"""solution of adv_2023_21"""


def _to_pos(in_x: int, in_y: int) -> tuple[int, int]:
    return (in_x, in_y)


_START = "S"


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
            if char == _START:
                s_pos = _to_pos(x_pos, y_pos)
    return res, x_size, y_size, s_pos


def _shift(in_pos, in_dir):
    return tuple(_p + _s for _p, _s in zip(in_pos, in_dir))


def _gen_new_positions(getter, in_pos):
    for shift in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        cur_pos = _shift(in_pos, shift)
        if getter(cur_pos) in {".", _START}:
            yield cur_pos


def _single_step(getter, in_positions):
    res = set()
    for cur_pos in in_positions:
        res.update(_gen_new_positions(getter, cur_pos))
    return res


def _make_steps(getter, in_positions, in_number_of_steps):
    reached = in_positions
    for _ in range(in_number_of_steps):
        reached = _single_step(getter, reached)
    return reached


def count_accessible(getter, in_start_pos, in_number_of_steps):
    """returns the number of filelds which can be reached in given number of steps"""
    assert getter(in_start_pos) == _START
    reached = _make_steps(getter, {in_start_pos}, in_number_of_steps)
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


def _compute_model(in_vals):
    diff_1 = _compute_diffs(in_vals)
    diff_2 = _compute_diffs(diff_1)
    return in_vals[-1], diff_1[-1], diff_2[-1]


def _extrapolate(in_vals, in_steps):
    assert len(in_vals) == 3
    return (
        in_vals[0] + in_steps * in_vals[1] + in_steps * (in_steps + 1) // 2 * in_vals[2]
    )


def _compute_quot_and_rem(total_steps, period):
    rem = total_steps % period
    quot = (total_steps - rem) // period
    assert total_steps == rem + quot * period
    return rem, quot


def _compute_diffs(in_vals):
    return [b - a for a, b in zip(in_vals[:-1], in_vals[1:])]


def _is_enough_data(in_values):
    if len(in_values) < 4:
        return False

    second_diffs = _compute_diffs(_compute_diffs(in_values))
    return second_diffs[-1] == second_diffs[-2]


def count_accessible_with_extrapolation(
    getter, in_period, in_start_pos, in_number_of_steps
):
    """returns the number of filelds which can be reached in given number of steps"""
    assert getter(in_start_pos) == _START
    rem, quot = _compute_quot_and_rem(in_number_of_steps, in_period)
    reached = _make_steps(getter, {in_start_pos}, rem)
    vals = [len(reached)]
    while not _is_enough_data(vals):
        reached = _make_steps(getter, reached, in_period)
        vals.append(len(reached))
    model = _compute_model(vals)
    return _extrapolate(model, quot - len(vals) + 1)


def solve_b(in_str: str):
    """returns the solution for part_b"""
    plan, x_size, y_size, start_pos = parse_input(in_str)
    getter = get_getter(plan, x_size, y_size)
    assert x_size == y_size
    return count_accessible_with_extrapolation(getter, x_size, start_pos, 26501365)
