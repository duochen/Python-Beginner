# Replacing the input function with something faster
import sys
input = sys.stdin.readline


lst = input().split()
r = int(lst[0])
c = int(lst[1])

mysterious_rows = set()
mysterious_cols = set()

for i in range(r):
    row = input()
    for j in range(c):
        if row[j] == 'X':
            mysterious_rows.add(i + 1)
            mysterious_cols.add(j + 1)

q = int(input())

for i in range(q):
    position = input().split()
    col = int(position[0])
    row = int(position[1])
    if row in mysterious_rows or col in mysterious_cols:
        print('Y')
    else:
        print('N')
