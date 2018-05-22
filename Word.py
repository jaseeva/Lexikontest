class Word(object):
    def __init__(self, word, translation):
        self.word = word
        self.translation = translation

    def __eq__(self, other):
        return self.word == other.word and self.translation == other.translation

    def __hash__(self):
        return hash(('word', self.word, 'translation', self.translation))


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
