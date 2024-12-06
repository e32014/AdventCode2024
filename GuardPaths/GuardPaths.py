file = open('input.txt')

grid = set()
facing = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1,0)}
rotate = {"U": "R", "R": "D", "D": "L", "L": "U"}
max_x = 0
max_y = 0

def walking(start, start_dir, added_obs):
    pos = start
    dir = start_dir
    visited = set()
    while 0 <= pos[0] < max_x and 0 <= pos[1] < max_y and (pos,dir) not in visited:
        visited.add((pos, dir))
        next = (pos[0] + facing[dir][0], pos[1] + facing[dir][1])
        if next in grid or next in added_obs:
            dir = rotate[dir]
        else:
            pos = next
    return (pos,dir) in visited, {pos for pos, dir in visited}

pos = (0,0)
for i, line in enumerate(file):
    max_x = len(line.strip())
    for j, char in enumerate(line.strip()):
        if char == '#':
            grid.add((j, i))
        elif char == '^':
            pos = (j, i)
    max_y += 1

dir = "U"

_, visited = walking(pos, dir, set())
count = 0
for new_ob in visited:
    if new_ob != pos:
        loop, _ = walking(pos, dir, {new_ob})
        if loop:
            count += 1



print(len(visited))
print(count)