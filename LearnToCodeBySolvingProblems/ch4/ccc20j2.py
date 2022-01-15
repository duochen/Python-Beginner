target_infected = int(input())
num_infected = int(input())
person_infects = int(input())

day = 0
prev_day = num_infected

while num_infected <= target_infected:
    num_infected = num_infected + prev_day * person_infects
    prev_day = prev_day * person_infects
    day = day + 1

print(day)
