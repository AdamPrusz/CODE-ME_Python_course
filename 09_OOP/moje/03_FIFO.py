# 3▹ Stwórz własną implementację kolejki FIFO. Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
# Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki, sprawdzenie czy jest pusta, dodanie elementu do
# kolejki (put), wyjęcie elementu z kolejki (get).
#
# Utwórz kilka obiektów klasy Queue z różnymi parametrami.


class Queue:

    def __init__(self, products):
        self.products = products

    def show(self):
        print(self.products)

    def is_empty(self):
        if len(self.products) == 0:
            return True
        else:
            return False

    def put(self, item):
        self.products.append(item)
        print("dodano produkt!")

    def get(self):
        try:
            return self.products.pop(0)
        except IndexError:
            return "nie ma więcej elementów"

if __name__ == "__main__":
    products1 = Queue([1,2,3,4])
    products1.show()
    print(products1.is_empty())
    products1.put("8")
    products1.show()
    print(products1.get())


