"""solution of adv_2023_01"""


def parse_input(in_str):
    """parses the input into list of lines"""
    return in_str.splitlines()


def _get_sum(in_str):
    return int(in_str[0] + in_str[-1])


def _extract_nums(in_str, in_nums):
    res = ""
    for cur_pos in range(len(in_str)):
        for _k, _v in in_nums.items():
            if in_str[cur_pos:].startswith(_k):
                res += _v
                break
    return res


def _get_num(in_str, in_nums):
    return _get_sum(_extract_nums(in_str, in_nums))


_NUMS_A = {str(_): str(_) for _ in range(1, 10)}


def solve_a(in_str):
    """returns the solution for part_a"""
    return sum(_get_num(_, _NUMS_A) for _ in parse_input(in_str))


_NUMS_B = _NUMS_A | {
    _k: str(_v)
    for _v, _k in enumerate(
        ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine"), 1
    )
}


def solve_b(in_str):
    """returns the solution for part_b"""
    return sum(_get_num(_, _NUMS_B) for _ in parse_input(in_str))
