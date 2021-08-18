from PyDictionary import PyDictionary
dictionary = PyDictionary()
from nltk.corpus import wordnet

def Meaning(Word):
    """
    :param Message: The word that the user wants the definition of
    :return: meaning of the word
    """
    if len(Word.split(" ")) >= 2:
        return "1 word only"
    Def = dictionary.meaning(Word)
    return Def


def Synonym(Word):
    """
    :param Message: The word that the user wants the synonym of
    :return: synonyms of the word
    """
    if len(Word.split(" ")) >= 2:
        return "1 word only"

    synonyms = []
    for syn in wordnet.synsets(Word):
        for lm in syn.lemmas():
            synonyms.append(lm.name())
    return set(synonyms)


def Antonym(Word):
    """
    :param Message: The word that the user wants the antonym of
    :return: antonym of the word
    """
    if len(Word.split(" ")) >= 2:
        return "1 word only"

    antonyms = []
    for syn in wordnet.synsets(Word):
        for lm in syn.lemmas():
            if lm.antonyms():
                antonyms.append(lm.antonyms()[0].name())
    return set(antonyms)


