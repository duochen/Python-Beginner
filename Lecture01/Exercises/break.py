for n in range(10):
    if n == 6:
        break
    print(n, end=',') # => 0,1,2,3,4,5

for n in range(10):
    if n % 4 == 0:
        print("Even", n)
        continue
    print("Odd", n)