from random import randint
import Word


def select_words(words, amount):
    selected = []

    while len(selected) < amount:
        # take lower half of words list with less learned words
        i = randint(int(len(words) / 2), len(words) - 1)
        if i not in selected:
            selected.append(i)
        else:
            continue
    return selected


def show_correct(words, wrongs):
    for key, value in wrongs.items():
        print(key + ' -- ' + value)

        correct = ''

        # find correct translation
        for w in words:
            if w.word == key:
                correct = w.translation
        print("Correct answer: " + correct + '\n')


def show_correct_reverse(words, wrongs):
    for key, value in wrongs.items():
        print(key + ' -- ' + value)

        correct = ''

        # find correct translation
        for w in words:
            if w.word == key:
                if type(w) is Word.Verb:
                    correct = w.word
                elif type(w) is Word.Noun:
                    correct = w.article + ' ' + w.word
        print("Correct answer: " + correct + '\n')


def quiz_run(words, indexes):
    correctPoints = 0
    wrongWords = {}

    for i in indexes:
        w = words[i]
        print(w.word + '\n')
        answer = input("answer: ")
        if answer == w.translation:
            correctPoints += 1
            w.learn_rate += 1
        else:
            wrongWords.update({w.word: answer})

    print("Result: " + str(correctPoints) + '/' + str(len(indexes)) + '\n')

    if len(wrongWords) > 0:
        show_correct(words, wrongWords)


def quiz_run_reverse(words, indexes):
    correctPoints = 0
    wrongWords = {}

    for i in indexes:
        w = words[i]
        print(w.translation + '\n')
        answer = input("answer: ")
        right = ''

        if type(w) is Word.Verb:
            right = w.word
        elif type(w) is Word.Noun:
            right = w.article + ' ' + w.word

        if answer == right:
            correctPoints += 1
            w.learn_rate += 1
        else:
            wrongWords.update({w.word: answer})

    print("Result: " + str(correctPoints) + '/' + str(len(indexes)) + '\n')

    if len(wrongWords) > 0:
        show_correct_reverse(words, wrongWords)


def compose_quiz(words, amount, mode):
    # sort list of words by word rate
    words.sort(key=lambda x: x.learn_rate, reverse=True)

    # select random unique words below the median rate
    indexes = select_words(words, amount)

    if mode == 'w':
        quiz_run(words, indexes)
    elif mode == 't':
        quiz_run_reverse(words, indexes)
