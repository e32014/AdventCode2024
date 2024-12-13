import re

file = open('input.txt')
next_line = file.readline().strip()
total = 0
mod = 10000000000000
while next_line:
    part_a = re.match("Button A: X\+(\d+), Y\+(\d+)", next_line)
    next_line = file.readline().strip()
    part_b = re.match("Button B: X\+(\d+), Y\+(\d+)", next_line)
    next_line = file.readline().strip()
    goal = re.match("Prize: X=(\d+), Y=(\d+)", next_line)
    file.readline().strip()
    next_line = file.readline().strip()
    ax = int(part_a[1])
    ay = int(part_a[2])
    bx = int(part_b[1])
    by = int(part_b[2])
    px = int(goal[1]) + mod
    py = int(goal[2]) + mod
    d = ax * by - ay * bx
    if d == 0:
        continue
    a = (px * by - py * bx) / d
    b = (py * ax - px * ay) / d
    if a < 0 or b < 0 or a != int(a) or b != int(b):
        continue
    print(a,b)
    total += 3 * a + b
print(total)