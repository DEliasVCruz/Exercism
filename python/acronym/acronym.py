import re


def abbreviate(words):
    words = words.upper()
    words = re.sub("-|_", " ", words)
    words = re.split(r"\s+", words)

    acronym = []
    for word in words:
        acronym.append(word[0])

    acronym = "".join(acronym)

    return acronym
