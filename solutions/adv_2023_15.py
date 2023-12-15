"""solution of adv_2023_15"""


def _parse_input(in_str: str):
    return in_str.strip().split(",")


_HASH_SIZE = 256


def our_hash(in_str):
    """computes the HASH"""
    res = 0
    for _ in in_str:
        res += ord(_)
        res *= 17
        res %= _HASH_SIZE
    return res


def solve_a(in_str: str):
    """returns the solution for part_a"""
    data = _parse_input(in_str)

    return sum(our_hash(_) for _ in data)


class _Boxes:
    def __init__(self):
        self.boxes = {_: [] for _ in range(_HASH_SIZE)}

    def _replace_or_add(self, in_label, in_power):
        cur_box = our_hash(in_label)
        was_change = False
        for _ in self.boxes[cur_box]:
            if _[0] == in_label:
                _[1] = in_power
                was_change = True
        if not was_change:
            self.boxes[cur_box].append([in_label, in_power])

    def _remove(self, in_label):
        cur_box = our_hash(in_label)
        self.boxes[cur_box] = [_ for _ in self.boxes[cur_box] if _[0] != in_label]

    def proc(self, in_str):
        """processes a single string"""
        if "=" in in_str:
            cur_label, cur_power = in_str.split("=")
            self._replace_or_add(cur_label, int(cur_power))
        else:
            assert in_str[-1] == "-"
            self._remove(in_str[:-1])

    def compute_total_power(self):
        """computes the focusing power of all of the boxes"""
        res = 0
        for box_num, lenses in enumerate(self.boxes.values(), 1):
            for lense_num, lense in enumerate(lenses, 1):
                res += box_num * lense_num * lense[1]
        return res


def solve_b(in_str: str):
    """returns the solution for part_b"""
    data = _parse_input(in_str)
    boxes = _Boxes()
    for _ in data:
        boxes.proc(_)
    return boxes.compute_total_power()
