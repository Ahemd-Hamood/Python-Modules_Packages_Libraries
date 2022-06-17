class Sales:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        print(f"Item name: {self.name}, the price is {self.price}")
