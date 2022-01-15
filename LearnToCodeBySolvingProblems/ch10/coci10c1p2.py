# Here's an O(n) solution.


def max_consecutive(desks, grade):
    """
    desks is a list of desks; each desk is a list of two grades.
    grade is a grade to check.

    Return the maximum number of consecutive desks containing grade.
    """
    max_students = 0
    current_students = 0
    for desk in desks:
        if desk[0] == grade or desk[1] == grade:
            current_students = current_students + 1
            if current_students > max_students:
                max_students = current_students
        else:
            current_students = 0
    return max_students


n = int(input())

desks = []

for i in range(n):
    desk = input().split()
    desk[0] = int(desk[0])
    desk[1] = int(desk[1])
    desks.append(desk)

max_students = 0
smallest_grade = 0

for grade in range(1, 6):
    result = max_consecutive(desks, grade)
    if result > max_students:
        max_students = result
        smallest_grade = grade

print(max_students, smallest_grade)
