k = int(input())

a = 1
b = 0

for i in range(k):
    new_a = b
    new_b = a + b
    a = new_a
    b = new_b

print(a, b)
