# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:56:53 2021

@author: justo
"""

import random

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

#Check if guess correct

def guesscheck(word, guess):
    """
    Checks if the guess is correct or not
    If it is correct then it returns true
    else it returns false
    """
    if guess in word:
        return True
    return False


def updateword(guesses, word):
    """
    Goes over the guesses and if its in the word then it updates the new string
    returns: the new unguessed string
    
    Parameters:
        guesses: a list that contains the guessed letters
        word: a string that is the word the user is trying to guess
        
    """
    Updatedword = ""
    for i in word:
        if i in guesses:
            Updatedword += i
        else:
            Updatedword += "_ "
            
    if word == Updatedword:
        return True
    return Updatedword

def Printing(guesses, points, warnings, word):
    print("You have {} points left and {} warnings left".format(points, warnings))
    guessesstring = ""
    for i in guesses:
        guessesstring += str(i)
        guessesstring += "-"
        
    print("Guesses: {}".format(guessesstring))
    print("The word: {}".format(word))
    
def game(word):
        print("Hello user, welcome to hangman. Please input your guess in the next message to start the game")
        lengthofword = len(word)
        guesses = []
        points = 8
        warnings = 3
        print("The rules are the following, if you guessed a contant and its not correct you lose a point, however if you guessed a vowel and its not correct you lose 2 points. You have 8 points. You also have 3 warnings in case you guessed the same letter twice or guessed a number")
        print("The word is {} letters".format(lengthofword))
        print("And the game starts now")
        guessword = updateword(guesses, word)
        while True:
            if points <= 0 or warnings <= 0:
                print("Sorry you lost the game")
                break
                return None
            if guessword == True:
                points = lengthofword * points
                print("You won, you scored {} points".format(points))
                break
                return None
            Printing(guesses, points, warnings, guessword)
            guess = input("Pleae input your guess: ")
            if guess in guesses or len(guess) != 1:
                warnings -= 1

            else:
                guesses.append(guess)
                if guesscheck(word, guess):
                    guessword = updateword(guesses, word)
                    print("Congrats, your guess is correct")
                else:
                    print("Sorry your guess is not correct")
                    if guess in "aeiou":
                        points -= 2
                    else:
                        points -= 1
                        
wordlist = load_words()
word=choose_word(wordlist)
print(word)
game(word)
                        
                    
      
