FIRST_HALF = 1440


def points_in_first_half(times_a, times_b):
    """
    times_a is a list of the times when team A scored.
    times_b is a list of the times when team B scored.

    Return total points scored in first half.
    """
    points = 0

    for time in times_a:
        if time <= FIRST_HALF:
            points = points + 1

    for time in times_b:
        if time <= FIRST_HALF:
            points = points + 1

    return points


def points_at_times(times):
    """
    times is a list of the times when a team scored.

    Return a list lst, where lst[i] is the total points
    scored by the team in the first i seconds.
    """
    # points_at[i] gives points scored by team in first i seconds
    points_at = [0]
    i = 0
    for second in range(1, FIRST_HALF * 2 + 1):
        if i < len(times) and times[i] == second:
            points_at.append(points_at[second - 1] + 1)
            i = i + 1
        else:
            points_at.append(points_at[second - 1])
    return points_at


def num_turnarounds(points_at_a, points_at_b):
    """
    points_at_a is a list for team A as returned by points_at_times.
    points_at_b is a list for team B as returned by points_at_times.

    Return the number of turnarounds.
    """
    turnarounds = 0
    winning = 'x'
    for i in range(FIRST_HALF * 2):
        if winning != 'a' and points_at_a[i] > points_at_b[i]:
            winning = 'a'
            turnarounds = turnarounds + 1
        elif winning != 'b' and points_at_b[i] > points_at_a[i]:
            winning = 'b'
            turnarounds = turnarounds + 1
    # Subtract 1 because team that scores first doesn't count as a turnaround
    return turnarounds - 1


a = int(input())
times_a = []
for i in range(a):
    times_a.append(int(input()))

b = int(input())
times_b = []
for i in range(b):
    times_b.append(int(input()))

# Answer first question (points in first half)
print(points_in_first_half(times_a, times_b))

# Answer second question (number of turnarounds)
points_at_a = points_at_times(times_a)
points_at_b = points_at_times(times_b)
print(num_turnarounds(points_at_a, points_at_b))
