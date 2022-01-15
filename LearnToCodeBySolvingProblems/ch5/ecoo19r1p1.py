for dataset in range(10):
    lst = input().split()
    n = int(lst[0])
    m = int(lst[1])
    d = int(lst[2])

    events = input().split()
    for i in range(m):
        events[i] = int(events[i])

    events.sort()

    clean_shirts = n
    laundry_times = 0
    event_index = 0

    for day in range(1, d + 1):
        if clean_shirts == 0:
            laundry_times = laundry_times + 1
            clean_shirts = n
        clean_shirts = clean_shirts - 1
        while event_index < len(events) and events[event_index] == day:
            clean_shirts = clean_shirts + 1
            n = n + 1
            event_index = event_index + 1

    print(laundry_times)
