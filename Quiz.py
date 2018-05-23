from random import randint


def count_median(words):
    rates = []

    for w in words:
        rates.append(w.learn_rate)
    rates.sort()

    median = rates[int(len(rates)/2)]
    print(median)
    return median


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


def compose_quiz(words, amount):
    # counter for correct answers
    correct = 0

    # sort list of words by word rate
    words.sort(key=lambda x: x.learn_rate, reverse=True)

    # select random unique words below the median rate
    indexes = select_words(words, amount)

    for i in indexes:
        w = words[i]
        print(w.word + '\n')
        answer = input("answer: ")
        if answer == w.translation:
            correct += 1
            w.learn_rate += 1
    # TODO: show which words were correct
    print("Result: " + str(correct) + '/' + str(amount))
