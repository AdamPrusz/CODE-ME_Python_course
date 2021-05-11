# 4▹ Pomyśl co sprawia, że ssak jest ssakiem? Utwórz klasę ssaki.
# Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki.

class Mammals:
    def __init__(self,hairs, legs):
        self.hairs = hairs
        self.legs = legs

    def milk(self):
        content = "can produce own milk"
        return content



wolf = Mammals("grey", 4)
horse = Mammals("brown", 4)

print(f"wolf has got {wolf.hairs} colour and {wolf.milk()}")
print("horse has", horse.legs, "legs")

