x = [1, 2, 3, 4, 5]

def square(num):
    return num*num

result = map(square, x)
print(list(result))