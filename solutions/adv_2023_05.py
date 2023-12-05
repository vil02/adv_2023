"""solution of adv_2023_05"""

import collections

Interval = collections.namedtuple("Interval", ["begin", "end"])


def is_not_empty(in_interval):
    """checks if the in_interval is not empty"""
    return in_interval.begin < in_interval.end


class IntervalShift:
    """represents a mapping described by single interval"""

    def __init__(self, in_dest_start, in_source_start, in_len):
        self._dest_start = in_dest_start
        self._source_start = in_source_start
        assert in_len > 0
        self._length = in_len

    def covers(self, in_val):
        """checks if in_val is in this interval"""
        return self._source_start <= in_val <= self.last_source()

    def __call__(self, in_val):
        """maps a single seed"""
        assert self.covers(in_val)
        diff = in_val - self._source_start
        return self._dest_start + diff

    def last_source(self):
        """returns the last value, which is mapped by this mapping"""
        return self._source_start + self._length

    def split(self, in_interval):
        """splits in_interval into tree part relative to this _MapRange"""
        before = Interval(in_interval.begin, min(in_interval.end, self._source_start))
        mid = Interval(
            max(in_interval.begin, self._source_start),
            min(self.last_source(), in_interval.end),
        )
        after = Interval(max(self.last_source(), in_interval.begin), in_interval.end)
        return before, mid, after


class _Map:
    def __init__(self, in_domain, in_target, in_ranges):
        self.domain = in_domain
        self.target = in_target
        self._shifts = in_ranges

    def __call__(self, in_val):
        for _ in self._shifts:
            if _.covers(in_val):
                return _(in_val)
        return in_val

    def _map_single_interval(self, in_shift, in_interval):
        before, mid, after = in_shift.split(in_interval)
        final_res = []
        if is_not_empty(mid):
            final_res.append(Interval(in_shift(mid.begin), in_shift(mid.end)))

        tmp_res = [_ for _ in [before, after] if is_not_empty(_)]
        return final_res, tmp_res

    def map_intervals(self, in_intervals):
        """mapps the in_intervals using all of the stored IntervalShifts"""
        res = []
        tmp_intervas = in_intervals
        for cur_shift in self._shifts:
            mapped_intervals = []
            for _ in tmp_intervas:
                final_res, tmp_res = self._map_single_interval(cur_shift, _)
                res.extend(final_res)
                mapped_intervals.extend(tmp_res)
            tmp_intervas = mapped_intervals
        return res + tmp_intervas


def _parse_seeds(in_str):
    _, nums = in_str.split(": ")
    assert _ == "seeds"
    return [int(_) for _ in nums.split(" ")]


def _parse_domain_target(in_str):
    domain, _, target = in_str.split("-")
    assert _ == "to"
    return domain, target


def _parse_map(in_str):
    lines = in_str.splitlines()
    name, _ = lines[0].split()
    assert _ == "map:"
    ranges = []
    for line in lines[1:]:
        dest_start_str, source_start_str, len_str = line.split()
        ranges.append(
            IntervalShift(int(dest_start_str), int(source_start_str), int(len_str))
        )

    return _Map(*_parse_domain_target(name), ranges)


def _parse_input(in_str):
    pieces = in_str.split("\n\n")
    seeds = _parse_seeds(pieces[0])
    maps = [_parse_map(_) for _ in pieces[1:]]

    for _ in range(len(maps) - 1):
        assert maps[_].target == maps[_ + 1].domain

    return seeds, maps


def _compute_final_location(in_seed, in_maps):
    cur = in_seed
    for _ in in_maps:
        cur = _(cur)
    return cur


def solve_a(in_str):
    """returns the solution for part_a"""
    seeds, maps = _parse_input(in_str)
    return min(_compute_final_location(_, maps) for _ in seeds)


def _seeds_to_intervals(in_seeds):
    return [Interval(_s, _s + _l) for _s, _l in zip(in_seeds[0::2], in_seeds[1::2])]


def _apply_all(maps, in_interval):
    res = [in_interval]
    for _ in maps:
        res = _.map_intervals(res)
    return res


def solve_b(in_str):
    """returns the solution for part_b"""
    seeds, maps = _parse_input(in_str)
    res_intervals = []
    for _ in _seeds_to_intervals(seeds):
        res_intervals.extend(_apply_all(maps, _))

    return min(_.begin for _ in res_intervals)
