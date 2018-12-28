with open('file.txt', 'w') as f:
    print(1/0)

f.closed                 # => True

