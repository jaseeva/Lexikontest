import Word


def save_dict(words, path):
    check = len(words)

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
                content += str(i.learn_rate) + ';'
                allnouns.append(content)

            elif type(i) is Word.Verb:
                content += i.word + ';'
                content += i.translation + ';'
                content += i.perfect + ';'
                content += str(i.learn_rate) + ';'
                allverbs.append(content)

        # add dividers and write words
        content = ''
        content += '##NOUNS;' + '\n'
        for i in allnouns:
            content += i + '\n'

        content += '##VERBS;' + '\n'
        for i in allverbs:
            content += i + '\n'

        checksum = '##END;' + str(check)

        try:
            f.write(content + '\n' + checksum)
        except IOError as e:
            print("Writing to file failed (%s)." % e)


def parse_dict(path):
    words = []
    mode = ''
    valid = False

    with open(path, encoding="utf-8") as f:
        for line in f:
            item = line.split(';')
            if len(item) <= 2:
                if item[0] == '##NOUNS':
                    mode = 'n'
                elif item[0] == '##VERBS':
                    mode = 'v'
                elif item[0] == '##END':
                    if int(item[1]) == len(words):
                        valid = True
                        break
                else:
                    continue
            else:
                if mode == 'n':
                    words.append(Word.Noun(item[0], item[1], item[2], item[3], int(item[4])))
                elif mode == 'v':
                    words.append(Word.Verb(item[0], item[1], item[2], int(item[3])))
                else:
                    continue
    return words, valid


def parse_new_words(path):
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
                    words.append(Word.Noun(item[0], item[1], item[2], item[3], 0))
                elif mode == 'v':
                    words.append(Word.Verb(item[0], item[1], item[2], 0))
                else:
                    continue
    return words
