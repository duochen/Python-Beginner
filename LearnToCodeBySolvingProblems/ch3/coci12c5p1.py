composition = input()

a_minor = 0
c_major = 0

for i in range(len(composition)):
    if i == 0 or composition[i - 1] == '|':
        if composition[i] in 'ADE':
            a_minor = a_minor + 1
        if composition[i] in 'CFG':
            c_major = c_major + 1

if a_minor == c_major:
    if composition[-1] == 'A':
        a_minor = a_minor + 1
    else:
        c_major = c_major + 1

if a_minor > c_major:
    print('A-mol')  # A-minor
else:
    print('C-dur')  # C-major
