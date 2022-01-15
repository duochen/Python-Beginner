input_file = open('whereami.in', 'r')
output_file = open('whereami.out', 'w')

n = int(input_file.readline())
s = input_file.readline().strip()

k = 1
found = False

while not found:
    i = 0
    only_one = True
    while i < len(s) - k and only_one:
        if s[i:i+k] in s[i+1:]:
            only_one = False
        i = i + 1

    if only_one:
        found = True
    else:
        k = k + 1

output_file.write(f'{k}\n')

input_file.close()
output_file.close()
