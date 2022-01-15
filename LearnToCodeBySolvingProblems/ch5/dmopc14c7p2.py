n = int(input())
readings = input().split()

for i in range(len(readings)):
    readings[i] = int(readings[i])

index_smallest = readings.index(min(readings))
index_biggest = readings.index(max(readings))

if index_biggest < index_smallest:
    print('unknown')
else:
    is_sorted = True
    i = index_smallest
    while i < index_biggest and is_sorted:
        if readings[i] > readings[i + 1]:
            is_sorted = False
        i = i + 1

    if is_sorted:
        print(readings[index_biggest] - readings[index_smallest])
    else:
        print('unknown')
