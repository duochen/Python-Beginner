class Pizza:
    def __init__(self, radius, toppings, slices=8):
        self.radius = radius
        self.toppings = toppings
        self.slices_left = slices

    def eat_slice(self):
        if self.slices_left > 0:
            self.slices_left -= 1
        else:
            print("Oh no! Out of pizaa")

    def __repr__(self):
        return '{}" pizza'.format(self.radius)

p = Pizza(14, ("Pepperoni", "Olives"), slices=12)        
print(Pizza.eat_slice)   # => <function Pizza.eat_slice>

print(p.eat_slice)       # => <bound method Pizza.eat_slice of 14" Pizza>

method = p.eat_slice
print(method.__self__)   # => 14" Pizza
print(method.__func__)   # => <function Pizza.eat_slice>

p.eat_slice()            # Implicitly calls Pizza.eat_slice(p)