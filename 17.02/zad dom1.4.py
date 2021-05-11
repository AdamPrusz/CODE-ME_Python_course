# Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora,
#liczbę stron, a następnie:

print()

title = input("Write book title: ")
author = input("Write book author : ")
page = input("Write number of pages: ")

print()

# A) Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
x=title.replace(" ", "")
print("Does book title have only letters?: ", x.isalpha())
print()

y=author.replace(" ", "")
print("Does author name have only letters?: ", y.isalpha())
print()


print("Does number of pages have only digits?: ",page.isdigit())
print()



# B) Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich

print("The title with capital letters: ", title.title())
print()
print("The author with capital letter: ", author.title())
print()



# C) Połącz dane w jeden ciąg book za pomocą spacji

a= title+author+page
book=a.replace(" ","")

print("the chain is: ", book)
print()


# D) Policz liczbę wszystkich znaków w napisie book

print("The number of signs in the above sentece is: ", len(book))

























