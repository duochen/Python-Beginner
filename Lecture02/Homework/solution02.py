n = int(input("Input a number: "))
d = dict()

for x in range(1, n+1):
    d[x] = x*x

print(d)

# Input a number: 10
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}