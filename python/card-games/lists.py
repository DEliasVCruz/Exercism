"""Counting awsome cards"""


def get_rounds(number):
    """Return a list of the current and next two rounds

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Return a single unified list of rounds

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    rounds_1.extend(rounds_2)
    return rounds_1


def list_contains_round(rounds, number):
    """Find if an specified round was played

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return bool(number in rounds)


def card_average(hand):
    """Find the average value of cards in hand

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Check if approximate averages are equal to average

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """

    median_index = int(len(hand) / 2)
    median = hand[median_index]
    aprox_average = (hand[0] + hand[-1]) / 2
    real_average = card_average(hand)

    return bool(real_average in (median, aprox_average))


def average_even_is_average_odd(hand):
    """Check if average of evens or odds is equal to real average

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    evens_and_odds = [[0, 0], [0, 0]]

    for index in range(len(hand)):
        if (index + 1) % 2 == 0:
            evens_and_odds[0][0] += hand[index]
            evens_and_odds[0][1] += 1
        else:
            evens_and_odds[1][0] += hand[index]
            evens_and_odds[1][1] += 1

    evens_average = evens_and_odds[0][0] / evens_and_odds[0][1]
    odds_average = evens_and_odds[1][0] / evens_and_odds[1][1]
    real_average = card_average(hand)

    return bool(real_average in (odds_average, evens_average))


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2

    return hand
