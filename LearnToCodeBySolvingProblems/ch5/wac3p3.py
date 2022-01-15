moves = input()
num_combos = int(input())

combo_sequences = []
combo_points = []

for i in range(num_combos):
    lst = input().split()
    sequence = lst[0]
    points = int(lst[1])
    combo_sequences.append(sequence)
    combo_points.append(points)

points = len(moves)
i = 0

while i < len(moves):
    best_length = 0
    best_points = 0
    for j in range(len(combo_sequences)):
        combo_length = len(combo_sequences[j])
        if (combo_length > best_length and
                moves[i:i+combo_length] == combo_sequences[j]):
            best_length = combo_length
            best_points = combo_points[j]

    if best_length == 0:
        i = i + 1
    else:
        i = i + best_length
        points = points + best_points

print(points)
