#Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
#Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

number_1 = int(input("Podaj liczbę dowolną liczbę całkowitą: "))
print()
number_2 = int(input("Podaj drugą dowolną liczbę całkowitą: "))
print()

if number_1+number_2 > 100:
    print(number_1+number_2)
else:
    print("Koniec")
