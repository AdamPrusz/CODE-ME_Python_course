# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 10

user_num = int(input("Zgadnij ukryytą liczbę od 0 do 20: "))

if user_num < 0:
    print ("liczba nie może być mniejsza od 0!")
elif user_num > 20:
    print ("Liczba nie może być większa od 20!")

while user_num != secret_num:
    if user_num > secret_num:
        print("Twoja liczba jest za duża, spróbój jeszcze raz")
    elif user_num < secret_num:
        print("Twoja liczba jest za mała, spróbój jeszcze raz")

print("BRAWO, zgadłeś liczbę")



##  user_num == secret_num
   # print("BRAWO!")



#temp_F = 0
#while temp_F < 201:
 #   temp_C = (5.0 / 9.0) * (temp_F - 32)
  #  print("temperatura w F =", temp_F, "na C to:", round(temp_C, 2))
  #  temp_F = temp_F + 20