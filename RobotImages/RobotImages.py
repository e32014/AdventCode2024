import re
from collections import Counter

file = open('input.txt')

max_x = 101
max_y = 103
robots = []
for line in file:
    px, py, vx, vy = re.match('p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line.strip()).groups()
    robots.append((int(px), int(py), int(vx), int(vy)))

for c in range(10000):
    next_step = []
    robo_set = set()
    for px, py, vx, vy in robots:
        next_step.append(((px + vx) % max_x, (py + vy) % max_y, vx, vy))
        robo_set.add(((px + vx) % max_x, (py + vy) % max_y))
    robots = next_step
    if len(robots) == len(robo_set):
        for j in range(max_y):
            for i in range(max_x):
                if (i, j) in robo_set:
                    print('#',end = '')
                else:
                    print('.', end = '')
            print()
        for _ in range(max_x):
            print('_', end='')
        print()
        print(c)
        break

quad = Counter()
for px, py, _, _ in robots:
    if px < max_x // 2 and py < max_y // 2:
        quad[0] += 1
    elif px > max_x // 2 and py < max_y // 2:
        quad[1] += 1
    elif px < max_x // 2 and py > max_y // 2:
        quad[2] += 1
    elif px > max_x // 2 and py > max_y // 2:
        quad[3] += 1

total = 1
for val in quad.values():
    total *= val

print(total)