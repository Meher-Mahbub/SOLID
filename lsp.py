# Liskov Substitution Principle --> A subclass should be replaceable for its parent class without breaking the system.

# ✅ Example: A subclass must not break expected behavior


# class Bird:
#     def fly(self):
#         return "I can fly!"
    
# class Sparrow(Bird):
#     pass

# class Penguin(Bird):
#     def fly(self):
#         return "I can't fly"
    

# def make_bird_fly(bird):
#     print(bird.fly())
    
# make_bird_fly(Sparrow())
# make_bird_fly(Penguin())


# Error --> Penguin, however, overrides fly() with "I can't fly!", 
#       --> breaking the expectation that all birds can fly. 
# Fix   --> Use an Abstract Base Class and Separate Behaviors

from abc import ABC, abstractmethod
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass
    
class FlyingBird(Bird):
    def move(self):
        return "I can fly"

class NonFlyingBird(Bird):
    def move(self):
        return "I walk or swim"
    
class Sparrow(FlyingBird):
    pass

class Penguin(NonFlyingBird):
    pass
    

def make_bird_move(bird):
    print(bird.move())
    
make_bird_move(Sparrow())
make_bird_move(Penguin())



# ✔ LSP is now followed → Penguin is not forced to override fly().
# ✔ Clear separation → FlyingBird and NonFlyingBird handle movement properly.