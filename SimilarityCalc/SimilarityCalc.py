file = open("input.txt")

listA, listB = [], []
counts = dict()
for line in file:
    chars = line.split()
    listA.append(int(chars[0]))
    listB.append(int(chars[1]))
    counts[int(chars[1])] = counts.get(int(chars[1]), 0) + 1

pairs = zip(sorted(listA), sorted(listB))

sum = 0
for a,b in pairs:
    sum += counts.get(a, 0) * a

print(sum)