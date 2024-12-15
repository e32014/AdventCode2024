file = open('input.txt')

dirs = {"<": (-1, 0), "^": (0, -1), "v": (0, 1), ">": (1,0)}
walls = set()
boxes = set()
box_pair = {}
curr = ()
commands = ""
mode = 1
max_x = 0
max_y = 0
for i, line in enumerate(file):
    if line == "\n":
        mode = 2
        continue
    if mode == 1:
        max_y += 1
        for j, char in enumerate(line.strip()):
            if char == "#":
                walls.add((j * 2, i))
                walls.add((j * 2 + 1, i))
            if char == "O":
                boxes.add((j * 2, i))
            if char == "@":
                curr = (j * 2, i)
        max_x = (j + 1) * 2
    elif mode == 2:
        commands += line.strip()

for command in commands:
    dx, dy = dirs[command]
    px, py = curr

    hit_boxes = []
    offset = 1

    consider = [(px, py)]
    visited = []
    while consider:
        cx, cy = consider.pop()
        if (cx, cy) in visited:
            continue
        visited.append((cx, cy))
        if (cx + dx, cy + dy) in boxes:
            consider.append((cx + dx, cy + dy))
            consider.append((cx + dx + 1, cy + dy))
        elif (cx + dx - 1, cy + dy) in boxes:
            consider.append((cx + dx - 1, cy + dy))
            consider.append((cx + dx, cy + dy))
    legal = True
    for vx, vy in visited:
        if (vx + dx, vy + dy) in walls:
            legal = False
            break
        elif (vx, vy) in boxes:
            hit_boxes.append((vx, vy))

    if not legal:
        continue

    hit_boxes.sort(key=lambda x:abs(x[0] - px) + abs(x[1] - py), reverse=True)
    for box in hit_boxes:
        boxes.remove(box)
        boxes.add((box[0] + dx, box[1] + dy))
    curr = (px + dx, py + dy)

total = 0
for bx, by in boxes:
    total += by * 100 + bx
print(total)