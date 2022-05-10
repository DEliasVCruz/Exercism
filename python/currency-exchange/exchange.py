def exchange_money(budget, exchange_rate):
    """Calculate the value of the exchanged currency

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Calculate the amount of money left after the exchange

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of the bill received

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """Calculate the number of bills that can be obtained

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value you can get through an exchange

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    true_exchange_rate = exchange_rate * (1 + spread / 100)
    new_currency = exchange_money(budget, true_exchange_rate)
    return new_currency - new_currency % denomination


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate amount not lost due to the denomination of the bills

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """

    true_exchange_rate = exchange_rate * (1 + spread / 100)
    new_currency = exchange_money(budget, true_exchange_rate)
    return int(new_currency % denomination)
