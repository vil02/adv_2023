"""solution of adv_2023_14"""


def _to_pos(in_x: int, in_y: int) -> tuple[int, int]:
    return (in_x, in_y)


def parse_input(in_str: str):
    """parses the input into a dict"""
    lines = in_str.splitlines()
    assert lines
    y_size = len(lines)
    x_size = len(lines[0])
    res = {}
    for y_pos, row in enumerate(lines[::-1]):
        assert x_size == len(row)
        for x_pos, c in enumerate(row):
            res[_to_pos(x_pos + 1, y_pos + 1)] = c
    return res, x_size, y_size


def find_empty_north(in_image, y_size, x_pos, y_pos):
    """find the final y-position of the round rock while moving to the north"""
    cur_y_pos = y_pos + 1
    while cur_y_pos < y_size + 1 and in_image[_to_pos(x_pos, cur_y_pos)] == ".":
        cur_y_pos += 1
    return cur_y_pos - 1


def _to_string(in_image, x_size, y_size):
    res = []
    for y_pos in range(y_size, 0, -1):
        cur_row = []
        for x_pos in range(1, x_size + 1):
            cur_row.append(in_image[_to_pos(x_pos, y_pos)])
        res.append("".join(cur_row))
    return "\n".join(res)


def _tilt_north(image, x_size, y_size):
    for y_pos in range(y_size, 0, -1):
        for x_pos in range(1, x_size + 1):
            if image[_to_pos(x_pos, y_pos)] == "O":
                new_y_pos = find_empty_north(image, y_size, x_pos, y_pos)
                image[_to_pos(x_pos, y_pos)] = "."
                image[_to_pos(x_pos, new_y_pos)] = "O"
    return image


def _rotate_90(image, x_size, y_size):
    res = {}
    for pos, c in image.items():
        new_x = pos[1]
        new_y = x_size - pos[0] + 1
        res[_to_pos(new_x, new_y)] = c
    return res, y_size, x_size


def _compute_load_score(in_image):
    res = 0
    for pos, char in in_image.items():
        if char == "O":
            res += pos[1]
    return res


def solve_a(in_str: str):
    """returns the solution for part_a"""
    image, x_size, y_size = parse_input(in_str)
    _tilt_north(image, x_size, y_size)
    return _compute_load_score(image)


def _tilt_south(image, x_size, y_size):
    image, x_size, y_size = _rotate_90(image, x_size, y_size)
    image, x_size, y_size = _rotate_90(image, x_size, y_size)
    image = _tilt_north(image, x_size, y_size)
    image, x_size, y_size = _rotate_90(image, x_size, y_size)
    image, x_size, y_size = _rotate_90(image, x_size, y_size)
    return image


def _tilt_east(image, x_size, y_size):
    image, x_size, y_size = _rotate_90(image, x_size, y_size)
    image, x_size, y_size = _rotate_90(image, x_size, y_size)
    image, x_size, y_size = _rotate_90(image, x_size, y_size)
    image = _tilt_north(image, x_size, y_size)
    image, x_size, y_size = _rotate_90(image, x_size, y_size)
    return image


def _tilt_west(image, x_size, y_size):
    image, x_size, y_size = _rotate_90(image, x_size, y_size)
    image = _tilt_north(image, x_size, y_size)
    image, x_size, y_size = _rotate_90(image, x_size, y_size)
    image, x_size, y_size = _rotate_90(image, x_size, y_size)
    image, x_size, y_size = _rotate_90(image, x_size, y_size)
    return image


def _make_cycle(image, x_size, y_size):
    image = _tilt_north(image, x_size, y_size)
    image = _tilt_west(image, x_size, y_size)
    image = _tilt_south(image, x_size, y_size)
    image = _tilt_east(image, x_size, y_size)
    return image


def _compute_cycle_data(image, x_size, y_size):
    res = {}
    changes = {}
    move_num = 0
    while _to_string(image, x_size, y_size) not in res:
        res[_to_string(image, x_size, y_size)] = move_num
        image = _make_cycle(image, x_size, y_size)
        move_num += 1
        changes[move_num - 1] = move_num
    changes[move_num - 1] = res[_to_string(image, x_size, y_size)]
    return res, changes


def _compute_cycle_info(in_changes):
    max_key = max(in_changes.keys())
    first_of_cycle = in_changes[max_key]
    cycle_len = max_key - first_of_cycle

    return first_of_cycle, cycle_len + 1


def _compute_state(in_cycle_data, in_changes, in_cycle_num):
    first_of_cycle, cycle_len = _compute_cycle_info(in_changes)
    r_val = (in_cycle_num - first_of_cycle) % cycle_len
    reduced_move = r_val + first_of_cycle

    after_move = {_v: _k for _k, _v in in_cycle_data.items()}

    return after_move[reduced_move]


def solve_b(in_str: str):
    """returns the solution for part_b"""
    image, x_size, y_size = parse_input(in_str)
    cycle_data, changes = _compute_cycle_data(image, x_size, y_size)

    res_str = _compute_state(cycle_data, changes, 1000000000)
    new_image, _, _ = parse_input(res_str)
    return _compute_load_score(new_image)
