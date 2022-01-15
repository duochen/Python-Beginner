cards_by_value = [0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 16, 4]

n = int(input())

in_hand = 0

for i in range(n):
    card_val = int(input())
    in_hand = in_hand + card_val
    cards_by_value[card_val] = cards_by_value[card_val] - 1

x = 21 - in_hand

if sum(cards_by_value[x+1:]) >= sum(cards_by_value[:x+1]):
    print('DOSTA')
else:
    print('VUCI')
