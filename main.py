def is_palindrome(word):
    """Sprawdza, czy podane słowo (lub liczba) jest palindromem.

      Args:
          word (str or int): Słowo lub liczba do sprawdzenia.

      Returns:
          bool: True, jeśli słowo jest palindromem, inaczej False.
      """
    word = str(word)
    return word == word[::-1]

print(is_palindrome("kajak"))
print(is_palindrome("potop"))
print(is_palindrome("python"))
print(is_palindrome(12321))
print(is_palindrome(123))