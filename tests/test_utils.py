"""general utilities for advent of code"""

import dataclasses
import pathlib
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


def _day_id_str(in_day_id: int) -> str:
    assert 0 <= in_day_id <= 25
    return str(in_day_id).zfill(2)


def _input_file_name(in_day_id: int, in_type_id: str) -> str:
    return f"data_{_project_code()}_{_day_id_str(in_day_id)}_{in_type_id}.txt"


def _input_dir(in_day_id: int, in_type_id: str) -> pathlib.Path:
    if in_type_id == "p" and in_day_id > 0:
        return input_data_folder() / "p_inputs" / _project_code()
    return input_data_folder()


def _input_path(in_day_id: int, in_type_id: str) -> pathlib.Path:
    return _input_dir(in_day_id, in_type_id) / _input_file_name(in_day_id, in_type_id)


def _input_exists(in_day_id: int, in_type_id: str) -> bool:
    return _input_path(in_day_id, in_type_id).is_file()


def _read_input(in_day_id: int, in_type_id: str) -> str | None:
    """returns specified test input as a string"""
    if _input_exists(in_day_id, in_type_id):
        return read_to_string(_input_path(in_day_id, in_type_id))
    return None


def _read_all_inputs(in_day_id: int, in_keys: set[str]) -> dict[str, str | None]:
    """returns a dict with all inputs for given in_day_id and data key"""
    return {_: _read_input(in_day_id, _) for _ in in_keys}


type SolveOutput = int | str


def _extract_expected(
    in_key_to_all_expected: dict[str, tuple[SolveOutput, ...]], in_fun_num: int
) -> dict[str, SolveOutput]:
    return {_k: _v[in_fun_num] for _k, _v in in_key_to_all_expected.items()}


@dataclasses.dataclass(frozen=True)
class _Inputs:
    inputs: dict[str, str | None]

    def _get_pytest_param(self, key: str, expected: SolveOutput) -> typing.Any:
        if self.inputs[key] is not None:
            return pytest.param(self.inputs[key], expected, id=key)
        return pytest.param(
            self.inputs[key],
            expected,
            id=key,
            marks=pytest.mark.skip(reason="Input not available"),
        )

    def _get_pytest_params(
        self, in_key_to_expected: dict[str, SolveOutput]
    ) -> list[typing.Any]:
        return [
            self._get_pytest_param(key, expected)
            for key, expected in in_key_to_expected.items()
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
            ("input_str", "expected"), self._get_pytest_params(in_key_to_expected)
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
