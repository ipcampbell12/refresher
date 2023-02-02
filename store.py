class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.

    def add_item(self, name, price):
        item = {"name": name, "price": price}
        self.items.append(item)
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        total = 0
        for item in self.items:
            total += item["price"]

        return total


myStore = Store("My Cool Store")

myStore.add_item("Pumpa", 3.95)
myStore.add_item("Thumpa", 5.35)
myStore.add_item("Dmpa", 12.22)

# print(myStore.name)
# print(myStore.items)
print(myStore.stock_price())
