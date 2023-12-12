"""solution of adv_2023_12"""
import functools


def _parse_nums(in_str: str) -> tuple[int]:
    return tuple(int(_) for _ in in_str.split(","))


def _parse_line(in_str: str) -> tuple[str, tuple[int]]:
    data, nums = in_str.split()
    return data, _parse_nums(nums)


def _parse_input(in_str: str) -> list[tuple[str, tuple[int]]]:
    return [_parse_line(_) for _ in in_str.splitlines()]


@functools.lru_cache(maxsize=None)
def how_many(in_str: str, in_nums: tuple[int], size=None) -> int:
    """
    computes in how many ways '?' can be replaced in in_str
    such that in_nums are correct
    """
    if size is None:
        size = len(in_str)
    if len(in_nums) == 0:
        if all(_ in {".", "?"} for _ in in_str):
            return 1
        return 0
    cur_num = in_nums[0]
    rest_nums = in_nums[1:]
    tmp_size = sum(rest_nums) + len(rest_nums)
    res = 0
    for _ in range(size - tmp_size - cur_num + 1):
        tmp_str = "." * _ + "#" * cur_num + "."
        if all(_a in (_b, "?") for _a, _b in zip(in_str, tmp_str)):
            res += how_many(in_str[len(tmp_str) :], rest_nums, size - cur_num - _ - 1)

    return res


def solve_a(in_str: str) -> int:
    """returns the solution for part_a"""
    data = _parse_input(in_str)
    return sum(how_many(*_) for _ in data)


def expand(in_str: str, in_nums: tuple[int]) -> tuple[str, tuple[int]]:
    """expands the input data as described in part_b"""
    n_copies = 5
    res_str = "".join((in_str + "?") * n_copies)[:-1]
    res_nums: list[int] = []
    for _ in range(n_copies):
        res_nums.extend(in_nums)
    return (res_str, tuple(res_nums))


def solve_b(in_str: str) -> int:
    """returns the solution for part_b"""
    data = _parse_input(in_str)
    return sum(how_many(*expand(*_)) for _ in data)
