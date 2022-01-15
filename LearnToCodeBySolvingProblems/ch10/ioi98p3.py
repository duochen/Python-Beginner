num_lamps = int(input())
num_presses = int(input())

lamps_on = input().split()
lamps_on.pop()  # Remove the -1 at the end
for i in range(len(lamps_on)):
    lamps_on[i] = int(lamps_on[i])

lamps_off = input().split()
lamps_off.pop()  # Remove the -1 at the end
for i in range(len(lamps_off)):
    lamps_off[i] = int(lamps_off[i])

possible = set({})

# We track whether each button was pressed an even (0) or odd (1)
# number of times.
for button1 in [0, 1]:
    for button2 in [0, 1]:
        for button3 in [0, 1]:
            for button4 in [0, 1]:
                if button1 + button2 + button3 + button4 > num_presses:
                    continue
                if (button1 + button2 + button3 + button4) % 2 != num_presses % 2:
                    continue

                # 1 = on, 0 = off; all lamps start on
                status = [1] * num_lamps
                if button1 == 1:
                    status = [0] * num_lamps
                if button2 == 1:
                    for i in range(0, len(status), 2):
                        status[i] = 1 - status[i]
                if button3 == 1:
                    for i in range(1, len(status), 2):
                        status[i] = 1 - status[i]
                if button4 == 1:
                    for i in range(0, len(status), 3):
                        status[i] = 1 - status[i]

                good = True
                for lamp in lamps_on:
                    if status[lamp - 1] == 0:
                        good = False
                for lamp in lamps_off:
                    if status[lamp - 1] == 1:
                        good = False

                if good:
                    possible.add(tuple(status))

if not possible:
    print('IMPOSSIBLE')
else:
    for configuration in possible:
        configuration = list(configuration)
        for i in range(len(configuration)):
            configuration[i] = str(configuration[i])
        print(''.join(configuration))
