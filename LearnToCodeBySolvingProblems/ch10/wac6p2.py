# Here's an O(n+m) solution.

# The approach is to watch the lights change, not flipping any of
# them ourselves yet, and keeping track of the number of lights that are on.
# The more seconds we watch, the more flips we store up.

# There are two cases:

# 1. Maybe during the m light changes, there's never a moment where we
#    have enough stored flips to shut off all of the lights. In that case,
#    the answer is the number of lights that are on after the m  light
#    changes, because we need to store up that many flips to shut off
#    all of these lights.

# 2. Otherwise, if we do find a moment in the m light changes where we can
#    shut off all of the lights, then that moment is our answer!


lst = input().split()
n = int(lst[0])
m = int(lst[1])

light_state = [0] + input().split()
for i in range(1, n + 1):
    light_state[i] = int(light_state[i])

lights_on = 0

for i in range(1, n + 1):
    if light_state[i] == 1:
        lights_on = lights_on + 1

light_change = input().split()
for i in range(m):
    light_change[i] = int(light_change[i])

second = 0

while second < m and second < lights_on:
    flip = light_change[second]
    if light_state[flip] == 1:
        light_state[flip] = 0
        lights_on = lights_on - 1
    else:
        light_state[flip] = 1
        lights_on = lights_on + 1
    second = second + 1

if second < lights_on:  # Case 1
    print(lights_on)
else:  # Case 2
    print(second)
