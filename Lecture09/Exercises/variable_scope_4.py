x = 4
def myfunc():
    x = 3
    def inner():
        nonlocal x  # global x
        print(x)
    inner()

myfunc()