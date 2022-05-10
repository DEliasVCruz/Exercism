def capitalize_title(title):
    """Capitalize every word in the title

    :param title: str title string that needs title casing
    :return:  str title string in title case (first letters capitalized)
    """
    words = title.split(" ")
    title_as_list = []
    for word in words:
        # The str.capitalize() method only does so for the first word in a string
        title_as_list.append(word.capitalize())
    title = " ".join(title_as_list)
    return title


def check_sentence_ending(sentence):
    """Determine if the sentence ends with a period

    :param sentence: str a sentence to check.
    :return:  bool True if punctuated correctly with period, False otherwise.
    """

    return bool(sentence[-1] == ".")


def clean_up_spacing(sentence):
    """Remove trailing spaces

    :param sentence: str a sentence to clean of leading and trailing space characters.
    :return: str a sentence that has been cleaned of leading and trailing space characters.
    """
    start = 0
    end = 0
    for character, _ in enumerate(sentence):
        if sentence[character] != " " and start == 0:
            start += character
        if sentence[character * -1] != " " and end == 0:
            end += len(sentence) - character + 1
            print(end)
    sentence = sentence[start:end]
    return sentence


clean_up_spacing("  A rolling stone gathers no moss")


def replace_word_choice(sentence, old_word, new_word):
    """Replace the word of choice

    :param sentence: str a sentence to replace words in.
    :param old_word: str word to replace
    :param new_word: str replacement word
    :return:  str input sentence with new words in place of old words
    """

    words = sentence.split(" ")
    if old_word in words or (old_word + ".") in words:
        try:
            index = words.index(old_word)
        except ValueError:
            index = words.index(old_word + ".")
        if words[index][-1] == ".":
            new_word += "."
        words.insert(index, new_word)
        try:
            words.remove(old_word)
        except ValueError:
            words.remove(old_word + ".")
        sentence = " ".join(words)

    return sentence
