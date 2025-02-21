# A class should not be forced to implement methods it doesn't use.
# ✅ Example: Use separate interfaces instead of one large interface.

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self):
        pass
    
class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass
    
class AllInOnePrinter(Printer, Scanner):
    def print(self):
        return "printing..."
    
    def scan(self):
        return "scanning..."    

class SimplePrinter(Printer):
    def print(self):
        return "printing only..."
    

printer = SimplePrinter()
print(printer.print())

print(printer.scan())      # will raise an error since its not a scanner


# ☑ Why? This avoids unnecessary method implementation in unrelated classes.