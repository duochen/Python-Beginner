input_file = open('lostcow.in', 'r')
output_file = open('lostcow.out', 'w')

lst = input_file.readline().split()
fj_start = int(lst[0])
bessie = int(lst[1])

found = False  # Haven't found Bessie yet
total = 0
cur_round = 0
fj_last = fj_start

while not found:
    fj_dist = 2 ** cur_round
    if cur_round % 2 == 0:  # Move right
        fj_next = fj_start + fj_dist
        if fj_last <= bessie and bessie <= fj_next:
            found = True
            total = total + bessie - fj_last
        else:
            total = total + fj_next - fj_last
    else:  # Move left
        fj_next = fj_start - fj_dist
        if fj_next <= bessie and bessie <= fj_last:
            found = True
            total = total + fj_last - bessie
        else:
            total = total + fj_last - fj_next
    fj_last = fj_next
    cur_round = cur_round + 1

output_file.write(f'{total}\n')

input_file.close()
output_file.close()
