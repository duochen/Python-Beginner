for dataset in range(10):
    num_routes = int(input())

    min_diameter = 100000
    min_diameter_ids = []

    for i in range(num_routes):
        info = input().split()
        for j in range(len(info)):
            info[j] = int(info[j])
        identifier = info[0]
        diameters = info[2:]
        min_here = min(diameters)

        if min_here < min_diameter:
            min_diameter = min_here
            min_diameter_ids = [identifier]
        elif min_here == min_diameter:
            min_diameter_ids.append(identifier)

    min_diameter_ids.sort()

    for i in range(len(min_diameter_ids)):
        min_diameter_ids[i] = str(min_diameter_ids[i])

    s = ','.join(min_diameter_ids)
    print(f'{min_diameter} {{{s}}}')
