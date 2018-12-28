data_source = ['hello', 'world', 'iterator']
for data in data_source:
    print(data)  # => hello world iterator

# is really
for data in iter(data_source):
    print(data)  # => hello world iterator