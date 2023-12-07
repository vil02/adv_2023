"""solution of adv_2023_07"""

import functools
import itertools
import collections


def _parse_input(in_str):
    def _proc_single_line(in_line):
        hand, bid = in_line.split()
        return hand, int(bid)

    return dict(_proc_single_line(_) for _ in in_str.splitlines())


def _compute_characteristic(in_hand):
    return tuple(sorted(collections.Counter(in_hand).values()))


_CHARACTERISTIC_TO_KIND = {
    (5,): "five of kind",
    (1, 4): "four of kind",
    (2, 3): "full house",
    (1, 1, 3): "three of kind",
    (1, 2, 2): "two pair",
    (1, 1, 1, 2): "one pair",
    (1, 1, 1, 1, 1): "high card",
}


def get_hand_type(in_hand):
    """returns the hand type"""
    return _CHARACTERISTIC_TO_KIND[_compute_characteristic(in_hand)]


_HAND_TO_STRENGTH = {
    "five of kind": 7,
    "four of kind": 6,
    "full house": 5,
    "three of kind": 4,
    "two pair": 3,
    "one pair": 2,
    "high card": 1,
}


def _get_hand_strength(in_hand):
    return _HAND_TO_STRENGTH[get_hand_type(in_hand)]


_CARD_STRENGTH_A = {
    _c: _s + 1
    for _s, _c in enumerate(
        ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    )
}


def _cmp(in_a, in_b):
    if in_a > in_b:
        return 1
    if in_a < in_b:
        return -1
    assert in_a == in_b
    return 0


def _get_compare_hands(in_get_hand_strength, in_get_card_strength):
    def _compare_hands(hand_a, hand_b):
        if _ := _cmp(in_get_hand_strength(hand_a), in_get_hand_strength(hand_b)):
            return _
        for _a, _b in zip(hand_a, hand_b):
            if _ := _cmp(in_get_card_strength[_a], in_get_card_strength[_b]):
                return _

        return 0

    return _compare_hands


def _compute_total_score(in_data, in_cmp):
    hands = sorted(in_data.keys(), key=functools.cmp_to_key(in_cmp))
    return sum(_r * in_data[_h] for _r, _h in enumerate(hands, 1))


cmp_a = _get_compare_hands(_get_hand_strength, _CARD_STRENGTH_A)


def solve_a(in_str):
    """returns the solution for part_a"""
    return _compute_total_score(_parse_input(in_str), cmp_a)


def _substitute(in_hand, in_sub_positions, in_substitution):
    res = list(in_hand)
    for _i, _p in enumerate(in_sub_positions):
        res[_p] = in_substitution[_i]
    return "".join(res)


def _gen_hands(in_hand):
    normal_hands = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    pos_of_js = [_p for _p, _c in enumerate(in_hand) if _c == "J"]
    for cur_subs in itertools.product(normal_hands, repeat=len(pos_of_js)):
        yield _substitute(in_hand, pos_of_js, cur_subs)


@functools.lru_cache(maxsize=None)
def get_best_hand_type(in_hand):
    """
    returns the best hand type which can be obtained by replacing J by any other card
    """
    best_hand = in_hand
    best_hand_strenght = _get_hand_strength(best_hand)
    for cur_hand in _gen_hands(in_hand):
        cur_hand_strenght = _get_hand_strength(cur_hand)
        if cur_hand_strenght > best_hand_strenght:
            best_hand = cur_hand
            best_hand_strenght = cur_hand_strenght
        if best_hand_strenght == 7:
            break
    return get_hand_type(best_hand)


def _get_best_hand_strenght(in_hand):
    return _HAND_TO_STRENGTH[get_best_hand_type(in_hand)]


_CARD_STRENGTH_B = {
    _c: _s
    for _s, _c in enumerate(
        ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"], 1
    )
}


cmp_b = _get_compare_hands(_get_best_hand_strenght, _CARD_STRENGTH_B)


def solve_b(in_str):
    """returns the solution for part_b"""
    return _compute_total_score(_parse_input(in_str), cmp_b)
