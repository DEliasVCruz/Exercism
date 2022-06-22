def square_of_sum(number):
    n: int = number

    sum: float = ((n * (n + 1)) / 2) ** 2

    return sum


def sum_of_squares(number: int):
    n: int = number

    sum: float = (n * (n + 1) * (2 * n + 1)) / 6

    return sum


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
