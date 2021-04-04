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