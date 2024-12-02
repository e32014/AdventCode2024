file = open("input.txt")

def safe_check(vals):
    diffs = []
    for i in range(len(vals) - 1):
        diffs.append(vals[i] - vals[i + 1])
    if (all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)) and all(
            0 < abs(diff) < 4 for diff in diffs):
        return True

safeCount = 0
for line in file:
    vals = [int(x) for x in line.split()]
    if safe_check(vals):
        safeCount += 1
    else:
        for i in range(len(vals)):
            newVals = vals[0:i] + vals[i+1:]
            if safe_check(newVals):
                safeCount += 1
                break

print(safeCount)