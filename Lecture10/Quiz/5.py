# def f(a, b):
#     pass

# x = 2

def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')

a()