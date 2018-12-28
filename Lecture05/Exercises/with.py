# This is what enables us to use with ... as ...
with open(filename) as f:
    raw = f.read()

# is (almost) equivalent to 
f = open(filename)
f.__enter__()
try:
    raw = f.read()
finally:
    f.__exit__()        # Closes the file