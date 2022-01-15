from bisect import bisect_left, bisect_right


input_file = open('haybales.in', 'r')
output_file = open('haybales.out', 'w')

lst = input_file.readline().split()
n = int(lst[0])
q = int(lst[1])

positions = input_file.readline().split()
for i in range(len(positions)):
    positions[i] = int(positions[i])

positions.sort()

for i in range(q):
    query = input_file.readline().split()
    low = int(query[0])
    high = int(query[1])
    left = bisect_left(positions, low)
    right = bisect_right(positions, high)
    answer = right - left
    output_file.write(f'{answer}\n')

input_file.close()
output_file.close()
