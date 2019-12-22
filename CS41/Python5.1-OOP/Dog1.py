class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name
    
    def add_trick(self, trick):
        self.tricks.append(trick)

d1 = Dog('Brave')
d1.add_trick("trick1")
print(d1.tricks)
d2 = Dog('Shy')
d2.add_trick("trick2")
print(d2.tricks)
print(d1.tricks)
