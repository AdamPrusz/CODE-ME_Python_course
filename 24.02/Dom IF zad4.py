#Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków
#oraz czy zawiera literę a. Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

your_characters = str(input("wpisz dowolny ciąg znaków, większy od 5: "))

your_characters_small_letters = your_characters.lower()

if len(your_characters_small_letters) < 5:
    print("ciąg znaków ma być większy od 5! ")
elif "a" in your_characters_small_letters:
    print(your_characters_small_letters.replace("a" , "z"))
else:
    print("nie ma żadnej litery 'a' w twoim ciągu znaków")