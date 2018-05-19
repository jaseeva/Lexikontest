from random import randint


def compose_quiz(words):
    correct = 0
    for i in range(0, 3):
        # TODO: make sure that selected words are unique
        i = randint(0, len(words) - 1)
        w = words[i]
        print(w.word + '\n')
        answer = input("answer: ")
        if answer == w.translation:
            correct += 1
    # TODO: show which words were correct
    print("Result: " + str(correct) + '/3')
