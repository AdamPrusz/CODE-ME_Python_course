# 6▹ Utworz klasę Kraj, która zawiera informację o powierzchni. ludności, jaki język jest urzędowy, jakie
# miasto jest stolicą. Utwórz klika obiektów klasy Kraj, stwórz listę obiektów klasy kraj, wyświetl elementy
# na liście krajów.

class Country:
    def __init__(self, area, population, language, capital):
        self.area = area
        self.population = population
        self.language = language
        self.capital = capital


Poland = Country(60, 40, "polish", "Warsaw")
Germany = Country(80, 80, "german", "Berlin")
France = Country(85, 70, "french", "Paris")