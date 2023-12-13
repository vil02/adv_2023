"""solution of adv_2023_13"""
import copy


def _to_pos(in_x: int, in_y: int) -> tuple[int, int]:
    return (in_x, in_y)


def _parse_single(in_str: str):
    res = {}
    y_size = 0
    for y_pos, row in enumerate(in_str.splitlines()):
        x_size = len(row)
        for x_pos, c in enumerate(row):
            res[_to_pos(x_pos + 1, y_pos + 1)] = c
        y_size += 1
    return res, x_size, y_size


def parse_input(in_str):
    """returns a list of dicts representing the image and its sizes"""
    return [_parse_single(_) for _ in in_str.split("\n\n")]


def _get_col(in_image, in_col, y_size):
    return [in_image[_to_pos(in_col, _)] for _ in range(1, y_size + 1)]


def _get_row(in_image, in_row, x_size):
    return [in_image[_to_pos(_, in_row)] for _ in range(1, x_size + 1)]


def _is_symmetric_col(in_image, in_col, x_size, y_size):
    left_col = in_col
    right_col = in_col + 1
    while left_col > 0 and right_col <= x_size:
        left_col_data = _get_col(in_image, left_col, y_size)
        right_col_data = _get_col(in_image, right_col, y_size)
        if left_col_data != right_col_data:
            return False
        left_col -= 1
        right_col += 1
    return True


def _find_sym_col(in_image, x_size, y_size):
    res = []
    for _ in range(1, x_size):
        if _is_symmetric_col(in_image, _, x_size, y_size):
            res.append(_)
    return res


def _is_symmetric_row(in_image, in_row, x_size, y_size):
    up_row = in_row + 1
    bo_row = in_row
    while bo_row > 0 and up_row <= y_size:
        up_row_data = _get_row(in_image, up_row, x_size)
        bo_row_data = _get_row(in_image, bo_row, x_size)
        if up_row_data != bo_row_data:
            return False
        bo_row -= 1
        up_row += 1
    return True


def _find_sym_row(in_image, x_size, y_size):
    res = []
    for _ in range(1, y_size):
        if _is_symmetric_row(in_image, _, x_size, y_size):
            res.append(_)
    return res


def _compute_score_sum(in_cols, in_rows):
    return sum(in_cols) + 100 * sum(in_rows)


def compute_sym_score(in_image, x_size, y_size):
    """computes symmetry score for given image"""
    sym_col = _find_sym_col(in_image, x_size, y_size)
    sym_row = _find_sym_row(in_image, x_size, y_size)
    return _compute_score_sum(sym_col, sym_row)


def solve_a(in_str: str):
    """returns the solution for part_a"""
    data = parse_input(in_str)
    return sum(compute_sym_score(*_) for _ in data)


def _flip(in_char):
    return "." if in_char == "#" else "#"


def _get_image_with_flipped(in_image, in_pos):
    res = copy.copy(in_image)
    res[in_pos] = _flip(res[in_pos])
    return res


def find_smuge(in_image, x_size, y_size):
    """returns the new symmetric collumns and rows"""
    org_cols = set(_find_sym_col(in_image, x_size, y_size))
    org_rows = set(_find_sym_row(in_image, x_size, y_size))
    for _ in in_image:
        tmp_img = _get_image_with_flipped(in_image, _)
        tmp_cols = set(_find_sym_col(tmp_img, x_size, y_size))
        tmp_rows = set(_find_sym_row(tmp_img, x_size, y_size))
        if (tmp_cols or tmp_rows) and (tmp_cols != org_cols or tmp_rows != org_rows):
            return tmp_cols.difference(org_cols), tmp_rows.difference(org_rows)
    return None


def _compute_sym_score_b(in_image, x_size, y_size):
    cols, rows = find_smuge(in_image, x_size, y_size)
    return _compute_score_sum(cols, rows)


def solve_b(in_str: str):
    """returns the solution for part_b"""
    data = parse_input(in_str)
    return sum(_compute_sym_score_b(*_) for _ in data)
