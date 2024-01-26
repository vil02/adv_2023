"""solution of adv_2023_24"""

import collections
import itertools
import sympy

Heil = collections.namedtuple("Heil", ["pos", "vel"])


def _parse_vec(in_str):
    pieces = in_str.split(", ")
    assert len(pieces) == 3
    return tuple(int(_) for _ in pieces)


def _parse_heil(in_str):
    pos_str, vel_str = in_str.split(" @ ")
    return Heil(pos=_parse_vec(pos_str), vel=_parse_vec(vel_str))


def parse_input(in_str: str):
    """parses the inputs into a list of Heils"""
    return [_parse_heil(_) for _ in in_str.splitlines()]


def _get_position(in_heil, in_t):
    return [p + in_t * v for p, v in zip(in_heil.pos, in_heil.vel)]


def _compute_coross_times(heil_a, heil_b):
    mat_a = sympy.Matrix(
        [
            [heil_b.vel[0], -heil_a.vel[0]],
            [heil_b.vel[1], -heil_a.vel[1]],
        ]
    )
    mat_b = sympy.Matrix(
        [
            [heil_a.pos[0] - heil_b.pos[0]],
            [heil_a.pos[1] - heil_b.pos[1]],
        ]
    )
    if mat_a.det() != 0:
        inv_a = mat_a.inv()
        sols = inv_a * mat_b
        return sols[1], sols[0]

    mat_a_x = sympy.Matrix(
        [
            [heil_a.pos[0] - heil_b.pos[0], -heil_a.vel[0]],
            [heil_a.pos[1] - heil_b.pos[1], -heil_a.vel[1]],
        ]
    )

    mat_a_y = sympy.Matrix(
        [
            [-heil_a.vel[0], heil_a.pos[0] - heil_b.pos[0]],
            [-heil_a.vel[1], heil_a.pos[1] - heil_b.pos[1]],
        ]
    )
    assert mat_a_x.det() != 0 or mat_a_y.det() != 0
    return None, None


def _is_inside_xy(in_pos, min_val, max_val):
    return all(min_val <= _ <= max_val for _ in in_pos[0:2])


def do_cross_xy(heil_a, heil_b, min_val, max_val):
    """
    checks if paths of two particles intersect:
    - for positive times
    - in a at the position with coordinates between min_val and max_val
    """
    t_a, t_b = _compute_coross_times(heil_a, heil_b)
    if t_a is not None and t_b is not None:
        if t_a > 0 and t_b > 0:
            pos_a = _get_position(heil_a, t_a)
            pos_b = _get_position(heil_b, t_b)
            assert pos_a[0:2] == pos_b[0:2]
            return _is_inside_xy(pos_a, min_val, max_val)
        return False
    return False


def count_crossing(in_heil_list, min_val, max_val):
    """counts the number of pairs of particles whose paths intersect as in part_a"""
    return sum(
        1
        for _ in itertools.combinations(in_heil_list, 2)
        if do_cross_xy(*_, min_val, max_val)
    )


def solve_a(in_str: str):
    """returns the solution for part_a"""
    return count_crossing(parse_input(in_str), 200000000000000, 400000000000000)


def _get_result_rock(solution):
    res_pos = [solution[0][0], solution[0][1], solution[0][2]]
    res_vel = [solution[0][3], solution[0][4], solution[0][5]]
    return Heil(pos=res_pos, vel=res_vel)


def _get_equations(in_heil_list, rock_pos_vars, rock_vel_vars, time_vars):
    res = []
    for heil, cur_time in zip(in_heil_list, time_vars):
        for _, (rock_start_pos, rock_vel) in enumerate(
            zip(rock_pos_vars, rock_vel_vars)
        ):
            cur_rock_pos = rock_start_pos + cur_time * rock_vel
            cur_heil_pos = heil.pos[_] + cur_time * heil.vel[_]
            res.append(sympy.Eq(cur_heil_pos, cur_rock_pos))
    return res


def _find_rock(in_heil_list):
    assert len(in_heil_list) >= 3
    rx, ry, rz = sympy.symbols("rx, ry, rz")
    vrx, vry, vrz = sympy.symbols("vrx, vry, vrz")
    ta, tb, tc = sympy.symbols("ta, tb, tc")
    equations = _get_equations(
        in_heil_list,
        [rx, ry, rz],
        [vrx, vry, vrz],
        [ta, tb, tc],
    )
    return _get_result_rock(
        sympy.solve(equations, [rx, ry, rz, vrx, vry, vrz, ta, tb, tc])
    )


def solve_b(in_str: str):
    """returns the solution for part_b"""
    heils = parse_input(in_str)
    return sum(_find_rock(heils).pos)
