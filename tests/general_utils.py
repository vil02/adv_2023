"""general utilities for advent of code"""
import pathlib
import functools


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


def test_input_data_folder():
    """returns the path of the with test input data"""
    res = project_folder() / "tests" / "test_input_data"
    assert res.is_dir()
    return res


@functools.lru_cache(None)
def read_input(in_day_id, in_type_id):
    """returns specified test input as a string"""

    def _day_id_str(in_day_id):
        assert 0 <= in_day_id <= 25
        return str(in_day_id).zfill(2)

    f_name = f"data_{_project_code()}_{_day_id_str(in_day_id)}_{in_type_id}.txt"
    return read_to_string(test_input_data_folder() / f_name)
