class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, item, price):
        self.items.append({"item": item, "price": price})

    def calculate_total(self):
        return sum(item["price"] for item in self.items)

