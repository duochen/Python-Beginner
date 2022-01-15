NUM_COWS = 10


def cow_crossings(observations, cow):
    """
    observations is a list of observations; each observation is a list
    of two integers: [cow_number, side].
    cow is a cow number.

    Return number of times cow crosses in observations.
    """
    crossings = 0
    last_side = -1
    for observation in observations:
        if observation[0] == cow:
            if last_side != -1 and last_side != observation[1]:
                crossings = crossings + 1
            last_side = observation[1]
    return crossings


input_file = open('crossroad.in', 'r')
output_file = open('crossroad.out', 'w')

n = int(input_file.readline())

observations = []

for i in range(n):
    lst = input_file.readline().split()
    lst[0] = int(lst[0])
    lst[1] = int(lst[1])
    observations.append(lst)

total_crossings = 0

for i in range(1, NUM_COWS + 1):
    total_crossings = total_crossings + cow_crossings(observations, i)

output_file.write(f'{total_crossings}\n')

input_file.close()
output_file.close()
