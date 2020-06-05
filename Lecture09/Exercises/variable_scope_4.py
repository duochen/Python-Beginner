x = 4
def myfunc():
    x = 3
    def inner():
        nonlocal x  # global x
        x = x + 10
        print(x)
    inner()
    print(x)

myfunc()