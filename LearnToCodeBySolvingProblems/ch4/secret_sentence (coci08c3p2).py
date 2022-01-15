sentence = input()

result = ''
i = 0

while i < len(sentence):
    result = result + sentence[i]
    if sentence[i] in 'aeiou':
        i = i + 3
    else:
        i = i + 1

print(result)
