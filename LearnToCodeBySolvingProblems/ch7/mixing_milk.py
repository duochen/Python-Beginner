NUM_BUCKETS = 3
NUM_POURS = 100


input_file = open('mixmilk.in', 'r')
output_file = open('mixmilk.out', 'w')

capacities = []
amounts = []

for i in range(NUM_BUCKETS):
    lst = input_file.readline().split()
    capacity = int(lst[0])
    amount = int(lst[1])
    capacities.append(capacity)
    amounts.append(amount)

for i in range(NUM_POURS):
    first = i % NUM_BUCKETS  # Pour from bucket
    second = (first + 1) % NUM_BUCKETS  # Pour to bucket
    # Pour the amount in first or the space in second
    # (whichever is smaller).
    # We can call min with multiple arguments instead of a list
    pour = min(amounts[first], capacities[second] - amounts[second])
    amounts[first] = amounts[first] - pour
    amounts[second] = amounts[second] + pour

for i in range(NUM_BUCKETS):
    output_file.write(f'{amounts[i]}\n')

input_file.close()
output_file.close()
