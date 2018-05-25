import os
import iocsv


def load_dict(dataDirectory):
    activeWords = []

    # if dictionary file already exists
    if len(os.listdir(dataDirectory)) > 0:
        file = os.listdir(dataDirectory)[-1]

        if os.path.splitext(file)[1].lower() == '.csv':
            fullPath = dataDirectory + '\\' + file

            if os.path.exists(fullPath):
                activeWords, fileVal = iocsv.parse_dict(fullPath)

                # if the last saved dictionary file is not valid
                if not fileVal:
                    # check previous dict file
                    fullPathOlder = dataDirectory + '\\' + os.listdir(dataDirectory)[-2]
                    olderWords, olderFileVal = iocsv.parse_dict(fullPathOlder)
                    if olderFileVal:
                        activeWords = olderWords

                    # if both files not valid, pick the bigger(or newer) one
                    else:
                        newerSize = os.path.getsize(fullPath)
                        olderSize = os.path.getsize(fullPathOlder)
                        if newerSize < olderSize:
                            activeWords = olderWords
                        else:
                            return activeWords
    return activeWords
