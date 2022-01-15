burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

calories = 0

if burger == 1:
    calories = calories + 461
elif burger == 2:
    calories = calories + 431
elif burger == 3:
    calories = calories + 420

if drink == 1:
    calories = calories + 130
elif drink == 2:
    calories = calories + 160
elif drink == 3:
    calories = calories + 118

if side == 1:
    calories = calories + 100
elif side == 2:
    calories = calories + 57
elif side == 3:
    calories = calories + 70

if dessert == 1:
    calories = calories + 167
elif dessert == 2:
    calories = calories + 266
elif dessert == 3:
    calories = calories + 75

print(f'Your total Calorie count is {calories}.')
