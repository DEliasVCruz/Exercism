def square(number):
    if number > 1 and number < 65:
        previous_number = number - 1
        previous_square = square(previous_number)
        return previous_square * 2
    elif number == 1:
        return 1
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    total_grains_on_the_board = 0
    for number in range(65):
        try:
            total_grains_on_the_board += square(number)
        except ValueError:
            pass
    return total_grains_on_the_board
