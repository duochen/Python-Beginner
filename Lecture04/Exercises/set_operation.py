my_set = {1.0, "Hello", (1,2,3)}
print(my_set) # => {1.0, 'Hello', (1, 2, 3)}

set_with_lists = {[1,2,3]} # => ypeError: unhashable type: 'list'

set_with_lists = set([1,2,3])
print(type(set_with_lists)) # => <class 'set'>
print(set_with_lists) # => {1, 2, 3}