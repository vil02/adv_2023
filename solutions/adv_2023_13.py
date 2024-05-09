"""solution of adv_2023_13"""

import copy


def _to_pos(in_x: int, in_y: int) -> tuple[int, int]:
    return (in_x, in_y)


def _parse_single(in_str: str):
    lines = in_str.splitlines()
    assert lines
    y_size = len(lines)
    x_size = len(lines[0])
    res = {}
    for y_pos, row in enumerate(lines):
        assert x_size == len(row)
        for x_pos, c in enumerate(row):
            res[_to_pos(x_pos + 1, y_pos + 1)] = c
    return res, x_size, y_size


def parse_input(in_str):
    """returns a list of dicts representing the image and its sizes"""
    return [_parse_single(_) for _ in in_str.split("\n\n")]


def _pos_range(in_size):
    return range(1, in_size + 1)


def _gen_col_positons(in_col, y_size):
    return (_to_pos(in_col, _) for _ in _pos_range(y_size))


def _gen_row_positons(in_row, x_size):
    return (_to_pos(_, in_row) for _ in _pos_range(x_size))


def _get_col(in_image_dict, in_col, y_size):
    return [in_image_dict[_] for _ in _gen_col_positons(in_col, y_size)]


def _get_row(in_image_dict, in_row, x_size):
    return [in_image_dict[_] for _ in _gen_row_positons(in_row, x_size)]


def _compute_score_sum(in_cols, in_rows):
    return sum(in_cols) + 100 * sum(in_rows)


def _gen_pairs(in_start_val, in_limit):
    small = in_start_val
    big = small + 1
    while small > 0 and big <= in_limit:
        yield small, big
        small -= 1
        big += 1


class _Image:
    def __init__(self, in_image_dict, in_x_size, in_y_size):
        self._image_dict = in_image_dict
        self._x_size = in_x_size
        self._y_size = in_y_size
        self._cols = {}
        self._rows = {}

    def _get_col(self, in_col):
        if in_col not in self._cols:
            self._cols[in_col] = _get_col(self._image_dict, in_col, self._y_size)
        return self._cols[in_col]

    def _get_row(self, in_row):
        if in_row not in self._rows:
            self._rows[in_row] = _get_row(self._image_dict, in_row, self._x_size)
        return self._rows[in_row]

    def _is_symmetric_col(self, in_col):
        for left_col, right_col in _gen_pairs(in_col, self._x_size):
            if self._get_col(left_col) != self._get_col(right_col):
                return False
        return True

    def _is_symmetric_row(self, in_row):
        for up_row, bo_row in _gen_pairs(in_row, self._y_size):
            if self._get_row(up_row) != self._get_row(bo_row):
                return False
        return True

    def find_sym_cols(self):
        """returns row nums which are at the symmetry axis"""
        return {_ for _ in range(1, self._x_size) if self._is_symmetric_col(_)}

    def find_sym_rows(self):
        """returns col nums which are at the symmetry axis"""
        return {_ for _ in range(1, self._y_size) if self._is_symmetric_row(_)}


def _compute_sym_data(in_image_dict, x_size, y_size):
    cur_image = _Image(in_image_dict, x_size, y_size)
    return cur_image.find_sym_cols(), cur_image.find_sym_rows()


def compute_sym_score(in_image_dict, x_size, y_size):
    """computes symmetry score for given image"""
    sym_col, sym_row = _compute_sym_data(in_image_dict, x_size, y_size)
    return _compute_score_sum(sym_col, sym_row)


def solve_a(in_str: str):
    """returns the solution for part_a"""
    return sum(compute_sym_score(*_) for _ in parse_input(in_str))


def _flip(in_char):
    return {".": "#", "#": "."}[in_char]


def _get_image_with_flipped(in_image_dict, in_pos):
    res = copy.copy(in_image_dict)
    res[in_pos] = _flip(res[in_pos])
    return res


def find_smuge(in_image_dict, x_size, y_size):
    """returns the new symmetric columns and rows"""
    org_cols, org_rows = _compute_sym_data(in_image_dict, x_size, y_size)
    for _ in in_image_dict:
        tmp_cols, tmp_rows = _compute_sym_data(
            _get_image_with_flipped(in_image_dict, _), x_size, y_size
        )
        if (tmp_cols or tmp_rows) and (tmp_cols != org_cols or tmp_rows != org_rows):
            return tmp_cols.difference(org_cols), tmp_rows.difference(org_rows)
    return None


def _compute_sym_score_b(in_image_dict, x_size, y_size):
    cols, rows = find_smuge(in_image_dict, x_size, y_size)
    return _compute_score_sum(cols, rows)


def solve_b(in_str: str):
    """returns the solution for part_b"""
    return sum(_compute_sym_score_b(*_) for _ in parse_input(in_str))
