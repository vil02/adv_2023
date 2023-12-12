"""tests of adv_2023_12"""
import pytest

import test_utils as tu
import solutions.adv_2023_12 as sol


@pytest.mark.parametrize(
    "in_str, in_nums, expected",
    [
        ("???.###", (1, 1, 3), 1),
        (".??..??...?##.", (1, 1, 3), 4),
        ("?#?#?#?#?#?#?#?", (1, 3, 1, 6), 1),
        ("????.#...#...", (4, 1, 1), 1),
        ("????.######..#####.", (1, 6, 5), 4),
        ("?###????????", (3, 2, 1), 10),
    ],
)
def test_how_many(in_str, in_nums, expected):
    """checks how_many with example data"""
    assert sol.how_many(in_str, in_nums) == expected


@pytest.mark.parametrize(
    "in_str, in_nums, expected",
    [
        ("???.###", (1, 1, 3), 1),
        (".??..??...?##.", (1, 1, 3), 16384),
        ("?#?#?#?#?#?#?#?", (1, 3, 1, 6), 1),
        ("????.#...#...", (4, 1, 1), 16),
        ("????.######..#####.", (1, 6, 5), 2500),
        ("?###????????", (3, 2, 1), 506250),
    ],
)
def test_how_many_b(in_str, in_nums, expected):
    """checks how_many with expanded example data"""
    assert sol.how_many(*sol.expand(in_str, in_nums)) == expected


@pytest.mark.parametrize(
    "in_str, in_nums, expected",
    [
        (".#", (1,), (".#?.#?.#?.#?.#", (1, 1, 1, 1, 1))),
        (
            "???.###",
            (1, 1, 3),
            (
                "???.###????.###????.###????.###????.###",
                (1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3),
            ),
        ),
    ],
)
def test_expand(in_str, in_nums, expected):
    """tests expand with example data"""
    assert sol.expand(in_str, in_nums) == expected


_INPUTS = tu.get_inputs(12, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b), {"small": (21, 525152), "p": (7173, 29826669191291)}
)
