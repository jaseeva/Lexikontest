import Word


def save_dict(words, path):
    with open(path, 'w') as f:
        allnouns = []
        allverbs = []
        # create formatted string for each word
        for i in words:
            content = ''
            if type(i) is Word.Noun:
                content += i.word + ';'
                content += i.translation + ';'
                content += i.article + ';'
                content += i.plural + ';'
                allnouns.append(content)
            elif type(i) is Word.Verb:
                content += i.word + ';'
                content += i.translation + ';'
                content += i.perfect + ';'
                allverbs.append(content)
        # add dividers and write words
        content = ''
        content += '##NOUNS;' + '\n'
        for i in allnouns:
            content += i + '\n'

        content += '##VERBS;' + '\n'
        for i in allverbs:
            content += i + '\n'

        f.write(content + '\n')
