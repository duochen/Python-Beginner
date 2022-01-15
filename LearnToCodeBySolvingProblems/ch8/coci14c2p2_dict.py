n = int(input())

registered = {}

for i in range(n):
    person = input()
    if not person in registered:
        registered[person] = 1
    else:
        registered[person] = registered[person] + 1

finished = {}

for i in range(n - 1):
    person = input()
    if not person in finished:
        finished[person] = 1
    else:
        finished[person] = finished[person] + 1

for person in registered:
    if not person in finished or registered[person] > finished[person]:
        print(person)
