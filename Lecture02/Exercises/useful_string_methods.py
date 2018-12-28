greeting = "Hello world!"

print(greeting[4])          # => o
print('world' in greeting)  # => True
print(len(greeting))        # => 12

print(greeting.find('lo'))  # => 3
print(greeting.replace('llo', 'y')) # => Hey world!
print(greeting.startswith('Hell'))  # => True
print(greeting.isalpha())   # => False

