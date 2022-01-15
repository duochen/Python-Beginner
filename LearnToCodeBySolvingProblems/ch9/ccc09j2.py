trout_points = int(input())
pike_points = int(input())
pickerel_points = int(input())
maximum_points = int(input())

total_ways = 0

for trout in range(maximum_points + 1):
    for pike in range(maximum_points + 1):
        for pickerel in range(maximum_points + 1):
            if (trout + pike + pickerel > 0 and
                    trout * trout_points +
                    pike * pike_points +
                    pickerel * pickerel_points <= maximum_points):
                output = f'{trout} Brown Trout, {pike} Northern Pike, '
                output = output + f'{pickerel} Yellow Pickerel'
                print(output)
                total_ways = total_ways + 1

print(f'Number of ways to catch fish: {total_ways}')
