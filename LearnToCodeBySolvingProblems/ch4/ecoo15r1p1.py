for dataset in range(10):
    num_orange = 0
    num_blue = 0
    num_green = 0
    num_yellow = 0
    num_pink = 0
    num_violet = 0
    num_brown = 0
    num_red = 0

    done = False

    while not done:
        line = input()
        if line == 'end of box':
            done = True
        elif line == 'orange':
            num_orange = num_orange + 1
        elif line == 'blue':
            num_blue = num_blue + 1
        elif line == 'green':
            num_green = num_green + 1
        elif line == 'yellow':
            num_yellow = num_yellow + 1
        elif line == 'pink':
            num_pink = num_pink + 1
        elif line == 'violet':
            num_violet = num_violet + 1
        elif line == 'brown':
            num_brown = num_brown + 1
        elif line == 'red':
            num_red = num_red + 1

    handfuls = ((num_orange + 6) // 7 + (num_blue + 6) // 7 +
                (num_green + 6) // 7 + (num_yellow + 6) // 7 +
                (num_pink + 6) // 7 + (num_violet + 6) // 7 +
                (num_brown + 6) // 7)

    print(handfuls * 13 + num_red * 16)
