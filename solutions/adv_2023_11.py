"""solution of adv_2023_11"""

import itertools


def _to_pos(in_x, in_y):
    return (in_x, in_y)


def parse_input(in_str):
    """parses the input into set of galaxies"""
    res = set()
    y_max = 0
    for y_pos, row in enumerate(in_str.splitlines()):
        x_max = len(row)
        y_max += 1
        for x_pos, char in enumerate(row):
            if char == "#":
                res.add(_to_pos(x_pos, y_pos))
    return res, x_max, y_max


def _get_empty(in_image, in_limit, in_exract):
    used = {in_exract(_) for _ in in_image}
    return {_ for _ in range(in_limit) if _ not in used}


def get_empty_rows(in_image, y_max):
    """returns indeces of empty rows"""
    return _get_empty(in_image, y_max, lambda pos: pos[1])


def get_empty_cols(in_image, x_max):
    """returns indeces of empty columns"""
    return _get_empty(in_image, x_max, lambda pos: pos[0])


def _gen_nums(in_a, in_b):
    assert in_a >= 0 and in_b >= 0
    yield from range(*sorted([in_a, in_b]))


def _compute_1d_dist(in_a, in_b, is_empty, empty_size):
    res = 0
    for _ in _gen_nums(in_a, in_b):
        res += 1
        if _ in is_empty:
            res += empty_size - 1
    return res


def compute_dist(in_pos_a, in_pos_b, empty_rows, empty_cols, empty_size):
    """computes the distance between two given positions"""
    return _compute_1d_dist(
        in_pos_a[0], in_pos_b[0], empty_cols, empty_size
    ) + _compute_1d_dist(in_pos_a[1], in_pos_b[1], empty_rows, empty_size)


def compute_sum_of_dists(in_str, in_empty_size):
    """computes the sum of all possible distances"""
    image, x_max, y_max = parse_input(in_str)
    empty_rows = get_empty_rows(image, y_max)
    empty_cols = get_empty_cols(image, x_max)
    return sum(
        compute_dist(*_, empty_rows, empty_cols, in_empty_size)
        for _ in itertools.combinations(image, 2)
    )


def solve_a(in_str):
    """returns the solution for part_a"""
    return compute_sum_of_dists(in_str, 2)


def solve_b(in_str):
    """returns the solution for part_b"""
    return compute_sum_of_dists(in_str, 1000000)
