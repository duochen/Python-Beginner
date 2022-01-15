# Replacing the input function with something faster
import sys
input = sys.stdin.readline


lst = input().split()
n = int(lst[0])
q = int(lst[1])
h = int(lst[2])

total_yield = 0
prefix_yield = [0]

for i in range(n):
    tree = input().split()
    tree_height = int(tree[0])
    tree_yield = int(tree[1])
    if tree_height > h:
        prefix_yield.append(total_yield)
    else:
        total_yield = total_yield + tree_yield
        prefix_yield.append(total_yield)

max_steal = 0

for i in range(q):
    steal_range = input().split()
    steal_left = int(steal_range[0])
    steal_right = int(steal_range[1])
    can_steal = prefix_yield[steal_right] - prefix_yield[steal_left - 1]
    if can_steal > max_steal:
        max_steal = can_steal

print(max_steal)
