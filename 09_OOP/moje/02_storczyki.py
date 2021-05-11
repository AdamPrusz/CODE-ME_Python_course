# 2▹ Utwórz klasę dla storczyków. Storczyki z zasady mają różne kolory, pory kwitnienia, gatunki.
# Utwórz dowolne atrybuty i metody. Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin.
#
# Utwórz kilka storczyków z różnymi parametrami.


class Orchids:

    kingdom = "plants"

    def __init__(self, colour, season_of_bloom, species):
        self.colour = colour
        self.season_of_bloom = season_of_bloom
        self.species = species

    def growth(self):
        content = f"{self.species} grows in {self.season_of_bloom}"
        return content


flower1 = Orchids("yellow", "april", "cattleya")
flower2 = Orchids("rose", "may", "cymbidium")
flower3 = Orchids("green", "march", "phalaenopis")


print(f"{flower1.species} has kingdom {flower1.kingdom}, colour {flower1.colour} and grows in {flower1.season_of_bloom}")
print(f"{flower3.species} has also kingdom {flower3.kingdom}")
print(flower2.growth())




