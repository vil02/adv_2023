"""solution of adv_2023_04"""

import collections

Card = collections.namedtuple("Card", ["id", "winning", "have"])


def _parse_card_id_str(in_str: str) -> int:
    _, id_str = in_str.split()
    assert _ == "Card"
    return int(id_str)


def _parse_numbers_str(in_str: str) -> set[int]:
    return {int(_) for _ in in_str.split()}


def _parse_card(in_str: str) -> Card:
    card_str, all_nums = in_str.split(": ")
    winning_str, have_str = all_nums.split(" | ")

    return Card(
        id=_parse_card_id_str(card_str),
        winning=_parse_numbers_str(winning_str),
        have=_parse_numbers_str(have_str),
    )


def _parse_input(in_str: str) -> list[Card]:
    return [_parse_card(_) for _ in in_str.splitlines()]


def _get_number_of_common(in_card: Card) -> int:
    return len(in_card.winning.intersection(in_card.have))


def _count_points(in_card: Card) -> int:
    common_len = _get_number_of_common(in_card)
    if common_len == 0:
        return 0
    return 2 ** (common_len - 1)


def solve_a(in_str: str) -> int:
    """returns the solution for part_a"""
    return sum(_count_points(_) for _ in _parse_input(in_str))


def _evaluate_stack(in_cards: list[Card]) -> int:
    hist = {_.id: 1 for _ in in_cards}
    total = 0
    for cur_card in in_cards:
        cur_id = cur_card.id
        cur_count = hist[cur_id]
        del hist[cur_id]
        total += cur_count
        for _ in range(_get_number_of_common(cur_card)):
            tmp_id = cur_id + 1 + _
            hist[tmp_id] += cur_count

    return total


def solve_b(in_str: str) -> int:
    """returns the solution for part_b"""
    return _evaluate_stack(_parse_input(in_str))
