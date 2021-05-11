# 2▹ Utwórz dowolną krotkę zawierającą kilka wartości np. 10. Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd



items = (13, "string", 2.45, 0, "e", True, False, [], {'key': 3}, (), {})

try:
    index = int(input("Gimme number of index 0-9: "))
    value = input("Gimme whatever: ")

    try:
        items[index] = value
        print(items[index])
    except TypeError:
        print("The tuple is not mutable")
    finally:
        new_items = list(items)
        new_items[index] = value
        print("If it had been a list, the result would have been as below: ")
        print(new_items[index])

except (IndexError, ValueError) as err:
    print('Incorrect index ->', err)


