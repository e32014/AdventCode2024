file = open('input.txt')

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

grid = []
max_x = 0
max_y = 0
for line in file:
    max_y += 1
    grid.append(line.strip())
    max_x = len(grid[-1])

visited = set()
total = 0
side_total = 0
for i in range(0, max_x):
    for j in range(0, max_y):
        if (i, j) in visited:
            continue
        queue = [(i, j)]
        curr_char = grid[j][i]
        peri = 0
        sides = []
        area = {(i, j)}
        while queue:
            curr_x, curr_y = queue.pop(-1)
            if (curr_x, curr_y) in visited:
                continue
            visited.add((curr_x, curr_y))
            for dx, dy in dirs:
                if (curr_x + dx < 0 or
                        curr_x + dx >= max_x or
                        curr_y + dy < 0 or
                        curr_y + dy >= max_y or
                        grid[curr_y + dy][curr_x + dx] != curr_char):
                    peri += 1
                    sides.append((curr_x + dx, curr_y + dy, (dx, dy)))
                elif (curr_x + dx, curr_y + dy) not in visited:
                    queue.append((curr_x + dx, curr_y + dy))
                    area.add((curr_x + dx, curr_y + dy))
        total += peri * len(area)
        visited_sides = set()
        side_count = 0
        for side in sides:
            if side in visited_sides:
                continue
            queue = [side]
            while queue:
                curr_x, curr_y, orient = queue.pop(-1)
                if (curr_x, curr_y, orient) in visited_sides:
                    continue
                visited_sides.add((curr_x, curr_y, orient))
                for dx, dy in dirs:
                    if (curr_x + dx, curr_y + dy, orient) not in sides:
                        continue
                    elif (curr_x + dx, curr_y + dy, orient) not in visited_sides:
                        queue.append((curr_x + dx, curr_y + dy, orient))
            side_count += 1
        side_total += side_count * len(area)


print(total)
print(side_total)