"""solution of adv_2023_07"""


import collections

import functools
import itertools

Game = collections.namedtuple("Game", ["hand", "bid"])


def parse_input(in_str):
    """parses the input into a list of Games"""

    def _proc_single_line(in_line):
        hand, bid = in_line.split()
        # return Game(hand, int(bid))
        return hand, int(bid)

    return dict(_proc_single_line(_) for _ in in_str.splitlines())


def _count_cards_of_type(in_hand, in_type):
    return sum(1 for _ in in_hand if _ == in_type)


def _is_five_of_kind(in_hand):
    return len(set(in_hand)) == 1


def _is_four_of_kind(in_hand):
    unique = set(in_hand)
    if len(unique) == 2:
        return {1, 4} == {_count_cards_of_type(in_hand, _) for _ in unique}
    return False


def _is_full_house(in_hand):
    unique = set(in_hand)
    if len(unique) == 2:
        return {2, 3} == {_count_cards_of_type(in_hand, _) for _ in unique}
    return False


def _is_three_of_kind(in_hand):
    unique = set(in_hand)
    if len(unique) == 3:
        return [1, 1, 3] == sorted([_count_cards_of_type(in_hand, _) for _ in unique])
    return False


def _is_two_pair(in_hand):
    unique = set(in_hand)
    if len(unique) == 3:
        return [1, 2, 2] == sorted([_count_cards_of_type(in_hand, _) for _ in unique])
    return False


def _is_one_pair(in_hand):
    unique = set(in_hand)
    if len(unique) == 4:
        return [1, 1, 1, 2] == sorted(
            [_count_cards_of_type(in_hand, _) for _ in unique]
        )
    return False


def _is_high_card(in_hand):
    return len(set(in_hand)) == 5


def get_hand_type(in_hand):
    """returns the hand type"""
    # pylint: disable=too-many-return-statements
    if _is_five_of_kind(in_hand):
        return "five of kind"
    if _is_four_of_kind(in_hand):
        return "four of kind"
    if _is_full_house(in_hand):
        return "full house"
    if _is_three_of_kind(in_hand):
        return "three of kind"
    if _is_two_pair(in_hand):
        return "two pair"
    if _is_one_pair(in_hand):
        return "one pair"
    assert _is_high_card(in_hand)
    return "high card"


def _get_hand_strenght(in_hand):
    hand_kind = get_hand_type(in_hand)
    return {
        "five of kind": 7,
        "four of kind": 6,
        "full house": 5,
        "three of kind": 4,
        "two pair": 3,
        "one pair": 2,
        "high card": 1,
    }[hand_kind]


def _get_card_strenght(in_card):
    return {
        _c: _s + 1
        for _s, _c in enumerate(
            ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        )
    }[in_card]


def _get_stronger_hand(hand_a, hand_b):
    kind_a = _get_hand_strenght(hand_a)
    kind_b = _get_hand_strenght(hand_b)
    if kind_a > kind_b:
        return 1
    if kind_b > kind_a:
        return -1
    assert kind_a == kind_b
    for _a, _b in zip(hand_a, hand_b):
        s_a = _get_card_strenght(_a)
        s_b = _get_card_strenght(_b)
        if s_a > s_b:
            return 1
        if s_b > s_a:
            return -1

    assert False
    return 0


def solve_a(in_str):
    """returns the solution for part_a"""
    data = parse_input(in_str)
    hands = sorted(list(data.keys()), key=functools.cmp_to_key(_get_stronger_hand))
    res = 0
    for _r, _h in enumerate(hands):
        res += (_r + 1) * data[_h]

    return res


_NORMAL_CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def get_best_hand_type(in_hand):
    """
    returns the best hand type which can be obtained by replacing J by any other card
    """
    if "J" not in in_hand:
        return get_hand_type(in_hand)
    pos_of_js = [_p for _p, _c in enumerate(in_hand) if _c == "J"]
    best_hand = in_hand
    best_hand_strenght = _get_hand_strenght(best_hand)
    for cur_subs in itertools.product(_NORMAL_CARDS, repeat=len(pos_of_js)):
        tmp_hand = list(in_hand)
        for _i, _p in enumerate(pos_of_js):
            tmp_hand[_p] = cur_subs[_i]
        tmp_hand = "".join(tmp_hand)
        cur_hand_strenght = _get_hand_strenght(tmp_hand)
        if cur_hand_strenght > best_hand_strenght:
            best_hand = tmp_hand
            best_hand_strenght = cur_hand_strenght
        if best_hand_strenght == 7:
            break
    return get_hand_type(best_hand)


def _get_best_hand_strenght(in_hand):
    hand_kind = get_best_hand_type(in_hand)
    return {
        "five of kind": 7,
        "four of kind": 6,
        "full house": 5,
        "three of kind": 4,
        "two pair": 3,
        "one pair": 2,
        "high card": 1,
    }[hand_kind]


def _get_card_strenght_b(in_card):
    return {
        _c: _s + 1
        for _s, _c in enumerate(
            ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
        )
    }[in_card]


def _get_stronger_hand_b(hand_a, hand_b):
    kind_a = _get_best_hand_strenght(hand_a)
    kind_b = _get_best_hand_strenght(hand_b)
    if kind_a > kind_b:
        return 1
        # return hand_a
    if kind_b > kind_a:
        return -1
        # return hand_b
    assert kind_a == kind_b
    for _a, _b in zip(hand_a, hand_b):
        s_a = _get_card_strenght_b(_a)
        s_b = _get_card_strenght_b(_b)
        if s_a > s_b:
            return 1
            # return kind_a
        if s_b > s_a:
            return -1
            # return kind_b

    assert False
    return 0
    # return kind_a


def solve_b(in_str):
    """returns the solution for part_b"""
    data = parse_input(in_str)
    hands = sorted(list(data.keys()), key=functools.cmp_to_key(_get_stronger_hand_b))
    res = 0
    for _r, _h in enumerate(hands):
        res += (_r + 1) * data[_h]

    return res
