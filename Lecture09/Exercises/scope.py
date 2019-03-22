v = 6

def f(x):
    print("global: ", list(globals().keys()))
    print("entry local: ", locals())
    y = x
    w = v
    print("exit local: ", locals())