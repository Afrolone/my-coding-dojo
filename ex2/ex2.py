def encode(plainText):
    lastLetter = plainText[0]
    occs = []
    occs.append({
        lastLetter: 0
    })
    finalString = ""

    for letter in plainText:
        if letter == lastLetter:
            occs[-1][lastLetter] += 1
        else:
            finalString = finalString + lastLetter + str(occs[-1][lastLetter])
            lastLetter = letter
            occs.append({
                lastLetter: 1
            })
    
    finalString = finalString + lastLetter + str(occs[-1][lastLetter])
    return finalString