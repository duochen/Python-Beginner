zoe = {"type":"cat", "owner":"duo"}
rocky = {"type":"dog", "owner":"jie"}
pets = [zoe, rocky]
for item in pets:
    for k in item:
        print(k, item[k])

        