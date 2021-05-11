#Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
#(N podane przez użytkownika, ale nie większe niż 8).



number = int(input("podaj liczbę całkowitą od 1 do 8: "))

factorial = 1

if number > 8:
    print("liczba nie może byc większa od 8")
elif number < 1:
    print("liczba nie może byc mniejsza od 1")
else:
    for step in range(1, number + 1):
        factorial = factorial * step
        print ("kolejne wyniki silni z" , number, "wynoszą: ", factorial)






