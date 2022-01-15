lst = input().split()
num_items = int(lst[0])
num_assignments = int(lst[1])

items = set()

for i in range(num_items):
    items.add(input())

total = 0

for i in range(num_assignments):
    num_in_assignment = int(input())
    assignment = set()
    for j in range(num_in_assignment):
        assignment.add(input())
    if assignment.issubset(items):
        total = total + 1

print(total)
