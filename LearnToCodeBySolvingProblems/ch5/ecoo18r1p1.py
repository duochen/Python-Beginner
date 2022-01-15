for dataset in range(10):
    lst = input().split()
    t = int(lst[0])
    n = int(lst[1])

    cat_time = 0

    for i in range(n):
        day = input()
        if day == 'B':
            cat_time = cat_time + t - 1
        else:
            if cat_time > 0:
                cat_time = cat_time - 1

    print(cat_time)
