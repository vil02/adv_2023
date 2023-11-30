"""general utilities for advent of code"""
import pathlib
import pytest


def _project_code():
    return "adv_2023"


def project_folder():
    """returns the path of the main folder of this project"""
    this_file_path = pathlib.Path(__file__)
    for _ in this_file_path.parents:
        if _.name == _project_code():
            res = _
            break
    else:
        raise RuntimeError("Wrong folder structure")
    return res.resolve()


def read_to_string(in_file_path):
    """reads a file to a string"""
    assert in_file_path.is_file()
    with open(in_file_path, "r", encoding="utf-8") as in_file:
        data_str = in_file.read()
    assert data_str
    return data_str


def input_data_folder():
    """returns the path of the with test input data"""
    res = project_folder() / "tests" / "test_input_data"
    assert res.is_dir()
    return res


def read_input(in_day_id, in_type_id):
    """returns specified test input as a string"""

    def _day_id_str(in_day_id):
        assert 0 <= in_day_id <= 25
        return str(in_day_id).zfill(2)

    f_name = f"data_{_project_code()}_{_day_id_str(in_day_id)}_{in_type_id}.txt"
    return read_to_string(input_data_folder() / f_name)


def get_all_inputs(in_day_id, in_keys):
    """returns a dict with all inputs for given in_day_id and data key"""
    res = {_: read_input(in_day_id, _) for _ in in_keys}
    assert len(set(res.values())) == len(res)
    return res


def _get_pytest_params(in_inputs, in_key_to_expected):
    return [
        pytest.param(in_inputs[key], val, id=key)
        for key, val in in_key_to_expected.items()
    ]


def get_test(in_fun, in_key_to_expected, in_inputs):
    """
    returns test, which checks the in_fun
    agains the data stored in in_inputs
    with expected retuls stored in in_key_to_expected
    """

    @pytest.mark.parametrize(
        "input_str,expected", _get_pytest_params(in_inputs, in_key_to_expected)
    )
    def _test_regular(input_str, expected):
        assert in_fun(input_str) == expected

    return _test_regular


def get_solve_tests(
    in_solve_a, in_key_to_expected_a, in_solve_b, in_key_to_expected_b, in_inputs
):
    """
    returns tests of the in_solve_a and in_solve_b functions
    """
    assert len(in_key_to_expected_a) == len(in_key_to_expected_b)
    return get_test(in_solve_a, in_key_to_expected_a, in_inputs), get_test(
        in_solve_b, in_key_to_expected_b, in_inputs
    )
