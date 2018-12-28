f = open('file.txt', 'w')
print(1 / 0)    # Crash
f.close()       # => Never called
f.closed        # => False
