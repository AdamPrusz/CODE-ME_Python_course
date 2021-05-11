#Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np
#Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie.
#Następnie sprawdź czy wprowadzone wyrażenie jest palindromem

word = "kajak"
print("Is palidrom: ", word == word[::-1])


sentence = "Kobyła ma mały bok"
sentence = "Kobyła ma mały bok".replace(" ", "")
sentence = sentence.lower()
print(sentence)
print("Is palidrom: ", sentence == sentence[::-1])


sentence = input('Gimme me a sentence? ')
sentence = sentence.replace(" ", "")
sentence = sentence.lower()
print(sentence)
print("Is palidrom: ", sentence == sentence[::-1]
