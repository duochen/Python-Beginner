lst = input().split()
n = int(lst[0])
health = int(lst[1])

charlie_moves = []
for i in range(n):
    lst = input().split()
    move_name = lst[0]
    move_health = int(lst[1])
    charlie_moves.append([move_name, move_health])

opponent_moves = []
for i in range(n):
    lst = input().split()
    move_name = lst[0]
    move_health = int(lst[1])
    opponent_moves.append([move_name, move_health])

charlie_health = health
opponent_health = health

i = 0
while i < len(charlie_moves) and charlie_health > 0 and opponent_health > 0:
    if charlie_moves[i][0] == 'A' and (i == 0 or
                                       opponent_moves[i - 1][0] == 'A'):
        opponent_health = opponent_health - charlie_moves[i][1]
    elif charlie_moves[i][0] == 'D' and opponent_moves[i][0] == 'D':
        charlie_health = charlie_health - charlie_moves[i][1]
    if charlie_health > 0 and opponent_health > 0:
        if opponent_moves[i][0] == 'A' and charlie_moves[i][0] == 'A':
            charlie_health = charlie_health - opponent_moves[i][1]
        elif opponent_moves[i][0] == 'D' and (i == len(charlie_moves) - 1 or
                                              charlie_moves[i + 1][0] == 'D'):
            opponent_health = opponent_health - opponent_moves[i][1]
    i = i + 1

if opponent_health <= 0:
    print('VICTORY')
elif charlie_health <= 0:
    print('DEFEAT')
else:
    print('TIE')
