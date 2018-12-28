languages = ["python", "perl", "java", "c++"]
a = [len(s) for s in languages]
print(a)   # => [6, 4, 4, 3]

b = list(map(len, languages))
print(b)   # => [6, 4, 4, 3]

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

fibs = [1, 1, 2, 3, 5, 8, 13, 21, 24]
c = [num for num in fibs if is_even(num)]
print(c)

d = filter(is_even, fibs)
for i in d:
    print(i)

map(float, ['1.0', '3.3', '-4.2'])


def sum(list):
    total = 0
    for i in list:
        total += i
    return total

def display_result(iter):
    for element in iter:
        print(element)

e =  [[1,3], [4, 2, -5]]
result = map(sum, e)
display_result(result)

f = [1, True, [2, 3]]

def add(element):
    return element + " : "

map(add, f)