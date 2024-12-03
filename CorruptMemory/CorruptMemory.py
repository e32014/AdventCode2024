import re

file = open('input.txt')
total = 0
enabled = True
for line in file:
    found = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line.strip())
    for command in found:
        if command.startswith("don't"):
            enabled = False
        elif command.startswith("do"):
            enabled = True
        elif command.startswith("mul") and enabled:
            vals = re.match("mul\((\d+),(\d+)\)", command)
            total += int(vals.group(1)) * int(vals.group(2))
print(total)