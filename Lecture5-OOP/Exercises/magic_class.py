class MagicClass:
    def __init__(self): 
        print("__init__")
    def __str__(self):
        print("__str__")
        return "MagicClass"
    def __eq__(self, other):
        print("__eq__")    
        return True
    def __lt__(self, other):
        print("__lt__")    
        return True        
    def __add__(self, other):
        print("__add__")    
        return 100                

x = MagicClass()        
y = MagicClass()

str(x)  # => x.__str__()
x == y  # => x.__eq__(y)

x < y   # => x.__lt__(y)
x + y   # => x.__add__(y)
