"""solution of adv_2023_08"""

import itertools
import math


def _parse_target(in_str):
    assert in_str[0] == "("
    assert in_str[-1] == ")"
    l_res, r_res = in_str[1:-1].split(", ")
    return l_res, r_res


def _parse_node(in_str):
    start_node, targets = in_str.split(" = ")
    return start_node, _parse_target(targets)


def _parse_nodes(in_str):
    return dict(_parse_node(_) for _ in in_str.splitlines())


def _parse_input(in_str):
    instructions, nodes = in_str.split("\n\n")
    return instructions, _parse_nodes(nodes)


def _gen_dirs(in_dirs):
    yield from itertools.cycle(in_dirs)


def _make_move(dirs, in_nodes, in_node):
    cur_turn = 1 if next(dirs) == "R" else 0
    return in_nodes[in_node][cur_turn]


def _iterate_till(dirs, in_nodes, in_start_node, is_end_fun):
    cur_node = in_start_node
    move_num = 0
    while not is_end_fun(cur_node):
        cur_node = _make_move(dirs, in_nodes, cur_node)
        move_num += 1
    return move_num, cur_node


def solve_a(in_str):
    """returns the solution for part_a"""
    dirs_str, nodes = _parse_input(in_str)
    move_num, _ = _iterate_till(_gen_dirs(dirs_str), nodes, "AAA", lambda n: n == "ZZZ")
    return move_num


def _is_start_node(in_node):
    return in_node[-1] == "A"


def _get_start_nodes(in_nodes):
    return [_ for _ in in_nodes.keys() if _is_start_node(_)]


def _proc_single_2(in_nodes, in_dirs_str, start_node):
    dirs = _gen_dirs(in_dirs_str)
    move_num, last_node = _iterate_till(
        dirs, in_nodes, start_node, lambda n: n[-1] == "Z"
    )
    next_node = _make_move(dirs, in_nodes, last_node)
    move_num_2, _ = _iterate_till(dirs, in_nodes, next_node, lambda n: n == last_node)
    move_num_2 += 1
    assert move_num == move_num_2
    return move_num


def solve_b(in_str):
    """returns the solution for part_b"""
    dirs_str, nodes = _parse_input(in_str)
    start_nodes = _get_start_nodes(nodes)
    return math.lcm(*[_proc_single_2(nodes, dirs_str, _) for _ in start_nodes])
