#Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl
#komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

a = 20 #jak wylosowac liczbe?

number = int(input("wybierz dowolną liczbę całkowitą od 1 do 100: "))

if number == a:
    print("gratulację!")
else:
    print("pudło!")