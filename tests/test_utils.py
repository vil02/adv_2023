"""general utilities for advent of code"""

import pathlib
import dataclasses
import typing
import pytest


def _project_code() -> str:
    return "adv_2023"


def project_folder() -> pathlib.Path:
    """returns the path of the main folder of this project"""
    this_file_path = pathlib.Path(__file__)
    for _ in this_file_path.parents:
        if _.name == _project_code():
            res = _
            break
    else:
        raise RuntimeError("Wrong folder structure")
    return res.resolve()


def read_to_string(in_file_path: pathlib.Path) -> str:
    """reads a file to a string"""
    assert in_file_path.is_file()
    with open(in_file_path, "r", encoding="utf-8") as in_file:
        data_str = in_file.read()
    assert data_str
    return data_str


def input_data_folder() -> pathlib.Path:
    """returns the path of the with test input data"""
    res = project_folder() / "tests" / "test_input_data"
    assert res.is_dir()
    return res


def _read_input(in_day_id: int, in_type_id: str) -> str:
    """returns specified test input as a string"""

    def _day_id_str(in_day_id: int) -> str:
        assert 0 <= in_day_id <= 25
        return str(in_day_id).zfill(2)

    f_name = f"data_{_project_code()}_{_day_id_str(in_day_id)}_{in_type_id}.txt"
    return read_to_string(input_data_folder() / f_name)


def _read_all_inputs(in_day_id: int, in_keys: set[str]) -> dict[str, str]:
    """returns a dict with all inputs for given in_day_id and data key"""
    res = {_: _read_input(in_day_id, _) for _ in in_keys}
    assert len(set(res.values())) == len(res)
    return res


SolveOutput: typing.TypeAlias = int | str


def _extract_expected(
    in_key_to_all_expected: dict[str, tuple[SolveOutput, ...]], in_fun_num: int
) -> dict[str, SolveOutput]:
    return {_k: _v[in_fun_num] for _k, _v in in_key_to_all_expected.items()}


@dataclasses.dataclass(frozen=True)
class _Inputs:
    inputs: dict[str, str]

    def _get_pytest_params(self, in_key_to_expected: dict[str, SolveOutput]) -> list:
        return [
            pytest.param(self.inputs[key], val, id=key)
            for key, val in in_key_to_expected.items()
        ]

    def get_test(
        self,
        in_fun: typing.Callable[[str], SolveOutput],
        in_key_to_expected: dict[str, SolveOutput],
    ) -> typing.Callable[[str, SolveOutput], None]:
        """
        returns test, which checks the in_fun
        against the data stored in self.inputs
        with expected result stored in in_key_to_expected
        """

        @pytest.mark.parametrize(
            "input_str,expected", self._get_pytest_params(in_key_to_expected)
        )
        def _test_regular(input_str: str, expected: SolveOutput) -> None:
            assert in_fun(input_str) == expected

        return _test_regular

    def get_tests(
        self,
        in_funcs: tuple[typing.Callable[[str], SolveOutput], ...],
        in_key_to_all_expected: dict[str, tuple[SolveOutput, ...]],
    ) -> tuple[typing.Callable[[str, SolveOutput], None], ...]:
        """returns a tuple of tests"""
        assert all(len(in_funcs) == len(_) for _ in in_key_to_all_expected.values())
        return tuple(
            self.get_test(cur_fun, _extract_expected(in_key_to_all_expected, fun_num))
            for fun_num, cur_fun in enumerate(in_funcs)
        )


def get_inputs(in_day_id: int, in_keys: set[str]) -> _Inputs:
    """returns an _Inputs object representing the data for given day/keys"""
    return _Inputs(_read_all_inputs(in_day_id, in_keys))
