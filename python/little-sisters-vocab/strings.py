def add_prefix_un(word):
    """Add un as a prefix to the word

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    return "un" + word


def make_word_groups(vocab_words):
    """Create a group of words with the disigned prefix

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    word_groups = []
    word_groups.append(vocab_words[0])
    for word in vocab_words[1:]:
        prefixed_word = vocab_words[0] + word
        word_groups.append(prefixed_word)
    word_groups = " :: ".join(word_groups)

    return word_groups


def remove_suffix_ness(word):
    """Remove the ness suffix from a word

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """

    lenght_of_word = len(word)
    un_suffixed_word_length = lenght_of_word - 4
    un_suffixed_word = word[:un_suffixed_word_length]
    if un_suffixed_word[-1] == "i":
        un_suffixed_word = un_suffixed_word[:un_suffixed_word_length - 1] + 'y'

    return un_suffixed_word


def noun_to_verb(sentence, index):
    """Turn the index word in a sentence into a verb

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """

    sentence = sentence[:len(sentence) - 1]
    words = sentence.split(" ")
    noun = words[index]
    verb = noun + "en"

    return verb
