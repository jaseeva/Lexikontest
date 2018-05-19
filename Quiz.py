from random import randint


def select_words(words, amount):
    selected = []
    while len(selected) < amount:
        i = randint(0, len(words) - 1)
        if i not in selected:
            selected.append(i)
        else:
            continue
    return selected


def compose_quiz(words, amount):
    # counter for correct answers
    correct = 0
    # select random unique words
    indexes = select_words(words, amount)
    for i in indexes:
        w = words[i]
        print(w.word + '\n')
        answer = input("answer: ")
        if answer == w.translation:
            correct += 1
    # TODO: show which words were correct
    print("Result: " + str(correct) + '/' + str(amount))
