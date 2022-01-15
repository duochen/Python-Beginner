lst = input().split()
n = int(lst[0])
d = int(lst[1])

people = input().split()
for i in range(n):
    people[i] = int(people[i])

for i in range(d):
    ni = int(input())
    f_sum = sum(people[:ni])
    s_sum = sum(people[ni:])
    if f_sum >= s_sum:
        people = people[ni:]
        print(f_sum)
    else:
        people = people[:ni]
        print(s_sum)
