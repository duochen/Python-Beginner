class Person:
    name = 'Adam'

p = Person()
print('Before modification:', p.name)

# Set name to 'John'
setattr(p, 'name', 'John')
print('After modification:', p.name)
