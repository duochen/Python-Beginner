def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')  
    print("if you put", voltage, "volts through it.")  
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# 1 position argument
parrot(1000)

# 1 keyword argument
parrot(voltage=1000)

# 2 keyword arguments
parrot(voltage=1000000, action='vooooom')

# 2 keyword arguments
parrot(action='vooooom', voltage=1000000)

# 3 positional arguments
parrot('a million', 'bereft of life', 'jump')

# 1 positional, 1 keyword
parrot('a thousand', state='pushing up the daisies')


