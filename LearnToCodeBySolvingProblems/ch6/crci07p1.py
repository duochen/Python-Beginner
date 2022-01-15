def covers(platform, horizontal_pos):
    """
    platform is a platform; i.e. [height, left, right].
    horizontal_pos is an integer.

    Return True if platform covers horizontal_pos, False otherwise.
    """
    return platform[1] <= horizontal_pos and platform[2] >= horizontal_pos


def pillar_from(platforms, height, horizontal_pos):
    """
    platforms is a list of platforms.
    height is a vertical position.
    horizontal_pos is a horizontal position.

    Return the minimum length of pillar from height and horizontal_pos
    to the platform/ground below.
    """
    bottom = 0
    for platform in platforms:
        if (platform[0] < height and platform[0] > bottom and
                covers(platform, horizontal_pos)):
            bottom = platform[0]
    return height - bottom


n = int(input())

platforms = []

for i in range(n):
    platform = input().split()
    for j in range(len(platform)):
        platform[j] = int(platform[j])
    platforms.append(platform)

total = 0

for platform in platforms:
    total = total + pillar_from(platforms, platform[0], platform[1] + 0.5)
    total = total + pillar_from(platforms, platform[0], platform[2] - 0.5)

print(total)
