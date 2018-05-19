class Word(object):
    def __init__(self, word, translation):
        self.word = word
        self.translation = translation


class Noun(Word):
    def __init__(self, word, translation, article, plural):
        Word.__init__(self, word, translation)
        self.article = article
        self.plural = plural


class Verb(Word):
    def __init__(self, word, translation, perfect):
        Word.__init__(self, word, translation)
        # self.forms = forms
        self.perfect = perfect
