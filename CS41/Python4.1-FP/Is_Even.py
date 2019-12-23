def fib(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    else:
        lst = fib(n-1)
        lst.append(lst[-1] + lst[-2])
        return lst

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

fibs = fib(10)
a = [num for num in fibs if is_even(num)]
print(a)

b = filter(is_even, fibs)
print(list(b))