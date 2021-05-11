# 1▹ Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.
#
# atrybuty: imię, kolor sierści, rasę
#
# metody: szczekaj, machaj ogonem
#
# Utwórz kilka obiektów klasy Pies z różnymi parametrami.

class Dog:
    def __init__(self, name, colour, brand):

        self.name = name
        self.colour = colour
        self.brand = brand

    def bark(self):
        print("my name is:", self.name, "HAU HAU HAU")

    def wiggle(self):
        print("my name is:", self.name, "wiggle wiggle wiggle")

dog_1 = Dog("Saba", "beige", "labrador")
dog_2 = Dog("Sonia", "brown", "srub")

dog_1.bark()
dog_2.wiggle()
