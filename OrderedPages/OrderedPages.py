file = open('input.txt')

def check_valid(vals, rules):
    for i, val in enumerate(vals):
        for compare in vals[i+1:]:
            if compare not in rules.get(val,{}):
                return False
    return True

rules = dict()

line = file.readline().strip()
while line:
    first, last = line.split("|")
    if first not in rules:
        rules[first] = {last}
    else:
        rules[first].add(last)
    line = file.readline().strip()

print(rules)
consider = file.readline().strip()
total = 0
invalidTotal = 0
while consider:
    vals = consider.split(",")
    if check_valid(vals, rules):
        total += int(vals[len(vals) // 2])
    else:
        val_pairs = dict()
        for i, val1 in enumerate(vals):
            val_pairs[val1] = 0
            for j, val2 in enumerate(vals):
                if i == j:
                    continue
                if val2 in rules.get(val1, {}):
                    val_pairs[val1] += 1
        vals = [item[0] for item in sorted(val_pairs.items(), key= lambda item: item[1],reverse=True)]
        invalidTotal += int(vals[len(vals) // 2])



    consider = file.readline().strip()
print(total)
print(invalidTotal)