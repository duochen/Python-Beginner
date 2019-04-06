filename = "test.txt"

with open(filename, "r") as file_object:
    line = file_object.read()  
    print(type(line))           # => <class 'str'>
    print(line)                 # => hello world

