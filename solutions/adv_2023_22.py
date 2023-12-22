"""solution of adv_2023_22"""

import collections
import copy

Brick = collections.namedtuple("Brick", ["id", "pos_a", "pos_b"])


def _parse_pos(in_str):
    pieces = in_str.split(",")
    assert len(pieces) == 3
    return tuple(int(_) for _ in pieces)


def _parse_single_brick(in_id, in_str):
    pos_a, pos_b = in_str.split("~")
    return Brick(id=in_id, pos_a=_parse_pos(pos_a), pos_b=_parse_pos(pos_b))


def _parse_input(in_str: str):
    return [
        _parse_single_brick(brick_id, brick_str)
        for brick_id, brick_str in enumerate(in_str.splitlines())
    ]


def _sort_bricks(bricks):
    bricks.sort(key=_get_min_z)


def _get_min_z(in_brick: Brick) -> int:
    return min(in_brick.pos_a[2], in_brick.pos_b[2])


def _get_x(in_brick):
    assert in_brick.pos_a[0] == in_brick.pos_b[0]
    return in_brick.pos_a[0]


def _get_y(in_brick):
    assert in_brick.pos_a[1] == in_brick.pos_b[1]
    return in_brick.pos_a[1]


def _get_z(in_brick):
    assert in_brick.pos_a[2] == in_brick.pos_b[2]
    return in_brick.pos_a[2]


def _get_range(in_a, in_b):
    return range(min(in_a, in_b), max(in_a, in_b) + 1)


def _get_occupied_space(in_brick):
    if in_brick.pos_a[0] != in_brick.pos_b[0]:
        return [
            (_, _get_y(in_brick), _get_z(in_brick))
            for _ in _get_range(in_brick.pos_a[0], in_brick.pos_b[0])
        ]

    if in_brick.pos_a[1] != in_brick.pos_b[1]:
        return [
            (_get_x(in_brick), _, _get_z(in_brick))
            for _ in _get_range(in_brick.pos_a[1], in_brick.pos_b[1])
        ]

    if in_brick.pos_a[2] != in_brick.pos_b[2]:
        return [
            (_get_x(in_brick), _get_y(in_brick), _)
            for _ in _get_range(in_brick.pos_a[2], in_brick.pos_b[2])
        ]

    assert in_brick.pos_a == in_brick.pos_b
    return [in_brick.pos_a]


def _move_in_z(in_occupied_space, new_z):
    if len({_[2] for _ in in_occupied_space}) == 1:
        return [(_[0], _[1], new_z) for _ in in_occupied_space]
    min_z = min(_[2] for _ in in_occupied_space)
    z_shift = new_z - min_z
    return [(_[0], _[1], _[2] + z_shift) for _ in in_occupied_space]


def _does_not_intersect(other_bricks, this_brick):
    return all(_ not in other_bricks for _ in this_brick)


def _find_min_z_space(in_space, in_brick_space):
    this_brick_space = copy.copy(in_brick_space)
    cur_z = _min_z_of_occupied_space(this_brick_space)
    while cur_z >= 0 and _does_not_intersect(in_space, this_brick_space):
        cur_z -= 1
        this_brick_space = _move_in_z(this_brick_space, cur_z)
    return cur_z + 1


def _find_min_z(in_space, in_brick):
    this_brick_space = _get_occupied_space(in_brick)
    return _find_min_z_space(in_space, this_brick_space)


def _fall(in_bricks):
    space_to_id = {}
    id_to_space = {}
    for brick in in_bricks:
        min_z = _find_min_z(space_to_id, brick)
        tmp_space = _move_in_z(_get_occupied_space(brick), min_z)

        for _ in tmp_space:
            assert _ not in space_to_id
            space_to_id[_] = brick.id
        id_to_space[brick.id] = tmp_space
    return space_to_id, id_to_space


def _max_z_of_occupied_space(in_brick_space):
    return max(_[2] for _ in in_brick_space)


def _min_z_of_occupied_space(in_brick_space):
    return min(_[2] for _ in in_brick_space)


def _get_all_xy(in_brick_space):
    return {(_[0], _[1]) for _ in in_brick_space}


def _get_supports(space_to_id, id_to_space):
    supports = {}
    for cur_id, cur_brick_space in id_to_space.items():
        supports[cur_id] = set()
        cur_z = 1 + _max_z_of_occupied_space(cur_brick_space)
        for cur_xy in _get_all_xy(cur_brick_space):
            cur_pos = (cur_xy[0], cur_xy[1], cur_z)
            if cur_pos in space_to_id:
                supports[cur_id].add(space_to_id[cur_pos])
    return supports


def _get_supported_by(space_to_id, id_to_space):
    supported_by = {}
    for cur_id, cur_brick_space in id_to_space.items():
        supported_by[cur_id] = set()
        cur_z = _min_z_of_occupied_space(cur_brick_space) - 1
        for cur_xy in _get_all_xy(cur_brick_space):
            cur_pos = (cur_xy[0], cur_xy[1], cur_z)
            if cur_pos in space_to_id:
                supported_by[cur_id].add(space_to_id[cur_pos])
    return supported_by


def _can_be_removed(in_id, supports, supported_by):
    for tmp_id in supports[in_id]:
        if len(supported_by[tmp_id].difference({in_id})) == 0:
            return False
    return True


def _count(space_to_id, id_to_space):
    supports = _get_supports(space_to_id, id_to_space)
    supported_by = _get_supported_by(space_to_id, id_to_space)
    return sum(
        1
        for cur_id in id_to_space.keys()
        if _can_be_removed(cur_id, supports, supported_by)
    )


def solve_a(in_str: str):
    """returns the solution for part_a"""
    bricks = _parse_input(in_str)
    _sort_bricks(bricks)
    space_to_id, id_to_space = _fall(bricks)
    return _count(space_to_id, id_to_space)


def _count_different(org_id_to_space, tmp_id_to_space):
    res = 0
    for cur_id, cur_pos in tmp_id_to_space.items():
        if org_id_to_space[cur_id] != cur_pos:
            res += 1
    return res


def solve_b(in_str: str):
    """returns the solution for part_b"""
    bricks = _parse_input(in_str)
    _sort_bricks(bricks)
    new_bricks = []
    for new_id, brick in enumerate(bricks):
        new_bricks.append(Brick(id=new_id, pos_a=brick.pos_a, pos_b=brick.pos_b))
    bricks = new_bricks
    _, org_id_to_space = _fall(bricks)
    res = 0
    for brick_num, brick in enumerate(bricks):
        assert brick_num == brick.id
        tmp_bricks = copy.copy(bricks)
        del tmp_bricks[brick_num]
        _, tmp_id_to_space = _fall(tmp_bricks)
        res += _count_different(org_id_to_space, tmp_id_to_space)
    return res
