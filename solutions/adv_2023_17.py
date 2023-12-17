"""solution of adv_2023_17"""

import collections
import heapq
import math


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
        for x_pos, val_str in enumerate(row):
            res[_to_pos(x_pos, y_pos)] = int(val_str)
    return res, x_size, y_size


Node = collections.namedtuple("Node", ["pos", "dir", "straight_moves"])


def _shift(in_pos, in_dir):
    return tuple(_p + _s for _p, _s in zip(in_pos, in_dir))


_W = (-1, 0)
_E = (1, 0)
_N = (0, -1)
_S = (0, 1)

_TURN_LEFT = {_N: _W, _W: _S, _S: _E, _E: _N}
_TURN_RIGHT = {_v: _k for _k, _v in _TURN_LEFT.items()}


def _next_node(in_node, new_dir=None):
    if new_dir is None:
        new_dir = in_node.dir
    new_pos = _shift(in_node.pos, new_dir)
    straight_moves = in_node.straight_moves + 1 if new_dir == in_node.dir else 1
    return Node(new_pos, new_dir, straight_moves)


def _next_nodes_a(in_node):
    assert 0 <= in_node.straight_moves <= 3
    res = []
    if in_node.straight_moves < 3:
        res.append(_next_node(in_node))
    res.append(_next_node(in_node, _TURN_LEFT[in_node.dir]))
    res.append(_next_node(in_node, _TURN_RIGHT[in_node.dir]))
    return res


def _find_best(in_plan, in_next_nodes, is_end):
    known_nodes = set()
    queue = []
    heapq.heappush(queue, (0, Node((0, 0), _E, 0)))
    heapq.heappush(queue, (0, Node((0, 0), _S, 0)))
    min_val = math.inf
    while queue:
        cur_cost, cur_node = heapq.heappop(queue)
        if is_end(cur_node):
            min_val = min(cur_cost, min_val)
            continue
        if cur_cost >= min_val or cur_node in known_nodes:
            continue
        known_nodes.add(cur_node)
        for new_node in in_next_nodes(cur_node):
            if new_node.pos in in_plan:
                heapq.heappush(queue, (cur_cost + in_plan[new_node.pos], new_node))
    return min_val


def solve_a(in_str: str) -> int:
    """returns the solution for part_a"""
    data, x_size, y_size = parse_input(in_str)
    return _find_best(
        data, _next_nodes_a, lambda cur_node: cur_node.pos == (x_size - 1, y_size - 1)
    )


_STOP_LIMIT = 3


def _next_nodes_b(in_node):
    res = []
    assert 0 <= in_node.straight_moves <= 10
    if in_node.straight_moves < 10:
        res.append(_next_node(in_node))
    if in_node.straight_moves > _STOP_LIMIT:
        res.append(_next_node(in_node, _TURN_LEFT[in_node.dir]))
        res.append(_next_node(in_node, _TURN_RIGHT[in_node.dir]))
    return res


def solve_b(in_str: str) -> int:
    """returns the solution for part_b"""
    data, x_size, y_size = parse_input(in_str)
    return _find_best(
        data,
        _next_nodes_b,
        lambda cur_node: cur_node.pos == (x_size - 1, y_size - 1)
        and cur_node.straight_moves > _STOP_LIMIT,
    )
