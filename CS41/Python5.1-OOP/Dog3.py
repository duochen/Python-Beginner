class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks =[]  # New list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')  
e = Dog('Buddy')
d.add_trick('roll over')  
e.add_trick('play dead')
print(d.tricks)	 # => ['roll over']
print(e.tricks)  # => ['play dead']
