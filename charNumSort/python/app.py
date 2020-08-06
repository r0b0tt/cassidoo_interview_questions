myList = ["Bananas", "do", "not", "grow", "in", "Mississippi"]


def distinctCharacters(myStr):
    """Returns the number of distinct characters in a string
    """
    characters = []
    for character in myStr:
        if character not in characters:
            characters.append(character)

    return len(characters)


def strLength(myStr):
    """Returns the length of the string
    """
    return len(myStr)


def charNumSort(myList):
    """Prints an array that has been sorted based on the number
    of distinct characters that occur in the word
    """
    sortedList = sorted(sorted(myList, key=distinctCharacters), key=strLength)
    print(sortedList)


charNumSort(myList)
