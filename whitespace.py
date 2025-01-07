from mapping import mapping


def insertNewLines(whitespace):
    newMap = {}
    for title in whitespace:
        newMap[title] = whitespace[title].replace(" ", "\n")
    return newMap


print(insertNewLines(mapping))
