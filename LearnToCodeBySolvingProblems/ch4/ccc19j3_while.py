n = int(input())

for dataset in range(n):
    result = ''
    line = input()
    i = 0

    while i < len(line):
        total = 1
        while i < len(line) - 1 and line[i] == line[i + 1]:
            i = i + 1
            total = total + 1
        result = result + f'{total} {line[i]} '
        i = i + 1

    print(result.strip())
