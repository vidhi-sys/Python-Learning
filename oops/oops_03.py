import csv
from csv import DictReader

class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, x: str, y: float, z: int):
        self.x = x        # name
        self.y = y        # price
        self.z = z        # quantity
        Item.all.append(self)

    def calculate_price(self):
        print(f"Total price for object: {self.x}")
        return self.y * self.z

    @classmethod
    def from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = DictReader(f)
            for item in reader:
                cls(
                    x=item['name'],
                    y=float(item['price']),
                    z=int(item['quantity'])
                )

    def apply_discount(self):
        self.y = self.y * self.pay_rate

    def __repr__(self):
        return f"Item(name={self.x}, price={self.y}, quantity={self.z})"


#  Call the class method OUTSIDE the class
Item.from_csv()

# Optional: check loaded items
for item in Item.all:
    print(item)

