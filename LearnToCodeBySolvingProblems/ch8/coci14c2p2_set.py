# Overall approach:
# All but one name in the input shows up an even number of times,
# because each one is registered and finishes the race.
# The remaining name in the input shows up an odd number of times,
# because a person with that name registered but didn't finish.
# We keep a set of names: if a name is not in the set,
# then we have seen it an even number of times;
# if it is in the set, then we have seen it an odd number of times.
# When we're done, the set will have only one name, and we print it.


n = int(input())

people = set()

for i in range(2 * n - 1):
    person = input()
    if not person in people:
        people.add(person)
    else:
        people.remove(person)

print(people.pop())
