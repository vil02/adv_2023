"""solution of adv_2023_01"""


def parse_input(in_str):
    """parses the input into list of lines"""

    return in_str.splitlines()


def _get_sum(in_str):
    return int(in_str[0] + in_str[-1])


def _get_num(in_line):
    res = ""
    for _ in in_line:
        if _ in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}:
            res += _
    return _get_sum(res)


def solve_a(in_str):
    """returns the solution for part_a"""
    return sum(_get_num(_) for _ in parse_input(in_str))


def _get_num_b(in_line):
    nums = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    res = ""
    for cur_pos in range(len(in_line)):
        for _k, _v in nums.items():
            if in_line[cur_pos:].startswith(_k):
                res += nums[_v]
                break
    return _get_sum(res)


def solve_b(in_str):
    """returns the solution for part_b"""
    return sum(_get_num_b(_) for _ in parse_input(in_str))
