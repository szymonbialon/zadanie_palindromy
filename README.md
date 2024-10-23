# Palindrome Checker

Projekt zawiera funkcję w Pythonie, która służy do sprawdzania, czy podane słowo lub liczba jest palindromem. 
Palindrom to słowo lub liczba, które czytane zarówno od lewej do prawej, jak i od prawej do lewej, brzmią tak samo.

## Jak działa funkcja

Funkcja `is_palindrome` przyjmuje jeden argument, który może być zarówno łańcuchem znaków, jak i liczbą. 
Funkcja konwertuje argument na string i porównuje go z jego odwróconą wersją. 
Jeśli oba te napisy są identyczne, funkcja zwraca `True`, wskazując, że argument jest palindromem. 
W przeciwnym razie zwraca `False`.

## Wymagania

- Python 3.6 lub nowszy

## Jak używać

1. Sklonuj repozytorium lub pobierz pliki na swój komputer.
2. Uruchom plik `main.py`, aby przetestować przykładowe słowa i liczby.

## Przykłady

Przykłady użycia funkcji:

```python
print(is_palindrome("kajak"))   # True - słowo jest palindromem
print(is_palindrome("potop"))   # True - słowo jest palindromem
print(is_palindrome("python"))  # False - słowo nie jest palindromem
print(is_palindrome(12321))     # True - liczba jest palindromem
print(is_palindrome(123))       # False - liczba nie jest palindromem
