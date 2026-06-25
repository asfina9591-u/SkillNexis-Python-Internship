class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Bill:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def calculate_total(self):
        total = sum(p.price * p.quantity for p in self.items)
        tax = total * 0.1  # 10% tax
        return total + tax

    def display_bill(self):
        print("----- Final Bill -----")
        for p in self.items:
            print(f"{p.name} | {p.price} | {p.quantity} | {p.price * p.quantity}")
        print("Total (with tax):", self.calculate_total())

# Example usage
bill = Bill()
bill.add_item(Product("Pen", 10, 2))
bill.add_item(Product("Notebook", 50, 1))
bill.display_bill()
