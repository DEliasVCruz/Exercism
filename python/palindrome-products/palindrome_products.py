from math import sqrt


def reverse_number(number, reverse=0):
    last_digit = number % 10
    reverse = reverse * 10 + last_digit
    number = number // 10
    if number == 0:
        return reverse
    return reverse_number(number, reverse)


def is_palindrom(number):
    reversed = reverse_number(number)
    return bool(number == reversed)


def divisors(number):
    divisor = 1
    factor_list = []
    while divisor <= sqrt(number):
        if number % divisor == 0:
            factor_list.append((divisor, int(number / divisor)))
        divisor += 1
    return factor_list


def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    spread = [x for x in range(min_factor, max_factor + 1)]
    factors = []
    for product in range(max_factor ** 2, (min_factor ** 2) - 1, -1):
        if is_palindrom(product):
            palindrom = product
            factor_list = divisors(palindrom)
            factors = [
                (element[0], element[1])
                for element in factor_list
                if element[0] in spread and element[1] in spread
            ]
            if len(factors) != 0:
                return (palindrom, factors)
    return (None, [])


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    spread = [x for x in range(min_factor, max_factor + 1)]
    products_spread = (x for x in range(min_factor ** 2, (max_factor ** 2) + 1))
    factors = []
    for product in products_spread:
        if is_palindrom(product):
            palindrom = product
            factor_list = divisors(palindrom)
            factors = [
                (element[0], element[1])
                for element in factor_list
                if element[0] in spread and element[1] in spread
            ]
            if len(factors) != 0:
                return (palindrom, factors)
    return (None, [])


if __name__ == "__main__":
    #  print(reverse_number(1))
    print(smallest(1, 9))
    print(largest(1, 9))
    #  print(smallest(10, 99))
    #  print(largest(10, 99))
    #  for divisor in divisors(9):
    #  print(divisor)
