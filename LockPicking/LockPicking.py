from itertools import product

file = open('input.txt')

isKey = None
curr = [-1,-1,-1,-1,-1]

keys = []
locks = []
for line in file:
    if line.strip() == '':
        if isKey:
            keys.append(curr)
        else:
            locks.append(curr)
        isKey = None
        curr = [-1,-1,-1,-1,-1]
        continue
    if '#' not in line and isKey is None:
        isKey = True
    elif '#' in line and isKey is None:
        isKey = False
    for i, char in enumerate(line.strip()):
        if char == '#':
            curr[i] += 1

if isKey:
    keys.append(curr)
else:
    locks.append(curr)

count = 0
for key, lock in product(keys, locks):
    valid = True
    for i in range(len(key)):
        if key[i] + lock[i] >= 6:
            valid = False
            break
    if valid:
        count += 1

print(count)