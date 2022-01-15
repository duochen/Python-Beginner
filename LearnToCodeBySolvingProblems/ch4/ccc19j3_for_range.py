n = int(input())

for dataset in range(n):
    result = ''
    line = input()
    total = 1

    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            total = total + 1
        else:
            result = result + f'{total} {line[i]} '
            total = 1

    result = result + f'{total} {line[-1]}'

    print(result)
