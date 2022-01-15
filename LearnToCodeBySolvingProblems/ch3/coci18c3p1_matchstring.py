word = input()

total = 0
match_position = 0
match_string = 'HONI'

for char in word:
    match = match_string[match_position]
    if match == char:
        match_position = match_position + 1
        if match_position == 4:
            match_position = 0
            total = total + 1

print(total)
