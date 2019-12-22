class Foo:
    counter = 0

c = Foo()
x = c

c.counter = 1
while c.counter < 10:
    c.counter = x.counter * 2
    print(c.counter)
del c.counter
print(c.counter)