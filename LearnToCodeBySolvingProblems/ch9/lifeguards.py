def num_covered(intervals, fired):
    """
    intervals is a list of lifeguard intervals;
    each interval is a [start, end] list.
    fired is the index of the lifeguard to fire.

    Return the number of time units covered by all lifeguards
    except the one fired.
    """
    covered = set()
    for i in range(len(intervals)):
        if i != fired:
            interval = intervals[i]
            for j in range(interval[0], interval[1]):
                covered.add(j)
    return len(covered)


input_file = open('lifeguards.in', 'r')
output_file = open('lifeguards.out', 'w')

n = int(input_file.readline())

intervals = []

for i in range(n):
    interval = input_file.readline().split()
    interval[0] = int(interval[0])
    interval[1] = int(interval[1])
    intervals.append(interval)

max_covered = 0

for fired in range(n):
    result = num_covered(intervals, fired)
    if result > max_covered:
        max_covered = result

output_file.write(f'{max_covered}\n')

input_file.close()
output_file.close()
