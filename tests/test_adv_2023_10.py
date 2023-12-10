"""tests of adv_2023_10"""

import test_utils as tu
import solutions.adv_2023_10 as sol


_INPUTS = tu.get_inputs(
    10, {"small", "small_b", "small_c", "small_d", "small_e", "small_wrong", "p"}
)


def test_initial_dir_is_none_when_wrong_input():
    """checks if initial_dir returns None for inputs with no initial dir"""
    pipes, s_pos = sol.parse_input(_INPUTS.inputs["small_wrong"])
    assert sol.initial_dir(pipes, s_pos) is None


test_solve_a = _INPUTS.get_test(sol.solve_a, {"small": 4, "small_b": 8, "p": 6875})

test_solve_b = _INPUTS.get_test(
    sol.solve_b,
    {"small": 1, "small_b": 1, "small_c": 4, "small_d": 4, "small_e": 8, "p": 471},
)
