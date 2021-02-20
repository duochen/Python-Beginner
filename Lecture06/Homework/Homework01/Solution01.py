nums = [3, 6, 12, 14]
target = 15
m = {}
n = len(nums)
for i in range(0,n):
    goal = target - nums[i]
    if(goal in m):
        print([m[goal], i])
    m[nums[i]] = i
        