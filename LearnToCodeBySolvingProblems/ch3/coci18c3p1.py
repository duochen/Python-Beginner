word = input()

total = 0
match_position = 0

for char in word:
    if match_position == 0:
        match = 'H'
    elif match_position == 1:
        match = 'O'
    elif match_position == 2:
        match = 'N'
    else:
        match = 'I'
    if match == char:
        match_position = match_position + 1
        if match_position == 4:
            match_position = 0
            total = total + 1

print(total)
