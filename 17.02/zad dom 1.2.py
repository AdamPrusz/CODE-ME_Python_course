# Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch
# s3, dołączając s2 w środku s1

s1 = input("write any word: ")
s2 = input("write any word: ")
len(s1)
mid_s1= len(s1)//2
s3= s1[:mid_s1] + s2 + s1[mid_s1:]
print(s3)
