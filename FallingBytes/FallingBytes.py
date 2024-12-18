file = open('input.txt')

dirs = [(0,1), (1,0), (0, -1), (-1, 0)]

def search(start, end, max_x, max_y, walls):
    queue = [(0, start, [start])]
    visited = set()
    while queue:
        steps, pos, path = queue.pop(0)
        px, py = pos
        if (px, py) in visited:
            continue
        if (px, py) == end:
            return steps, path
        visited.add((px, py))
        for dx, dy in dirs:
            if 0 <= px + dx <= max_x and 0 <= py + dy <= max_y and (px + dx, py + dy) not in walls and (px + dx, py + dy) not in visited:
                queue.append((steps + 1, (px + dx, py + dy), path + [(px + dx, py + dy)]))
    return -1, []

walls = set()
additionals = []
for line in file:
    if len(walls) == 1024:
        additionals.append(tuple([int(i) for i in line.strip().split(',')]))
    else:
        walls.add(tuple([int(i) for i in line.strip().split(",")]))

start = (0,0)
end = (70,70)
max_x = 70
max_y = 70
score, last_path = search(start, end, max_x, max_y, walls)
print(score)
for i in range(len(additionals)):
    if additionals[i] not in last_path:
        continue
    score, path = search(start, end, max_x, max_y, walls.union(set(additionals[:i+1])))
    if score == -1:
        print(additionals[i])
        break
    last_path = path