class Word(object):
    def __init__(self, word, translation, learn_rate):
        self.word = word
        self.translation = translation
        self.learn_rate = learn_rate

    def __eq__(self, other):
        return self.word == other.word and self.translation == other.translation

    def __hash__(self):
        return hash(('word', self.word, 'translation', self.translation))


class Noun(Word):
    def __init__(self, word, translation, article, plural, learn_rate):
        Word.__init__(self, word, translation, learn_rate)
        self.article = article
        self.plural = plural


class Verb(Word):
    def __init__(self, word, translation, perfect, learn_rate):
        Word.__init__(self, word, translation, learn_rate)
        # self.forms = forms
        self.perfect = perfect
