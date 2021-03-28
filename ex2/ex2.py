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

teststr1 = "aaaabbbcccddeeeaaaxxx"
teststr2 = "ccccxxeeeeeeyyttmmmhhloppddty"
teststr3 = "ppppprrssrtttuvbbbkkkoollllytt"

print(encode(teststr1)) # a4b3c3d2e3a3x3
print(encode(teststr2)) # c4x2e6y2t2m3h2l1o1p2d2t1y1
print(encode(teststr3)) # p5r2s2r1t3u1v1b3k3o2l4y1t2