# Wyświetl 3 losowe cytaty
import os
from random import choice

def select_three_random(quotes):
    three_quotes = []
    count = 0
    while count < 3:
        quote = choice(quotes)
        if quote in three_quotes:
            continue
        else:
            three_quotes.append(quote)
            count += 1

    return three_quotes

def print_three(quotes):
    for step in quotes:
        print(step)

filename = "quotes.txt"
with open(filename, 'r') as fopen:
    lines = fopen.readlines()

quote = select_three_random(lines)
print_three(quote)

path = os.getcwd()

size = os.path.getsize(path)

print("Size (In bytes) of '%s':" %path, size)






