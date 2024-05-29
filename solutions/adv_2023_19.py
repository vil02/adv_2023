"""solution of adv_2023_19"""

import collections
import functools

Condition = collections.namedtuple("Condition", ["check", "target", "part_type"])


def _parse_check(in_str: str):
    if "<" in in_str:
        part_type, limit = in_str.split("<")
        return lambda in_part: in_part[part_type] < int(limit), part_type
    assert ">" in in_str
    part_type, limit = in_str.split(">")
    return lambda in_part: in_part[part_type] > int(limit), part_type


def _parse_condition(in_str: str):
    if ":" in in_str:
        check_str, target = in_str.split(":")
        check, part_type = _parse_check(check_str)
        return Condition(check, target, part_type)
    return Condition(lambda _: True, in_str, None)


def _parse_workflow_conditions(in_str: str):
    return [_parse_condition(cur_piece) for cur_piece in in_str.split(",")]


_IN = "in"


def _parse_workflow_line(in_str: str):
    cur_name, conditions = in_str.split("{")
    assert conditions[-1] == "}"
    return cur_name, _parse_workflow_conditions(conditions[:-1])


def _parse_workflow(in_str: str):
    res = dict(_parse_workflow_line(_) for _ in in_str.splitlines())
    assert _IN in res
    return res


def _parse_piece_value(in_str: str):
    name, value = in_str.split("=")
    return name, int(value)


def _parse_piece(in_str: str):
    assert in_str[0] == "{"
    assert in_str[-1] == "}"
    return dict(_parse_piece_value(piece) for piece in in_str[1:-1].split(","))


def _parse_pieces(in_str: str):
    return [_parse_piece(_) for _ in in_str.splitlines()]


def _parse_input(in_str: str):
    workflow, pieces = in_str.split("\n\n")
    return _parse_workflow(workflow), _parse_pieces(pieces)


def _apply_conditions(in_conditions, in_piece):
    for cur_cond in in_conditions[:-1]:
        if cur_cond.check(in_piece):
            return cur_cond.target
    assert in_conditions[-1].check(in_piece)
    return in_conditions[-1].target


_ACCEPTED = "A"
_REJECTED = "R"


def _run_workflow(in_workflow, in_piece):
    cur_name = _IN
    while cur_name not in {_ACCEPTED, _REJECTED}:
        cur_name = _apply_conditions(in_workflow[cur_name], in_piece)
    return cur_name


def _is_accepted(in_name: str) -> bool:
    return {_ACCEPTED: True, _REJECTED: False}[in_name]


def _select_parts(in_workflow, in_pieces):
    return [
        piece for piece in in_pieces if _is_accepted(_run_workflow(in_workflow, piece))
    ]


def solve_a(in_str: str) -> int:
    """returns the solution for part_a"""
    workflow, pieces = _parse_input(in_str)
    accepted = _select_parts(workflow, pieces)
    return sum(sum(piece.values()) for piece in accepted)


def _split_range(in_range, in_cond):
    res_in = []
    res_out = []
    for _ in in_range:
        if in_cond.check({in_cond.part_type: _}):
            res_in.append(_)
        else:
            res_out.append(_)
    return res_in, res_out


def _count(in_workflow) -> int:
    def _count_single(in_state, ranges):
        if in_state == _ACCEPTED:
            return functools.reduce(lambda a, rg: a * len(rg), ranges.values(), 1)
        if in_state == _REJECTED:
            return 0
        res = 0
        for cur_cond in in_workflow[in_state]:
            if cur_cond.part_type is not None:
                new_in, new_out = _split_range(
                    ranges[cur_cond.part_type],
                    cur_cond,
                )
                tmp_ranges = dict(ranges.items())
                tmp_ranges[cur_cond.part_type] = new_in
                res += _count_single(cur_cond.target, tmp_ranges)
                ranges[cur_cond.part_type] = new_out
            else:
                res += _count_single(cur_cond.target, ranges)
        return res

    start_ranges = {_: list(range(1, 4001)) for _ in ["x", "m", "a", "s"]}
    return _count_single(_IN, start_ranges)


def solve_b(in_str: str) -> int:
    """returns the solution for part_b"""
    workflow, _ = _parse_input(in_str)
    return _count(workflow)
