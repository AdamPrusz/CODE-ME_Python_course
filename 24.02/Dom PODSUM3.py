# W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

signs = input ("write what you wanna: ")

digits= 0
big=0
small=0
special=0


for step in signs:
    if step.isdigit():
        digits = digits + 1
    elif step.isupper():
        big = big + 1
    elif step.islower():
        small = small + 1
    elif not step.isalnum():
        special = special + 1
print("the sum of digits is: ", digits)
print("the sum of capital letters is: ", big)
print("the sum of small letters is: ", small)
print("the sum of special signs is: ", special)