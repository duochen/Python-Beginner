n = int(input())

student = ''
for i in range(n):
    student = student + input()

    answer_key = ''
for i in range(n):
    answer_key = answer_key + input()

correct = 0

for i in range(n):
    if student[i] == answer_key[i]:
        correct = correct + 1

print(correct)
