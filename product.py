class Product:
    def __init__(self, name, ptype, price):
        self.name = name
        self.ptype = ptype
        self.price = price

    def __repr__(self):
        return f"{self.ptype}\t{self.name}"

    def get_dict(self):
        # return {'name': self.name, "ptype": self.ptype, "price": self.price}
        return self.__dict__