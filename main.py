# -*- coding:utf-8 -*-
import os
import Word
import Quiz
import iocsv


activeWords = []


def ask_source():
    while True:
        path = input("Select file with words >> ")
        if os.path.exists(path):
            return path
        else:
            print("Wrong path, please try again.")
            continue


def load_dict(file):
    # if dictionary file already exists
    if os.path.exists(file):
        global activeWords
        activeWords = iocsv.parse_words(file)
    return activeWords


if __name__ == "__main__":
    # check if the dictionary exists and load words from it
    activeWords = load_dict('../dict.csv')
    if len(activeWords) == 0:
        newWords = ask_source()
        activeWords = activeWords + iocsv.parse_words(newWords)

    while True:
        print("Type 'add' to upload new words or 'quiz' for a quick test. Press 'qq' to quit.")
        navigation = input('>> ')
        if navigation == 'add':
            addedWords = ask_source()
            # TODO: make sure that words are not added if they already exist in dictionary
            activeWords = activeWords + iocsv.parse_words(addedWords)
        elif navigation == 'quiz':
            Quiz.compose_quiz(activeWords, 3)
        elif navigation == 'qq':
            filePath = '../dict.csv'
            # TODO: make sure that user data is not lost if new file was saved incorrectly
            iocsv.save_dict(activeWords, filePath)
            quit()
        else:
            continue
