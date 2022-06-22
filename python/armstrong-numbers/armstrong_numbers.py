from typing import List

def is_armstrong_number(number: int):
    numbers: List[int] = [int(num) for num in str(number)]
    digits: int = len(numbers)
    result: int = sum([num ** digits for num in numbers])

    return result == number
