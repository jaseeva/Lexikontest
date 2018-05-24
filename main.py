# -*- coding:utf-8 -*-
import os
import time
import Quiz
import iocsv
from check_source import *
from load_dict import *


dataDirectory = r"D:\GitProjects\dicts"
activeWords = []


if __name__ == "__main__":
    # check if the dictionary exists and load words from it
    activeWords = load_dict(dataDirectory)
    if len(activeWords) == 0:
        newWords = check_source()
        activeWords = activeWords + iocsv.parse_new_words(newWords)
        activeWords = list(set(activeWords))
        print('New words added.' + '\n')
    else:
        print('Dictionary loaded.' + '\n')

    while True:
        print("Type 'add' to upload new words or 'quiz' for a quick test. Press 'qq' to quit.")
        navigation = input('>> ')

        if navigation == 'add':
            addedWords = check_source()
            activeWords = activeWords + iocsv.parse_new_words(addedWords)
            activeWords = list(set(activeWords))
            print('New words added.' + '\n')

        elif navigation == 'quiz':
            print('Select quiz type: regular or reverse:')
            choice = input('>> ')

            if choice == 'regular':
                Quiz.compose_quiz(activeWords, 3, 'w')
            elif choice == 'reverse':
                Quiz.compose_quiz(activeWords, 3, 't')
            else:
                continue

        elif navigation == 'qq':
            ts = str(time.time()).split('.')[0]
            filePath = '../dicts/' + 'dict' + ts + '.csv'
            iocsv.save_dict(activeWords, filePath)

            # remove old dict files so only 2 latest files stay
            filesList = os.listdir('../dicts/')
            if len(filesList) > 2:
                oldFiles = filesList[:-2]
                for i in oldFiles:
                    p = dataDirectory + '\\' + i
                    os.remove(p)
            quit()
        else:
            continue
