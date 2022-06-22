from typing import List, Any
from collections import Counter

def numbers(number: int) -> Any:
    return lambda score: sum([roll for roll in score if roll == number])


def straight(type: List[int]) -> Any:
    return lambda score: 30 if (sorted(score) == list(range(*type))) else 0


def house(type: str) -> function:

    def house(score: List[int]) -> int:
        counts: Counter = Counter(score)
        values: List = list(counts.values())
        max_value: int = max(values)

        if type == "four" and max_value >= 4:
            return max(counts) * 4

        if type == "full" and max_value == 3 and min(values) == 2:
            return sum(score)

        return 0


    return house


YACHT = lambda score: 50 if (len(set(score)) == 1) else 0
ONES = numbers(1)
TWOS = numbers(2)
THREES = numbers(3)
FOURS = numbers(4)
FIVES = numbers(5)
SIXES = numbers(6)
FULL_HOUSE = house("full")
FOUR_OF_A_KIND = house("four")
LITTLE_STRAIGHT = straight([1, 6])
BIG_STRAIGHT = straight([2, 7])
CHOICE = sum


def score(dice: List[int], category):
    return category(dice)
