# Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności od
# wyniku: niedowaga / waga normalna / nadwaga / otyłość

# BMI = (masa (kg)) / (wzrost (m))²

waga = int( input('Podaj swoją wagę [kg]: '))
wzrost_cm = int(input('Podaj swój wzrost [cm]: '))
wzrost_m = wzrost_cm / 100
BMI = waga / (wzrost_m ** 2)
BMI_rounded = round(BMI, 2)

if BMI_rounded >= 30:
    print ("otyłość")
elif BMI_rounded >= 25 and BMI_rounded <= 29.9:
    print ("nadwaga")
elif BMI_rounded < 18.5:
    print ("niedowaga")
else:
    print ("waga normalna")