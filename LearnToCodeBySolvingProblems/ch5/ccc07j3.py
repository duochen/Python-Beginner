# Dollar amounts are numbered from 1, so I include a dummy 0
# at index 0

amounts = [0, 100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000,
           1000000]

n = int(input())

for i in range(n):
    used = int(input())
    amounts[used] = 0

total = 0
for amount in amounts:
    total = total + amount

average = total / (10 - n)

banker_offer = int(input())

if banker_offer > average:
    print('deal')
else:
    print('no deal')
