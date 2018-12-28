print(type(4))       # => <class 'int'>
print(isinstance(4, object)) # => True
print(id(4))  # => 1630497632 (Yours could be different!)
print((4).__sizeof__()) # =>  # => 28


type(1) != type(1.0)
    int != float
