def is_palindrome(word):
    word = str(word)
    return word == word[::-1]

print(is_palindrome("kajak"))
print(is_palindrome("potop"))
print(is_palindrome("python"))
print(is_palindrome(12321))
print(is_palindrome(123))
