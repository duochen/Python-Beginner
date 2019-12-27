lines = []
while True:
    s = input("Please enter a word: ")
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print(sentence)    