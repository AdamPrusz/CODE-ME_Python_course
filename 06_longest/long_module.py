# Utwórz generator instancji testowych, który wygeneruje losowe ciągi znaków składające się z jedynie
# z cyfr od 0-9. Upewnij się, że co najmniej 2 takie same znaki znajdą się w sekwencji.

# Zmodyfikuj generator tak, by oczekiwał znaków podanych przez użytkownika np. użytkownik
# podaje 4 znaki: ‘a’, ‘b’, ‘c’, ‘*’.

import random


def user_choice():
    elements = []
    for step in range(4):
        user = input("gimme 4 elements: ")
        elements.append(user)
    return elements

def computer_choice(element):
    numbers = []
    for step in range(0,20):
        generator = random.choice(element)
        numbers.append(generator)
    return numbers


def finding_longest_seq(number):
    counts = 1
    max_counts = 0
    last_seen = number[0]
    for i in number [1:]:
        if i == last_seen:
            counts += 1
            most_freq = i
        else:
            if counts > max_counts:
                max_counts = counts
                most_freq = last_seen

            last_seen = i
            counts = 1


    print (number)

    if counts > max_counts:
        max_counts = counts
    if max_counts == 1:
        return("None of elements creates a sequence for more than 1")
    else:
        return(f"The longest sequnce is {str(most_freq) * max_counts} ---> length: {max_counts}")

















