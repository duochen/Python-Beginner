def check(x):
    if isinstance(x, str):
        return False
    if isinstance(x, int):
        return int(x) > 0

input =  [0, 1, 0, 6, 'A', 1, 0, 7]
output = filter(check, input)
print(list(output))