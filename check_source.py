import os


def check_source():
    while True:
        path = input("Select file with words >> ")
        if os.path.exists(path):
            return path
        else:
            print("Wrong path, please try again.")
            continue
