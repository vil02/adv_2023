"""solution of adv_2023_07"""

import functools
import itertools


def parse_input(in_str):
    """parses the input into a list of Games"""

    def _proc_single_line(in_line):
        hand, bid = in_line.split()
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


def _get_card_strenght(in_card):
    return _CARD_STRENGTH_A[in_card]


def _get_compare_hands(in_get_hand_strength, in_get_card_strength):
    def _compare_hands(hand_a, hand_b):
        kind_a = in_get_hand_strength(hand_a)
        kind_b = in_get_hand_strength(hand_b)
        if kind_a > kind_b:
            return 1
        if kind_b > kind_a:
            return -1
        assert kind_a == kind_b
        for _a, _b in zip(hand_a, hand_b):
            s_a = in_get_card_strength(_a)
            s_b = in_get_card_strength(_b)
            if s_a > s_b:
                return 1
            if s_b > s_a:
                return -1

        assert False
        return 0

    return _compare_hands


def _compute_total_score(in_data, in_cmp):
    hands = sorted(
        list(in_data.keys()),
        key=functools.cmp_to_key(in_cmp),
    )
    return sum(_r * in_data[_h] for _r, _h in enumerate(hands, 1))


def solve_a(in_str):
    """returns the solution for part_a"""
    return _compute_total_score(
        parse_input(in_str), _get_compare_hands(_get_hand_strength, _get_card_strenght)
    )


_NORMAL_CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def get_best_hand_type(in_hand):
    """
    returns the best hand type which can be obtained by replacing J by any other card
    """
    if "J" not in in_hand:
        return get_hand_type(in_hand)
    pos_of_js = [_p for _p, _c in enumerate(in_hand) if _c == "J"]
    best_hand = in_hand
    best_hand_strenght = _get_hand_strength(best_hand)
    for cur_subs in itertools.product(_NORMAL_CARDS, repeat=len(pos_of_js)):
        tmp_hand = list(in_hand)
        for _i, _p in enumerate(pos_of_js):
            tmp_hand[_p] = cur_subs[_i]
        tmp_hand = "".join(tmp_hand)
        cur_hand_strenght = _get_hand_strength(tmp_hand)
        if cur_hand_strenght > best_hand_strenght:
            best_hand = tmp_hand
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


def _get_card_strenght_b(in_card):
    return _CARD_STRENGTH_B[in_card]


def solve_b(in_str):
    """returns the solution for part_b"""
    return _compute_total_score(
        parse_input(in_str),
        _get_compare_hands(_get_best_hand_strenght, _get_card_strenght_b),
    )
