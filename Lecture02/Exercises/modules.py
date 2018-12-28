# Import a module
import math

print(math.sqrt(16))  # => 4.0

# Import specific symbols from a module into the lcoal namepspace
from math import ceil, floor
print(ceil(3.7))      # => 4
print(floor(3.7))     # => 3

# Bind module symbols to a new symbol in the local namespace
from some_module import super_long_symbol_name as short_name

# Any python file (including those your write) is a module
from my_script import my_function, my_variable