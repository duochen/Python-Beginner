numbers = {1,2,3,4,5,6,7,8,9,10}
odd = {1,3,5,7,9}
even = {2,4,6,8,10}

print(odd.isdisjoint(even))    # => True
print(numbers.issuperset(odd)) # => True
print(odd.issuperset(numbers)) # => False
print(odd.issubset(numbers))   # => True