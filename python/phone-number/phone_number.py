import re


def check_invalid_character(number):
    if re.search(r"[a-b]", number):
        raise ValueError("letters not permitted")
    if re.search(r"[@:!]", number):
        raise ValueError("punctuations not permitted")


def check_length_errors(strip_number, length):
    if length < 10:
        raise ValueError("incorrect number of digits")
    if length > 11:
        raise ValueError("more than 11 digits")
    if length == 11:
        country_code = strip_number[0]
        if country_code != "1":
            raise ValueError("11 digits must start with 1")
        strip_number = strip_number[1:]
    return strip_number


def check_valid_codes(area_code, exchange_code):
    if area_code[0] == "0":
        raise ValueError("area code cannot start with zero")
    if area_code[0] == "1":
        raise ValueError("area code cannot start with one")
    if exchange_code[0] == "0":
        raise ValueError("exchange code cannot start with zero")
    if exchange_code[0] == "1":
        raise ValueError("exchange code cannot start with one")


class PhoneNumber:
    def __init__(self, number):
        check_invalid_character(number)
        strip_number = re.sub(r"\D", "", number)
        length = len(strip_number)
        strip_number = check_length_errors(strip_number, length)
        area_code = strip_number[:3]
        exchange_code = strip_number[3:6]
        subscriber_number = strip_number[6:]
        check_valid_codes(area_code, exchange_code)
        self.area_code = area_code
        self.exchange_code = exchange_code
        self.subscriber = subscriber_number
        self.number = strip_number

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber}"
