
class Checkout:

    class Discount:
        def __init__(self, number_of_items, discounted_price):
            self.number_of_items = number_of_items
            self.discounted_price = discounted_price

    def __init__(self) -> None:
        self.prices = {}
        self.discounts = {}
        self.total = 0
        self.items = {}
    
    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        self.total += self.prices[item]
        self.items.setdefault(item, 0)
        self.items[item] += 1

    def calculateTotal(self):
        total = 0
        for item, number_of_items in self.items.items():
            total += self.calculateItemTotal(item, number_of_items)
        return total

    def calculateItemTotal(self, item, number_of_items):
        if item in self.discounts:
            return self.calculateItemDiscountedTotal(item, number_of_items)
        return number_of_items*self.prices[item]

    def calculateItemDiscountedTotal(self, item, number_of_items):
        discount = self.discounts[item]
        number_of_discounts = number_of_items // discount.number_of_items
        total = number_of_discounts * discount.discounted_price
        number_of_ramaining_items = number_of_items % discount.number_of_items
        total += number_of_ramaining_items * self.prices[item]
        return total

    def addDiscount(self, item, number_of_items, discounted_price):
        self.discounts[item] = self.Discount(number_of_items, discounted_price)
