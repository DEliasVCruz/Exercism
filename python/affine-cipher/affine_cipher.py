import re


def check_if_coprime(a):
    if a % 2 == 0 or a % 13 == 0 or a % 26 == 0:
        raise ValueError("a and m must be coprime.")


def pre_process_string(string):
    processed_string = string.lower()
    processed_string = re.sub(r"\W", "", processed_string)
    return processed_string


def find_mmi(a):
    for candidate in range(1, 26):
        if (a * candidate) % 26 == 1:
            return candidate


def cypher(plain_text, a, b, process):
    check_if_coprime(a)
    message = pre_process_string(plain_text)
    new_message = ""
    for place, character in enumerate(message):
        if character.isdigit():
            new_message += character
            continue
        index = ord(character) - 97
        if process == 'encode':
            new_char = chr((a * index + b) % 26 + 97)
            if place % 5 == 0 and place != 0:
                new_message += " "
        else:
            mmi = find_mmi(a)
            new_char = chr((mmi * (index - b)) % 26 + 97)
        new_message += new_char
    return new_message


def encode(plain_text, a, b):
    encoded_message = cypher(plain_text, a, b, 'encode')
    return encoded_message


def decode(ciphered_text, a, b):
    decoded_message = cypher(ciphered_text, a, b, 'decode')
    return decoded_message
