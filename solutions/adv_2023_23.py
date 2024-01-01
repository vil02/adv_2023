"""solution of adv_2023_23"""

import collections
import itertools


def _to_pos(in_x: int, in_y: int) -> tuple[int, int]:
    return (in_x, in_y)


def _parse_input(in_str: str):
    lines = in_str.splitlines()
    assert lines
    y_size = len(lines)
    x_size = len(lines[0])
    res = {}
    for y_pos, row in enumerate(lines):
        assert x_size == len(row)
        for x_pos, char in enumerate(row):
            res[_to_pos(x_pos, y_pos)] = char
    return res, x_size, y_size


_W = (-1, 0)
_E = (1, 0)
_N = (0, -1)
_S = (0, 1)

_SLIDES = {">": _E, "<": _W, "v": _S, "^": _N}

_ALL_DIRS = list(_SLIDES.values())


def _empty_graph(in_plan):
    return {
        cur_pos: Node(set(), set())
        for cur_pos, cur_char in in_plan.items()
        if cur_char != "#"
    }


Edge = collections.namedtuple("Edge", ["node_id", "length"])


def _add_edge(graph, start_id, end_id):
    graph[start_id].targets.add(Edge(end_id, 1))
    graph[end_id].sources.add(Edge(start_id, 1))


def _to_graph_a(in_plan):
    graph = _empty_graph(in_plan)

    for cur_pos, cur_char in in_plan.items():
        if in_plan[cur_pos] == ".":
            for cur_dir in _ALL_DIRS:
                tmp_pos = _shift(cur_pos, cur_dir)
                if tmp_pos in in_plan and in_plan[tmp_pos] != "#":
                    _add_edge(graph, cur_pos, tmp_pos)
        elif cur_char in _SLIDES:
            cur_dir = _SLIDES[cur_char]
            tmp_pos = _shift(cur_pos, cur_dir)
            assert tmp_pos in in_plan
            _add_edge(graph, cur_pos, tmp_pos)

    return graph


def _shift(in_pos, in_dir):
    return tuple(_p + _s for _p, _s in zip(in_pos, in_dir))


Node = collections.namedtuple("Node", ["sources", "targets"])


def _to_graph_b(in_plan):
    graph = _empty_graph(in_plan)
    for cur_pos, cur_char in in_plan.items():
        if cur_char != "#":
            for cur_dir in _ALL_DIRS:
                tmp_pos = _shift(cur_pos, cur_dir)
                if tmp_pos in in_plan and in_plan[tmp_pos] != "#":
                    _add_edge(graph, tmp_pos, cur_pos)
    return graph


def _is_trivial(in_node):
    if len(in_node.sources) == 2 and len(in_node.targets) == 2:
        return in_node.sources == in_node.targets
    return False


def _extract_from_trival(in_node):
    assert _is_trivial(in_node)
    return tuple(in_node.sources)


def _remove_edge(in_edges, id_to_remove):
    return {_ for _ in in_edges if _.node_id != id_to_remove}


def _prepare_edges(in_edges, id_to_remove, new_edge):
    res = _remove_edge(in_edges, id_to_remove)
    res.add(new_edge)
    return res


def _contracted_node(old_sources, old_targets, id_to_remove, new_edge):
    return Node(
        sources=_prepare_edges(old_sources, id_to_remove, new_edge),
        targets=_prepare_edges(old_targets, id_to_remove, new_edge),
    )


def _contract_single(graph):
    ids = list(graph.keys())
    for node_id in ids:
        if _is_trivial(graph[node_id]):
            in_edge, out_edge = _extract_from_trival(graph[node_id])
            new_len = in_edge.length + out_edge.length
            graph[in_edge.node_id] = _contracted_node(
                graph[in_edge.node_id].sources,
                graph[in_edge.node_id].targets,
                node_id,
                Edge(out_edge.node_id, new_len),
            )

            graph[out_edge.node_id] = _contracted_node(
                graph[out_edge.node_id].sources,
                graph[out_edge.node_id].targets,
                node_id,
                Edge(in_edge.node_id, new_len),
            )
            del graph[node_id]


def _check_graph(in_graph):
    for node in in_graph.values():
        assert all(
            _.node_id in in_graph for _ in itertools.chain(node.sources, node.targets)
        )


def _contract_all_edges(graph):
    cur_len = len(graph)
    _contract_single(graph)
    while len(graph) < cur_len:
        cur_len = len(graph)
        _contract_single(graph)
        _check_graph(graph)


def _find_longest(in_graph, start_id, end_id):
    assert start_id in in_graph
    assert end_id in in_graph
    longest = 0
    stack = [(0, start_id, {start_id})]
    while stack:
        moves, cur_id, cur_path = stack.pop(-1)
        if cur_id == end_id:
            longest = max(longest, moves)
            continue
        for new_edge in in_graph[cur_id].targets:
            if new_edge.node_id not in cur_path:
                stack.append(
                    (
                        moves + new_edge.length,
                        new_edge.node_id,
                        cur_path | {new_edge.node_id},
                    )
                )
    return longest


def _start_id():
    return (1, 0)


def _end_id(x_size, y_size):
    return (x_size - 2, y_size - 1)


def _get_solve_fun(in_to_graph_fun):
    def _solve(in_str):
        plan, x_size, y_size = _parse_input(in_str)
        graph = in_to_graph_fun(plan)
        _contract_all_edges(graph)
        return _find_longest(graph, _start_id(), _end_id(x_size, y_size))

    return _solve


solve_a = _get_solve_fun(_to_graph_a)
solve_b = _get_solve_fun(_to_graph_b)
