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

# Overall approach:
# We consider each streak of points during which only one team scores.
# We check if that streak changes the state from one team losing to winning.

# This list will contain the team names in order of when they scored points;
# that is, it merges two sorted lists into one
order = []

i = 0
j = 0

while i < len(times_a) and j < len(times_b):
    if times_a[i] < times_b[j]:
        order.append('A')
        i = i + 1
    else:
        order.append('B')
        j = j + 1

for remaining_a in times_a[i:]:
    order.append('A')

for remaining_b in times_b[j:]:
    order.append('B')

points_a = 0
points_b = 0
turnarounds = 0
i = 0

while i < len(order):
    start = i
    new_points_a = points_a
    new_points_b = points_b
    while i < len(order) and order[i] == order[start]:
        if order[i] == 'A':
            new_points_a = new_points_a + 1
        else:
            new_points_b = new_points_b + 1
        i = i + 1
    changed = ((points_a < points_b and new_points_a > new_points_b) or
               (points_b < points_a and new_points_b > new_points_a))
    if changed:
        turnarounds = turnarounds + 1
    points_a = new_points_a
    points_b = new_points_b

print(turnarounds)
