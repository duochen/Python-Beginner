class Dog:
    # Let's try a default argument!
    def __init__(self, name='', tricks=[]):
        self.name = name
        self.tricks = tricks

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')        
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')

print(d.tricks)   # => ['roll over', 'play dead'] (shared value)
print(e.tricks)   # => ['roll over', 'play dead'] (shared value)   

f = Dog('Fido', tricks=[])
g = Dog('Buddy', tricks=[])
f.add_trick('roll over')
g.add_trick('play dead')

print(f.tricks)   # => ['roll over'] (unique value)
print(g.tricks)   # => ['play dead'] (unique value)   
