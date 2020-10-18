def sum(*args):
    r = 0
    for i in args: 
        r += i
    return r

print(sum(1,2,3))
print(sum(1,2,3,4,5))