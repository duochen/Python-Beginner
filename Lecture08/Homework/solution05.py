def addition(a, b):
    if a + b == 0:
        raise Exception
    else:
        return a + b

try:
    addition(0,0)
except:
    print("the values are zero")