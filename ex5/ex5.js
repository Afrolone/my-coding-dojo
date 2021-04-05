function reversePalindrome(text) {

    function isPalindrome(word) {
        var re = /[^A-Za-z0-9]/g;
        word = word.toLowerCase().replace(re, '');
        var len = word.length;
        for (var i = 0; i < len / 2; i++) {
            if (word[i] !== word[len - 1 - i]) {
                return false;
            }
        }
        return true;
    }

    words = text.split(" ");

    palindromes = [];
    palindromeIndices = [];

    num_of_words = words.length;

    for(i=0; i<num_of_words; i++) {
        if (isPalindrome(words[i])) {
            palindromes.push(words[i]);
            palindromeIndices.push(i);
        }
    }

    palindromeIndices.forEach(i => {
        words[i] = palindromes.pop()
    });

    return words.join(" ");
}

S1 = "mom and dad went to eye hospital";
S2 = "wow it is next level";

console.log(reversePalindrome(S1));
console.log(reversePalindrome(S2));
