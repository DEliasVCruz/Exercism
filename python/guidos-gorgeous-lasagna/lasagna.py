EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    elapsed_bake_time = int(elapsed_bake_time)

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate time spendt making #n number of layers.
    :param number_of_layers: int number of layers in the lasagna.
    :return: int preparation time defived from 'PREPARATION_TIME'.

    A function that takes the number of added layers to the lasagna
    and return how much time in minutes will it take to preparate
    assuming that each layer takes 2 minuts to prepare
    """

    number_of_layers = int(number_of_layers)
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed cooking time.
    :param number_of_layers: int number of layers in the lasagna.
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int total number of minutes cooking

    A function that returns the sum of your preparation time and the time the
    lasagna has already spent baking in the oven
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
