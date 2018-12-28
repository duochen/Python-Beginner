# Curly braces in strings  are placeholders
print('{} {}'.format('monty', 'python'))  # => monty python

# Provide values by position or by placeholder
print("{0} can be {1} {0}".format("strings", "formatted"))    # => strings can be formatted strings
print("{name} loves {food}".format(name="Sam", food="plums")) # => Sam loves plums

# Pro: Values are converted to string
print("{} squared is {}".format(5, 5 ** 2)) # => 5 squared is 25