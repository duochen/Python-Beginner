# Solution using a list (not a dictionary);
# not efficient enough to pass all test cases in time


input_file = open('citystate.in', 'r')
output_file = open('citystate.out', 'w')

n = int(input_file.readline())

cities = []

for i in range(n):
    lst = input_file.readline().split()
    cities.append(lst)

total = 0

for i in range(n):
    for j in range(i + 1, n):
        city1 = cities[i][0]
        state1 = cities[i][1]
        city2 = cities[j][0]
        state2 = cities[j][1]
        if city1[:2] == state2 and city2[:2] == state1 and state1 != state2:
            total = total + 1

output_file.write(f'{total}\n')

input_file.close()
output_file.close()
