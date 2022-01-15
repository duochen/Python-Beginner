def solve(shell_a, shell_b, guesses, pebble_location):
    """
    shell_a and shell_b are parallel lists of integers;
    shell_a[i] and shell_b[i] give the shells swapped in swap i.
    guesses is a list of integer guesses, one for each swap.
    pebble_location is the starting location of the pebble.

    Return the number of correct guesses for the swaps
    with the starting pebble_location.
    """
    num_correct = 0
    for i in range(len(shell_a)):
        if shell_a[i] == pebble_location:
            pebble_location = shell_b[i]
        elif shell_b[i] == pebble_location:
            pebble_location = shell_a[i]
        if guesses[i] == pebble_location:
            num_correct = num_correct + 1
    return num_correct


input_file = open('shell.in', 'r')
output_file = open('shell.out', 'w')

n = int(input_file.readline())

shell_a = []
shell_b = []
guesses = []

for i in range(n):
    lst = input_file.readline().split()
    shell_a.append(int(lst[0]))
    shell_b.append(int(lst[1]))
    guesses.append(int(lst[2]))

max_correct = 0

for starting_location in [1, 2, 3]:
    num_correct = solve(shell_a, shell_b, guesses, starting_location)
    if num_correct > max_correct:
        max_correct = num_correct

output_file.write(f'{max_correct}\n')

input_file.close()
output_file.close()
