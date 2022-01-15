# Overall approach:
# We find each interval of contiguous time covered by the lifeguards,
# and add up the time units covered by each of these intervals.


def covered(intervals, fired):
    """
    intervals is a list of lifeguard intervals;
    each interval is a [start, end] list.
    fired is the index of the lifeguard to fire.

    Return the number of time units covered by all lifeguards
    except the one fired.
    """
    intervals = intervals[:]
    intervals.pop(fired)
    if len(intervals) == 0:
        return 0

    total = 0
    cur_start = intervals[0][0]
    cur_end = intervals[0][1]
    for interval in intervals[1:]:
        if interval[0] > cur_end:
            total = total + cur_end - cur_start
            cur_start = interval[0]
            cur_end = interval[1]
        elif interval[1] > cur_end:
            cur_end = interval[1]
    total = total + cur_end - cur_start
    return total


input_file = open('lifeguards.in', 'r')
output_file = open('lifeguards.out', 'w')

n = int(input_file.readline())

intervals = []

for i in range(n):
    interval = input_file.readline().split()
    interval[0] = int(interval[0])
    interval[1] = int(interval[1])
    intervals.append(interval)

intervals.sort()

max_covered = 0
for fired in range(n):
    result = covered(intervals, fired)
    if result > max_covered:
        max_covered = result

output_file.write(f'{max_covered}\n')

input_file.close()
output_file.close()
