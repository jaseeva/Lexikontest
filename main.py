# -*- coding:utf-8 -*-
import Word
import os


def ask_source():
    while True:
        path = input("Select file with words >> ")
        if os.path.exists(path):
            return path
        else:
            print("Wrong path, please try again.")
            continue


if __name__ == "__main__":
    file = ask_source()
    mode = ''
    obj = []
    with open(file, encoding="utf-8") as f:
        for line in f:
            item = line.split(';')
            item = item[:-1]
            if len(item) <= 1:
                if item[0] == '##NOUNS':
                    mode = 'n'
                elif item[0] == '##VERBS':
                    mode = 'v'
                else:
                    continue
            else:
                if mode == 'n':
                    obj.append(Word.Noun(item[0], item[1], item[2], item[3]))
                elif mode == 'v':
                    obj.append(Word.Verb(item[0], item[1], item[2]))
                else:
                    continue
    for i in obj:
        print(i.word)

