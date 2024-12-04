file = open('input.txt')

grid = []
xes = []
aes = []
i = 0
for line in file:
    grid.append(line.strip())
    for j in range(0, len(line.strip())):
        if line[j] == 'X':
            xes.append((j, i))
        if line[j] == 'A':
            aes.append((j,i))
    i += 1

dirs = [(1,0), (0,1), (-1, 0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
count = 0
for x in xes:
    match = 'XMAS'
    for dir in dirs:
        for pos in range(1, len(match)):
            xx, xy = x
            if xx + dir[0] * pos < 0 or xx + dir[0] * pos >= len(grid[0]) or xy + dir[1] * pos < 0 or xy + dir[1] * pos >= len(grid):
                break
            if grid[xy + dir[1] * pos][xx + dir[0] * pos] != match[pos]:
                break
            elif pos == len(match) - 1 and grid[xy + dir[1] * pos][xx + dir[0] * pos] == match[pos]:
                count += 1
print(count)

pairs = [((1,1), (-1,-1)), ((-1,1), (1,-1))]
count = 0
chars = {'M','S'}
for a in aes:
    ax, ay = a
    valid = 0
    for dir_1, dir_2 in pairs:
        if 0 <= ax + dir_1[0] < len(grid[0]) and 0 <= ax + dir_2[0] < len(grid[0]) and 0 <= ay + dir_1[1] < len(grid) and 0 <= ay + dir_2[1] < len(grid):
            if grid[ay + dir_1[1]][ax + dir_1[0]] in chars and grid[ay + dir_2[1]][ax + dir_2[0]] in chars and grid[ay + dir_1[1]][ax + dir_1[0]] != grid[ay + dir_2[1]][ax + dir_2[0]]:
                valid += 1
    if valid == 2:
        count += 1
print(count)