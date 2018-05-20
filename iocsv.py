import Word


def save_dict(words, path):
    with open(path, 'w', encoding='utf-8') as f:
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


def parse_words(path):
    words = []
    mode = ''
    with open(path, encoding="utf-8") as f:
        for line in f:
            item = line.split(';')
            if len(item) <= 2:
                if item[0] == '##NOUNS':
                    mode = 'n'
                elif item[0] == '##VERBS':
                    mode = 'v'
                else:
                    continue
            else:
                if mode == 'n':
                    words.append(Word.Noun(item[0], item[1], item[2], item[3]))
                elif mode == 'v':
                    words.append(Word.Verb(item[0], item[1], item[2]))
                else:
                    continue
    return words
