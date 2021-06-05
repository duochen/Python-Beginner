def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('afer f?')
a()