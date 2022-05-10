def is_triangle(sides):
    """Chech if the sides form a triangle

    :param sides: list - a list of three digits
    :return: bool - If it's a triangle
    """

    triangle_inequality = bool(2 * max(sides) <= sum(sides))
    return bool(all(sides) and triangle_inequality)


def equilateral(sides):
    """Check if the sides form an equilateral triangle

    :param sides: list - a list of three digits
    :return: bool - If it's a equilateral triangle
    """

    return bool(is_triangle(sides) * bool(len(set(sides)) == 1))


def isosceles(sides):
    """Check if the sides form an isosceles triangle

    :param sides: list - a list of three digits
    :return: bool - If it's a isosceles triangle
    """

    return bool(is_triangle(sides) * bool(len(set(sides)) <= 2))


def scalene(sides):
    """Check if the sides form an scalene triangle

    :param sides: list - a list of three digits
    :return: bool - If it's a scalene triangle
    """

    return bool(is_triangle(sides) * bool(len(set(sides)) == 3))
