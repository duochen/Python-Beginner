n = int(input())

registered = []

for i in range(n):
    registered.append(input())

finished = []

for i in range(n - 1):
    finished.append(input())

registered.sort()
finished.sort()

# The lists are sorted, so we can search for the first mismatch;
# that's the person who didn't finish
i = 0
while i < n - 1 and registered[i] == finished[i]:
    i = i + 1

print(registered[i])
