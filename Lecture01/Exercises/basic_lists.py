# Create a new list
empty = []
letters = ['a', 'b', 'c', 'd']
numbers = [2, 3, 5]

# Lists can contain elements of different types
mixed = [4, 5, "seconds"]

# Append elements to the end of a list
numbers.append(7)
print(numbers)      # => [2, 3, 5, 7]
numbers.append(11)
print(numbers)      # => [2, 3, 5, 7, 11]

# Access elements at a particular index
print(numbers[0])   # => 2
print(numbers[-1])  # => 11

# You can also slice lists - the same rules apply
print(letters[:3])    # => ['a', 'b', 'c']
print(numbers[1:-1])  # => [3, 5, 7]  

# Lists really can contain anything - even other lists!
x = [letters, numbers]
print(x)        # => [['a', 'b', 'c', 'd'], [2, 3, 5, 7, 11]]
print(x[0])     # => ['a', 'b', 'c', 'd']
print(x[0][1])  # => b
print(x[1][2:]) # => [5, 7, 11]