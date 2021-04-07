def isUnique(someStr):
    presentChars = []
    unique = True
    for char in someStr:
        if char not in presentChars:
            presentChars.append(char)
        else:
            unique = False
            break
    return unique

somesss = "abcdefhijkl"
somesss1 = "aaaeewwewe"

print(isUnique(somesss))
print(isUnique(somesss1))