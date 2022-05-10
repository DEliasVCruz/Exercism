SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):

    len_list_one = len(list_one)
    len_list_two = len(list_two)
    combined_length = len(list_one + list_two)

    if 0 < len_list_one == combined_length:
        return SUPERLIST

    if 0 < len_list_two == combined_length:
        return SUBLIST

    if list_one == list_two:
        return EQUAL

    if len_list_one < len_list_two:

        i = 0
        while i <= (len_list_two - len_list_one):
            if list_two[i:i + len_list_one] == list_one:
                return SUBLIST
            i += 1

    if len_list_one > len_list_two:

        i = 0
        while i <= (len_list_one - len_list_two):
            if list_one[i:i + len_list_two] == list_two:
                return SUPERLIST
            i += 1

    return UNEQUAL
