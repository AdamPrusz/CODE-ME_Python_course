# Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

text = input ("wpisz dowolne znaki: ")
length = len(text)

for step in range (length):
    if (step+2) % 2 == 0:
        print(text[step], end="")
print()

print("----------------------------------------------------------")

print(text[::2])






