class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 36)        
print(p.name)   # => John
print(p.age)    # => 36
p.age = 40
print(p.age)    # => 40