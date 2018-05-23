# -*- coding:utf-8 -*-
import os
import time
import Quiz
import iocsv


dataDirectory = r"D:\GitProjects\dicts"
activeWords = []


def ask_source():
    while True:
        path = input("Select file with words >> ")
        if os.path.exists(path):
            return path
        else:
            print("Wrong path, please try again.")
            continue


def load_dict():
    # if dictionary file already exists
    if len(os.listdir(dataDirectory)) > 0:
        file = os.listdir(dataDirectory)[-1]

        if os.path.splitext(file)[1].lower() == '.csv':
            fullPath = dataDirectory + '\\' + file

            if os.path.exists(fullPath):
                global activeWords
                activeWords, fileVal = iocsv.parse_dict(fullPath)

                # if the last saved dictionary file is not valid
                if not fileVal:
                    # check previous dict file
                    fullPathOlder = dataDirectory + '\\' + os.listdir(dataDirectory)[-2]
                    olderWords, olderFileVal = iocsv.parse_dict(fullPathOlder)
                    if olderFileVal:
                        activeWords = olderWords

                    # if both files not valid, pick the bigger(or newer) one
                    else:
                        newerSize = os.path.getsize(fullPath)
                        olderSize = os.path.getsize(fullPathOlder)
                        if newerSize < olderSize:
                            activeWords = olderWords
                        else:
                            return activeWords
    return activeWords


if __name__ == "__main__":
    # check if the dictionary exists and load words from it
    activeWords = load_dict()
    if len(activeWords) == 0:
        newWords = ask_source()
        activeWords = activeWords + iocsv.parse_new_words(newWords)
        activeWords = list(set(activeWords))
        print('New words added.' + '\n')
    else:
        print('Dictionary loaded.' + '\n')

    while True:
        print("Type 'add' to upload new words or 'quiz' for a quick test. Press 'qq' to quit.")
        navigation = input('>> ')

        if navigation == 'add':
            addedWords = ask_source()
            activeWords = activeWords + iocsv.parse_new_words(addedWords)
            activeWords = list(set(activeWords))
            print('New words added.' + '\n')

        elif navigation == 'quiz':
            Quiz.compose_quiz(activeWords, 3)

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
