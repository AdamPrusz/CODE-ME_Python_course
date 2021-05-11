# 4▹ Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku. Napisz funkcję,
# która przyjmie wartości i wyświetli średnią. Program powinien być odporny na błędy użytkownika. Błędów nie wyświetlaj,
# ale rodzaj błędu zapisz do pliku.

def arithmetic_average(elements):
    user_list = elements.split(",")
    new_list = []
    for step in user_list:
        number = int(step)
        new_list.append(number)
    result = sum(new_list) / len(user_list)
    return result

def save_exceptions(filename, exception):
    with open(filename, 'a') as fp:
        fp.write(exception + '\n')

# ----- main code ------------------


try:
    user = input("Gimme numbers, use come as separator: ")
    print(f"The arithmetic average for user numbers = {arithmetic_average(user)}")
except ValueError as err:
    error = str(err)
    save_exceptions('exceptions.txt', error)




