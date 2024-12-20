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

for i, j in combinations(path, 2):
    sx, sy = i
    ex, ey = j
    if 1 < abs(sx - ex) + abs(sy - ey) <= 20:
        cheat_pairs.add((i, j))
print(len(cheat_pairs))
curr = end
count = 0
while prevs[curr] is not None:
    count += 1
    curr = prevs[curr]

savings = Counter()
for cheat_end, cheat_start in cheat_pairs:
    cheat_count = -1  * (abs(cheat_end[0] - cheat_start[0]) + abs(cheat_end[1] - cheat_start[1])) + 1
    cheat_curr = cheat_start
    while prevs[cheat_curr] != cheat_end:
        cheat_count += 1
        cheat_curr = prevs[cheat_curr]
    savings[cheat_count] += 1
print(count)
total = 0
for val, num in sorted(savings.items()):
    if val >= 100:
        total += num
print(total)