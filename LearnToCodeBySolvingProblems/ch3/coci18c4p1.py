obeys = input()
n = int(input())

obeyed = obeys
total_obeys = 1

for i in range(n):
    line = input()
    winner = line[0]
    loser = line[2]
    if obeys == loser:
        obeys = winner
        if not winner in obeyed:
            total_obeys = total_obeys + 1
            obeyed = obeyed + winner

print(obeys)
print(total_obeys)
