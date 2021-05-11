# Program loteria. Użytkownik, podobnie jak w klasycznym totolotku, podaje ciąg 6 swoich liczb w zakresie
# od 1 do 50. Komputer losuje 6 liczb totolotka.


def computer_choice():
    #computer's choosing random numers from 1 to 50
    import random
    computer_numbers = []
    while len(computer_numbers) < 6:
        number = random.randint(1,50)
        if number in computer_numbers:
            continue
        computer_numbers.append(number)
    return computer_numbers


def user_choice():
    #user's selecting numbers in the lottery from 1 to 50, 6 times
    user_numbers =[]
    while len(user_numbers) < 6:
        user = int(input("Give me number from 1 to 50: "))
        if user in user_numbers:
            continue
        user_numbers.append(user)
    return user_numbers


def check_numbers(user,computer):
    #check if user numbers are the same as computer ones
    count =0
    for number in user():
        if number in computer():
            count =+ 1
    return count


def how_much_user_won(check):
    #check how much user won
    if check == 6:
        print ("WOW! You won 1 milion PLN!")
    elif check == 5:
        print ("WOW! You won 3500 PLN")
    elif check == 4:
        print ("Congrats! You won 100 PLN")
    elif check == 3:
        print ("Congrats! You won 10 PLN ")
    else:
        print ("Unfortunately you won 0 PLN :(")


#------ main code -----------------------

print("-----LOTERY-----")
how_much_user_won(check_numbers(user_choice,computer_choice))































