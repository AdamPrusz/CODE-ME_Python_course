# 5▹ Utwórz klasę sklep. Sklep posiada różne produkty. W sklepie można pordukt zobaczyc, przymierzyc, kupic, zwrocic.

class Shop:
    def __init__(self, products):
        self.products = products

    def show_products(self):
        print(self.products)

    def buy(self, element):
        print(f"Kupiono {self.products[element]}")
        self.products.pop(element)

    def give_back(self, element):
        self.products.append(element)
        print(f"Oddano {element}")




if __name__ == "__main__":
    products_list = ['cucumber', 'potato', 'milk', 'pasta', 'beer', 'bread']
    products = Shop(products_list)

    products.show_products()
    products.buy(1)
    products.show_products()

    products.give_back("potato")
    products.show_products()