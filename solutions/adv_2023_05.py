"""solution of adv_2023_05"""

import collections

Interval = collections.namedtuple("Interval", ["begin", "end"])


def _is_not_empty(in_interval):
    return in_interval.begin < in_interval.end


class _MapRange:
    def __init__(self, in_dest_start, in_source_start, in_len):
        self.dest_start = in_dest_start
        self.source_start = in_source_start
        assert in_len > 0
        self.len = in_len

    def covers(self, in_val):
        """checks if in_val is in this _MapRange"""
        return self.source_start <= in_val <= self.source_start + self.len

    def map(self, in_val):
        """maps a single seed"""
        assert self.covers(in_val)
        diff = in_val - self.source_start
        return self.dest_start + diff

    def source_end(self):
        """returns the end of the interval"""
        return self.source_start + self.len

    def split(self, in_interval):
        """splits in_interval into tree part relative to this _MapRange"""
        before = Interval(in_interval.begin, min(in_interval.end, self.source_start))
        mid = Interval(
            max(in_interval.begin, self.source_start),
            min(self.source_end(), in_interval.end),
        )
        after = Interval(max(self.source_end(), in_interval.begin), in_interval.end)
        return before, mid, after


class _Map:
    def __init__(self, in_name, in_ranges):
        self.name = in_name
        self.ranges = in_ranges

    def map(self, in_val):
        """maps a single seed"""
        for _ in self.ranges:
            if _.covers(in_val):
                return _.map(in_val)
        return in_val

    def map_intervals(self, in_intervals):
        """maps intervals"""
        res = []
        tmp_intervas = in_intervals
        for _ in self.ranges:
            mapped_intervals = []
            while tmp_intervas:
                before, mid, after = _.split(tmp_intervas.pop())
                if _is_not_empty(before):
                    mapped_intervals.append(before)
                if _is_not_empty(mid):
                    res.append(Interval(_.map(mid.begin), _.map(mid.end)))
                if _is_not_empty(after):
                    mapped_intervals.append(after)
            tmp_intervas = mapped_intervals
        return res + tmp_intervas


def _parse_seeds(in_str):
    _, nums = in_str.split(": ")
    assert _ == "seeds"
    return [int(_) for _ in nums.split(" ")]


def _parse_map(in_str):
    lines = in_str.splitlines()
    name, _ = lines[0].split()
    assert _ == "map:"
    ranges = []
    for line in lines[1:]:
        dest_start_str, source_start_str, len_str = line.split()
        ranges.append(
            _MapRange(int(dest_start_str), int(source_start_str), int(len_str))
        )

    return _Map(name, ranges)


def parse_input(in_str):
    """parses the input into..."""

    pieces = in_str.split("\n\n")
    seeds = _parse_seeds(pieces[0])
    maps = [_parse_map(_) for _ in pieces[1:]]

    return seeds, maps


def _compute_final_location(in_seed, in_maps):
    cur = in_seed
    for _ in in_maps:
        cur = _.map(cur)
    return cur


def solve_a(in_str):
    """returns the solution for part_a"""
    seeds, maps = parse_input(in_str)
    return min(_compute_final_location(_, maps) for _ in seeds)


def _seeds_to_intervals(in_seeds):
    assert len(in_seeds) % 2 == 0
    res = []
    for _ in range(0, len(in_seeds), 2):
        res.append(Interval(in_seeds[_], in_seeds[_] + in_seeds[_ + 1]))
    return res


def _apply_all(maps, in_interval):
    res = [in_interval]
    for _ in maps:
        res = _.map_intervals(res)
    return res


def solve_b(in_str):
    """returns the solution for part_b"""
    seeds, maps = parse_input(in_str)
    intervals = _seeds_to_intervals(seeds)
    res_intervals = []
    for _ in intervals:
        res_intervals.extend(_apply_all(maps, _))

    return min(_.begin for _ in res_intervals)
