def split_stream(streams, stream, percentage):
    """
    streams is a list of stream flows.
    stream is a stream index.
    percentage is the percentage to allocate to the left stream.

    Return the stream flows with stream split into two streams
    using the percentage.
    """
    left = streams[stream] * percentage / 100
    right = streams[stream] - left
    return streams[:stream] + [left, right] + streams[stream+1:]


def join_streams(streams, stream):
    """
    streams is a list of stream flows.
    stream is a stream index.

    Return the streams with stream and its right neighbour
    joined into one stream.
    """
    left = streams[stream]
    right = streams[stream + 1]
    return streams[:stream] + [left + right] + streams[stream+2:]


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
        streams = split_stream(streams, stream, percentage)
    elif command == 88:
        stream = int(input()) - 1  # Subtract 1 to make it 0-indexed
        streams = join_streams(streams, stream)

for i in range(len(streams)):
    streams[i] = str(round(streams[i]))

output = ''
for amount in streams:
    output = output + amount + ' '

print(output[:-1])
