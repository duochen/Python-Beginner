input_file = open('baseball.in', 'r')
output_file = open('baseball.out', 'w')

n = int(input_file.readline())

positions = []

for i in range(n):
    positions.append(int(input_file.readline()))

total = 0

for position1 in positions:
    for position2 in positions:
        first_two_diff = position2 - position1
        if first_two_diff > 0:
            low = position2 + first_two_diff
            high = position2 + first_two_diff * 2

            for position3 in positions:
                if position3 >= low and position3 <= high:
                    total = total + 1

output_file.write(f'{total}\n')

input_file.close()
output_file.close()
