from collections import Counter
from itertools import combinations

file = open('input.txt')

dirs = [(0,1), (1,0), (0, -1), (-1, 0)]
diags = [(1,1), (1,-1), (-1, 1), (-1, -1)]
grid = []
start = ()
end = ()
for i, line in enumerate(file):
    if 'S' in line:
        start = (line.index('S'), i)
        line = line.replace('S', '.')
    if 'E' in line:
        end = (line.index('E'), i)
        line = line.replace('E', '.')
    grid.append(line.strip())

prevs = dict()
cheat_pairs = set()
queue = [(start, None, [start])]
path = []

while queue:
    curr, last, curr_path = queue.pop(0)
    if curr in prevs:
        continue
    if curr == end:
        path = curr_path
    prevs[curr] = last

    px, py = curr
    for dx, dy in dirs:
        if 0 <= px + dx < len(grid[0]) and 0 <= py + dy < len(grid) and grid[py + dy][px + dx] != '#':
            queue.append(((px + dx, py + dy), curr, curr_path + [(px + dx, py + dy)]))
test_dict = Counter()
for i in range(len(path) - 100):
    for j in range(i + 100, len(path)):
        sx, sy = path[i]
        ex, ey = path[j]
        if 1 < abs(sx - ex) + abs(sy - ey) <= 20:
            cheat_pairs.add((path[i], path[j]))
            score = j - i - (abs(sx - ex) + abs(sy -ey))
            test_dict[score] += 1
total = 0
for val, num in sorted(test_dict.items()):
    if val >= 100:
        print(val, num)
        total += num
print(total)