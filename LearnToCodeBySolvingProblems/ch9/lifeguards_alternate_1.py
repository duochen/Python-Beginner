# Overall approach:
# We first find the number of lifeguards that cover each time unit.
# Now, when we fire a lifeguard, we don't have to look through
# all of the other lifeguards' intervals.
# Instead, we see for each of the fired lifeguard's time units
# whether they were the only working lifeguard.


def coverage(intervals):
    """
    intervals is a list of lifeguard intervals;
    each interval is a [start, end] list.

    Return a dictionary mapping each time unit to the number of lifeguards
    that cover it.
    """
    time_to_coverage = {}
    for interval in intervals:
        for time in range(interval[0], interval[1]):
            if time not in time_to_coverage:
                time_to_coverage[time] = 1
            else:
                time_to_coverage[time] = time_to_coverage[time] + 1
    return time_to_coverage


def num_covered(time_to_coverage, fired_start, fired_end):
    """
    time_to_coverage is a dictionary mapping each time unit to the number of
    lifeguards that cover it.
    fired_start and fired_end are the endpoints of the fired
    lifeguard's interval.

    Return the number of time units covered by all lifeguards
    except the one fired.
    """
    covered = len(time_to_coverage)
    for time in range(fired_start, fired_end):
        if time_to_coverage[time] == 1:  # No other lifeguard here; time unit lost
            covered = covered - 1
    return covered


input_file = open('lifeguards.in', 'r')
output_file = open('lifeguards.out', 'w')

n = int(input_file.readline())

intervals = []

for i in range(n):
    interval = input_file.readline().split()
    interval[0] = int(interval[0])
    interval[1] = int(interval[1])
    intervals.append(interval)

time_to_coverage = coverage(intervals)
max_covered = 0

for fired_interval in intervals:
    result = num_covered(time_to_coverage, fired_interval[0], fired_interval[1])
    if result > max_covered:
        max_covered = result

output_file.write(f'{max_covered}\n')

input_file.close()
output_file.close()
