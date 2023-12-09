"""solution of adv_2023_09"""


def _parse_input(in_str):
    def _proc_single_line(in_line):
        return [int(_) for _ in in_line.split()]

    return [_proc_single_line(_) for _ in in_str.splitlines()]


def _compute_diffs(in_list):
    return [in_list[_ + 1] - in_list[_] for _ in range(len(in_list) - 1)]


def extrapolate_right(in_list):
    """returns the extrapolated value on the right"""
    diffs = _compute_diffs(in_list)
    if all(_ == 0 for _ in diffs):
        return in_list[-1]
    return in_list[-1] + extrapolate_right(diffs)


def _sum_of_extrapolated(in_data, in_extrapolate):
    return sum(in_extrapolate(_) for _ in in_data)


def solve_a(in_str):
    """returns the solution for part_a"""
    return _sum_of_extrapolated(_parse_input(in_str), extrapolate_right)


def extrapolate_left(in_list):
    """returns the extrapolated value on the left"""
    diffs = _compute_diffs(in_list)
    if all(_ == 0 for _ in diffs):
        return in_list[0]
    return in_list[0] - extrapolate_left(diffs)


def solve_b(in_str):
    """returns the solution for part_b"""
    return _sum_of_extrapolated(_parse_input(in_str), extrapolate_left)
