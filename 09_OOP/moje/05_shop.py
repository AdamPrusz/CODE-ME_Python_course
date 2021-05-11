# 5▹ Utwórz klasę sklep. Sklep posiada różne produkty. W sklepie można pordukt zobaczyc, przymierzyc, kupic, zwrocic.
import random

class Shop:
    def __init__(self, products):
        self.products = products

    def show(self, index):
        try:
            print(self.products[index])
        except IndexError:
            print("The list is empty")

    def try_on(self, index):
        print(self.products[index], "was tried")

    def buy(self, item):
        if item in self.products:
            for index, value in enumerate(self.products):
                if value == item:
                    product_to_buy = self.products.pop(index)
                    return product_to_buy
        else:
            return "Nie ma takiego produktu"

    def give_back(self, item):
        self.products.append(item)
        print("produkt zwrócono!")


if __name__ == "__main__":

    clothes = Shop(["jeans", "t-shirt", "jacket", "pyjamas"])

    clothes.show(random.randint(0,3))

    clothes.try_on(random.randint(0,3))

    print(clothes.buy("jacket"))

    clothes.give_back("jacket")







