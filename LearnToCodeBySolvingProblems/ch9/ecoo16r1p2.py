for dataset in range(10):
    n = int(input())
    spinner = input().split()
    for i in range(len(spinner)):
        spinner[i] = int(spinner[i])
    spinner = set(spinner)  # Remove duplicates
    targets = input().split()
    for i in range(len(targets)):
        targets[i] = int(targets[i])
    can_make = [False] * len(targets)

    for spin1 in spinner:
        for roll1 in [5, 6]:
            for spin2 in spinner:
                for roll2 in [5, 6]:
                    for spin3 in spinner:
                        score = spin1
                        if roll1 == 5:
                            score = score + spin2
                        else:
                            score = score * spin2
                        if roll2 == 5:
                            score = score + spin3
                        else:
                            score = score * spin3

                        if score in targets:
                            where = targets.index(score)
                            can_make[where] = True

    output = ''
    for value in can_make:
        if value:
            output = output + 'T'
        else:
            output = output + 'F'
    print(output)
