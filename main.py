import pickle
from io import open
from typing import Dict
from product import Product
import json


class Store:
    nacenka: int
    store: Dict

    def __init__(self, name, nacenka):
        self.name = name
        self.nacenka = nacenka
        self.store = {}
        self.moneys = 0
        self.__filename = f"{self.name}.json"

    def add_product(self, prod: Product, count):
        self.store.update({prod: {"count": count, 'sell_price': self.__calcprice(prod.price)}})

    def display(self):
        print(f"Магазин {self.name} В кассе {self.moneys} денег.")
        for prod, value in self.store.items():
            prod: Product
            value: Dict
            print(prod, value)

    def __calcprice(self, prod_price):
        return round(prod_price * (1 + self.nacenka / 100), 3)

    def __get_product(self, name):
        for prod in self.store:
            if prod.name == name:
                return prod
        return None

    def sell(self, prod_name, p_count):
        prod = self.__get_product(prod_name)
        if prod and self.store[prod]["count"] >= p_count > 0:
            self.store[prod]["count"] -= p_count
            self.moneys += self.store[prod]["sell_price"] * p_count

    def save_pickle(self):
        with open(self.__filename, 'wb') as fo:
            pickle.dump(self, fo)
        print("Store info successfully saved")

    def load_pickle(self):
        with open(self.__filename, "rb") as fi:
            aself = pickle.load(fi)
            print("ALERT", aself.moneys)
        print("Store info successfully loaded")
        return aself

    def save_json(self):
        with open(self.__filename, 'w') as fo:
            data = {'moneys': self.moneys, 'store': []}
            slist = []
            for prod in self.store:
                adict = prod.get_dict()
                adict.update(self.store.get(prod))
                slist.append(adict)
            data["store"] = slist
            print(data)
            json.dump(data, fo)

    def load_json(self):
        with open(self.__filename) as fi:
            data = json.load(fi)
            print(data)
            self.moneys = data.pop("moneys")
            self.store = {}
            for prods in data["store"]:
                p = Product(prods.get('name'), prods.get('ptype'), prods.get('price'))
                self.store[p] = {'count': prods.get('count'), 'sell_price': prods.get('sell_price')}
            print("Store info successfully loaded")


if __name__ == '__main__':
    a1 = Product("Хлеб", "Мучное", 10)
    a2 = Product("Булка", "Мучное", 12)
    a3 = Product("Батон", "Мучное", 14)

    s1 = Store("SuperStore", 15)
    s2 = Store("ASHOT", 85)

    s1.add_product(a1, 10)
    s1.add_product(a2, 10)
    s1.add_product(a3, 10)

    s2.add_product(a1, 5)
    s2.add_product(a2, 6)
    s2.add_product(a3, 4)

    # s1.display()
    # s2.display()

    s1.sell("Хлеб", 5)
    s2.sell("Хлеб", 2)
    s1.sell("Булка", 4)
    s2.sell("Булка", -10)
    # a1.name = 'Paneton'
    # a1.price = 305

    s1.display()
    # s2.display()
    s1.save_json()
    s1.store = {}
    s1.moneys = 0
    s1.display()
    s1.load_json()
    #
    # s1 = s1.load()
    s1.display()
