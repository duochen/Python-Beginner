def tali(inputs):
    comp = {}
    nums = inputs.split(',')
    for idx in range(len(nums)):
        lst = [int(i) for i in nums[idx].strip()]
        if set(lst)=={1,3,4,6}:
            lst=[9,9,9,9]      
        comp[chr(idx+65)] = sorted(lst, reverse=True)
    winners = [player for player in comp.keys() if comp[player] == max(comp.values())]
    return ','.join(winners)
print(tali('6466, 6661, 4144, 4113'))
print(tali('6431, 1443, 4331, 6643'))
print(tali('6666, 6666, 6666, 1331'))
print(tali('3434, 1166, 3313, 1144'))
print(tali('6616, 4666, 4646, 6664'))