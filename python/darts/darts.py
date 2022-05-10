def score(x, y):
    inner_square_radius = 1
    middle_square_radius = 5 ** 2
    outer_squre_radius = 10 ** 2
    point = (x) ** 2 + (y) ** 2

    if point <= inner_square_radius:
        return 10
    if point <= middle_square_radius:
        return 5
    if point <= outer_squre_radius:
        return 1

    return 0
