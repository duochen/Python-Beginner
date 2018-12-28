def parrot(voltage, state='a stiff', action='voom',  type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')  
    print("if you put", voltage, "volts through it.")  
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# 1 positional argument  
parrot(1000)
# 1 keyword argument
parrot(voltage=1000)  
# 2 keyword arguments
parrot(voltage=1000000, action='VOOOOOM')
# 2 keyword arguments  
parrot(action='VOOOOOM', voltage=1000000)   
# 3 positional arguments
parrot('a million', 'bereft of life', 'jump')
# 1 positional, 1 keyword
parrot('a thousand', state='pushing up the daisies')

# required argument missing  
parrot()
# non-keyword argument after a keyword argument  
parrot(voltage=5.0, 'dead')
# duplicate value for the same argument
parrot(110, voltage=220)
# unknown keyword argument  
parrot(actor='John Cleese')
