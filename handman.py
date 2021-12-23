# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:56:53 2021

@author: justo
"""


#User Dict = {username, word, wordguessed, letters guessed, points, warnings, guess}
#GeneralDict = {username = (user Dict)}
import random
Users = {}


Wordlist = "words.txt"


def load_words():
    """

    :return: a wordlist list containing the words from the txt file
    """
    inFile = open(Wordlist, 'r')
    line = inFile.readline()
    wordlist = line.split()
    return wordlist

def chooseword(wordlist):
    """
    :param wordlist: a list containing all the words
    :return: returns a randomly chosen string from the list
    """
    return random.choice(wordlist)

def guesscheck(word, guess):
    """
    :param word: The word, in string type, the user is trying to guess
    :param guess: The guess, in string type, the user is trying to guess
    :return: returns True if guessed else False
    """
    if guess in word:
        return True
    return False

def updateword(guessedlist, word):
    """
    :param guessedlist: A list that contains the letters guessed
    :param word: The word, in string type, the user is trying to guess
    :return: returns the updated word filling the letters the user guessed
    """

    Updatedword = ""
    for i in word:
        if i in guessedlist:
            Updatedword += i
        else:
            Updatedword += "_ "

    if word == Updatedword:
        return True
    return Updatedword

def game(dict):
    Username = dict.get(Name)
    Word = dict.get(Word)
    Updatedword = dict.get(WordGuessed)
    Guesses = dict.get(LettersGuessed)
    PointsLeft = dict.get(Points)
    Warnings = dict.get(Warnings)
    Guess = dict.get(guess)
    if Guess in Guesses:
        Warnings -= 1


    elif Guess in Word:
        Updatedword = updateword(Guesses, Word)
        if Updatedword == True:
            return True
    

    else:
        



