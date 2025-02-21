 # A class should be open for extension but closed for modification.
 
# Using inheritance to extend behaviour instead of modifying existing code
class Discount:
    def apply(self, price):
        return price
    
class PercantageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent
        
    def apply(self, price):
        return price - (price * self.percent / 100)
    
discount = PercantageDiscount(10)
print(discount.apply(100))

# Why? We extend functionality by adding new classes instead of modifying Discount.