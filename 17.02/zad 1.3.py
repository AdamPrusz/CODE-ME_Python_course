qoute = "Honesty is the first chapter in the book of wisdom."

print(len(qoute)) #ilosc znakow

print(qoute[-7:-1]) #wisdom

mid = len(qoute)//2
print(qoute[:mid]) #pierwsza połowa

print(qoute[-1:]) #sama kropka

print(qoute[mid::3]) #od polowy co 3

print(qoute[::2]) #co dwa

print(qoute[::-1]) #odwrotnie

print(qoute.replace("wisdom", "freedom")) #zamiana slowa wisdom na freedom
