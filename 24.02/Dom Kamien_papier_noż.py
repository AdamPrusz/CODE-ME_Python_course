# Napisz grę - kamień (k) / papier (p) / nożyce (n).

# 1) Użytkownik podaje jedną z 3 figur.
# 2) Komputer losuje jedną z 3 figur.
# 3) Sprawdź kto wygrał tę rundę.
# 4) Zmień kod tak, by użytkownik mógł podac liczbę rund.
# 5) Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# 6) Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

rounds_number = int(input("Write number of rounds: "))

game = ['kamień', 'papier', 'nożyce']

import random

user_wins =0

computer_wins = 0


for step in range (1, rounds_number+1):
    user = input("choose kamień, papier or nożyce: ")
    computer = random.choice(game)
    print("computer: ", computer)
    print()
    if user == computer:
        print ("It's a draw! Try again")
        print()
    elif computer == "kamień" and user == "papier":
        print ("User won this round")
        user_wins = user_wins + 1
        print()
    elif computer == "papier" and user == "nożyce":
        print ("User won this round")
        user_wins = user_wins + 1
        print()
    elif computer == "nożyce" and user == "kamień":
        print ("User won this round")
        user_wins = user_wins + 1
        print()
    elif user == "koniec":
        break
    else:
        print ("Computer won this round")
        computer_wins = computer_wins + 1
        print()

print("Computer TOTAL wins: ", computer_wins)

print("User TOTAL wins: ", user_wins)

if computer_wins > user_wins:
    print("Computer won the GAME")
elif computer_wins < user_wins:
    print("User won the GAME")
else:
    print("DRAW")

