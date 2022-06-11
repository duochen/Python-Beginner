class Resturaunt:
    def __init__ (self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        print (f" {self.name} is the name of the resturaunt")

    def cuisine_type (self):
        print (f" {self.cuisine} is the cuisine")


resturaunt = Resturaunt ('CPK', 'Italian')
resturaunt.describe()
resturaunt.cuisine_type()
print (resturaunt.name)
print (resturaunt.cuisine)
