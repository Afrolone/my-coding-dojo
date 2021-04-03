def reversePalindrome(text):

    def isPalindrome(word):
        return word == word[::-1]
    
    words = text.split(" ")
    palindromes = []
    palindromeIndices = []

    for word in words:
        if isPalindrome(word):
            palindromes.append(word)
            palindromeIndices.append(words.index(word))
    
    count = -1
    for index in palindromeIndices:
        words[index] = palindromes[count]
        count = count -1
    
    return " ".join(words)

S1 = "mom and dad went to eye hospital"
# eye and dad went to mom hospital
S2 = "wow it is next level"
# level it is next wow.

print(S1)
print(reversePalindrome(S1))
print(S2)
print(reversePalindrome(S2))