# Here's an O(n log n) solution.
# Rather than simulate the pouring process, we directly
# calculate the amount of liquid that would end up in each glass.

n = int(input())

glasses = []
total_liquid = 0
liquid_in_glass = {}

for i in range(n):
    lst = input().split()
    liquid = int(lst[0])
    capacity = int(lst[1])
    total_liquid = total_liquid + liquid
    glasses.append([capacity, i])
    liquid_in_glass[i] = 0

glasses.sort()
glasses.reverse()

i = 0

while total_liquid > 0:
    glass = glasses[i]
    capacity = glass[0]
    which = glass[1]
    pour = min(total_liquid, capacity)
    liquid_in_glass[which] = pour
    total_liquid = total_liquid - pour
    i = i + 1

print(n - i)  # i glasses are not empty now, so n - i are empty

result = []

for i in range(n):
    result.append(str(liquid_in_glass[i]))
print(' '.join(result))
