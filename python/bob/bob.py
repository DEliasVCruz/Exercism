"""Set of responses Bob gives"""

import re


def response(statement):
    """Give a set of responses based on the given statment

    :param statement: str - a statement in the form of a string
    :return: str - a predifined response based on the statement

    It matches if the string follows a predefined pattern and gives
    one of a list of responses based on that pattern
    """

    # Remove withe trailing whitespace
    #  trailing_spaces = r"^[\s]+|[\s]+$"
    #  statement = re.sub(trailing_spaces, "", statement)
    statement = statement.strip()

    question = r".*\?$"
    shouting = r"^[^a-z]+[A-Z]+"
    shout_question = r"^[^a-z]+[A-Z]+\?$"

    if statement.expandtabs() == "":
        return "Fine. Be that way!"

    elif re.search(shout_question, statement):
        return "Calm down, I know what I'm doing!"

    elif re.search(question, statement):
        return "Sure."

    elif re.search(shouting, statement):
        return "Whoa, chill out!"

    return "Whatever."
