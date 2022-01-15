n = int(input())

streams = []

for i in range(n):
    streams.append(int(input()))

done = False

while not done:
    command = int(input())
    if command == 77:
        done = True
    elif command == 99:
        stream = int(input()) - 1  # Subtract 1 to make it 0-indexed
        percentage = int(input())
        left = streams[stream] * percentage / 100
        right = streams[stream] - left
        streams = streams[:stream] + [left, right] + streams[stream+1:]
    elif command == 88:
        stream = int(input()) - 1  # Subtract 1 to make it 0-indexed
        left = streams[stream]
        right = streams[stream + 1]
        streams = streams[:stream] + [left + right] + streams[stream+2:]

for i in range(len(streams)):
    streams[i] = str(round(streams[i]))

output = ''
for amount in streams:
    output = output + amount + ' '

print(output[:-1])
