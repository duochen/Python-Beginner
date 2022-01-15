FIRST_HALF = 1440


a = int(input())
times_a = []
for i in range(a):
    times_a.append(int(input()))

b = int(input())
times_b = []
for i in range(b):
    times_b.append(int(input()))


# Answer first question (points in first half)

first_half_points = 0

for i in range(a):
    if times_a[i] <= FIRST_HALF:
        first_half_points = first_half_points + 1

for i in range(b):
    if times_b[i] <= FIRST_HALF:
        first_half_points = first_half_points + 1

print(first_half_points)


# Answer second question (number of turnarounds)

# points_at_a[i] gives points scored by team A in first i seconds
points_at_a = [0]
i = 0
for second in range(1, FIRST_HALF * 2 + 1):
    if i < len(times_a) and times_a[i] == second:
        points_at_a.append(points_at_a[second - 1] + 1)
        i = i + 1
    else:
        points_at_a.append(points_at_a[second - 1])

# points_at_b[i] gives points scored by team B in first i seconds
points_at_b = [0]
i = 0
for second in range(1, FIRST_HALF * 2 + 1):
    if i < len(times_b) and times_b[i] == second:
        points_at_b.append(points_at_b[second - 1] + 1)
        i = i + 1
    else:
        points_at_b.append(points_at_b[second - 1])

turnarounds = 0
winning = 'x'

for i in range(FIRST_HALF * 2):
    if winning != 'a' and points_at_a[i] > points_at_b[i]:
        winning = 'a'
        turnarounds = turnarounds + 1
    elif winning != 'b' and points_at_b[i] > points_at_a[i]:
        winning = 'b'
        turnarounds = turnarounds + 1

# Subtract 1 because the team that scores first doesn't count as a turnaround
print(turnarounds - 1)
