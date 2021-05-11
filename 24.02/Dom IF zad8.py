# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

a = int(input("Podaj pierwszą dowolną liczbę: "))
print()

b = int(input("Podaj drugą dowolną liczbę: "))
print()

c = int(input("Podaj trzecią dowolną liczbę: "))
print()

if a > b and a > c:
    print ("największa liczba to ", a)
    print (a, max (b,c), min(b,c) )
elif b > a and b > c:
    print ("największa liczba to ", b)
    print (b, max(a,c), min(a,c) )
else:
    print("największa liczba to ", c)
    print(c, max(a, b), min(a, b))



