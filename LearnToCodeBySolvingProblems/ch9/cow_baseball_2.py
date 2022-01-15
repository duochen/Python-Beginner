input_file = open('baseball.in', 'r')
output_file = open('baseball.out', 'w')

n = int(input_file.readline())

positions = []

for i in range(n):
    positions.append(int(input_file.readline()))

positions.sort()

total = 0

for i in range(n):
    for j in range(i + 1, n):
        first_two_diff = positions[j] - positions[i]
        low = positions[j] + first_two_diff
        high = positions[j] + first_two_diff * 2

        left = j + 1
        while left < n and positions[left] < low:
            left = left + 1

        right = left
        while right < n and positions[right] <= high:
            right = right + 1

        total = total + right - left

output_file.write(f'{total}\n')

input_file.close()
output_file.close()
