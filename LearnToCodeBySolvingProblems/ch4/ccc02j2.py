done = False

while not done:
    word = input()
    if word == 'quit!':
        done = True
    elif len(word) > 4 and not (word[-3] in 'aeiouy') and word[-2:] == 'or':
        print(word[:-2] + 'our')
    else:
        print(word)
