import re

file = open("input.txt")

def evaluate(numbers, total, target):
    if len(numbers) == 0:
        return total == target
    if total > target:
        return False
    return evaluate(numbers[1:], total * numbers[0], target) or evaluate(numbers[1:], total + numbers[0], target) or evaluate(numbers[1:], int(str(total) + str(numbers[0])), target)

formulas = []
for line in file:
    formulas.append([int(num) for num in re.split(":? +", line.strip())])

total = 0
for formula in formulas:
    if evaluate(formula[1:], 0, formula[0]):
        total += formula[0]
print(total)