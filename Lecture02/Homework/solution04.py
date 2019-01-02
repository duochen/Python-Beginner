fruits = ['apple', 'mango', 'banana','cherry']

# dict comprehension to create dict with fruit name as keys
d = {f:len(f) for f in fruits}
print(d)        # => {'apple': 5, 'mango': 5, 'banana': 6, 'cherry': 6}