"""solution of adv_2023_25"""

import math
import networkx


def _parse_input(in_str: str):
    res = networkx.Graph()
    for cur_line in in_str.splitlines():
        start, nodes = cur_line.split(": ")
        for _ in nodes.split(" "):
            res.add_edge(start, _)
    return res


def solve_a(in_str: str) -> int:
    """returns the solution for part_a"""
    graph = _parse_input(in_str)
    edges_to_remove = networkx.minimum_edge_cut(graph)
    assert len(edges_to_remove) == 3
    graph.remove_edges_from(edges_to_remove)
    components = list(networkx.connected_components(graph))
    assert len(components) == 2
    return math.prod(len(_) for _ in components)
