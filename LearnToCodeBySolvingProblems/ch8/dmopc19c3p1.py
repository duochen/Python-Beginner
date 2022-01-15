n = int(input())
lst = input().split()

num_to_occurrences = {}

for num in lst:
    num = int(num)
    if not num in num_to_occurrences:
        num_to_occurrences[num] = 1
    else:
        num_to_occurrences[num] = num_to_occurrences[num] + 1

most = max(num_to_occurrences.values())

nums = list(num_to_occurrences)
nums.sort()

modes = []

for num in nums:
    if num_to_occurrences[num] == most:
        modes.append(num)

for i in range(len(modes)):
    modes[i] = str(modes[i])
print(' '.join(modes))
