# Encode plaintext
Implement the function `encode(plainText)` which returns an encoded message.
It receives a `plainText` string parameter, for example aaaabcccaaa.
You must encode it by counting consecutive sequence of a letter e.g. in aaaabcccaaa, there are:

* 4 times the letter a
* then 1b
* then 3c
* then 3a

Therefore you must return the string 4a1b3c3a.

Constraints:

* `plainText` is made of lowercase letters: a-z

* `plainText` is never null and has a maximum length of 15000 characters.