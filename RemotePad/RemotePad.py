import math
from functools import lru_cache

file = open('input.txt')

@lru_cache()
def cheapest_dir(start, end, depth):
    queue = [(start, '')]
    shortest = math.inf
    ex, ey = end
    while queue:
        curr, path = queue.pop(0)
        if curr == end:
            rec = cheapest_robot(path + 'A', depth - 1)
            shortest = min(rec, shortest)
        cx, cy = curr
        if dir_pad[cy][cx] == 'X':
            continue
        if cx < ex:
            queue.append(((cx + 1, cy), path + '>'))
        if cx > ex:
            queue.append(((cx - 1, cy), path + '<'))
        if cy < ey:
            queue.append(((cx, cy + 1), path + 'v'))
        if cy > ey:
            queue.append(((cx, cy - 1), path + '^'))
    return shortest


def cheapest_robot(path, depth):
    if depth == 0:
        return len(path)
    result = 0
    start = dir_dict['A']
    for char in path:
        end = dir_dict[char]
        result += cheapest_dir(start, end, depth)
        start = end
    return result


def cheapest(start, end):
    queue = [(start, '')]
    shortest = math.inf
    ex, ey = end
    while queue:
        curr, path = queue.pop(0)
        if curr == end:
            rec = cheapest_robot(path + 'A', 25)
            shortest = min(rec, shortest)
        cx, cy = curr
        if num_pad[cy][cx] == 'X':
            continue
        if cx < ex:
            queue.append(((cx + 1, cy), path + '>'))
        if cx > ex:
            queue.append(((cx - 1, cy), path + '<'))
        if cy < ey:
            queue.append(((cx, cy + 1), path + 'v'))
        if cy > ey:
            queue.append(((cx, cy - 1), path + '^'))
    return shortest

dir_pad = [['X', '^', 'A'],
            ['<', 'v', '>']]

dir_dict = dict()
for i in range(len(dir_pad)):
    for j in range(len(dir_pad[i])):
        dir_dict[dir_pad[i][j]] = (j, i)

num_pad = [['7', '8', '9'],
           ['4', '5', '6'],
           ['1', '2', '3'],
           ['X', '0', 'A']]
num_dict = dict()
for i in range(len(num_pad)):
    for j in range(len(num_pad[i])):
        num_dict[num_pad[i][j]] = (j, i)
total = 0
for line in file:
    subs = line.strip()
    start = num_dict['A']
    score = 0
    for char in subs:
        end = num_dict[char]
        score += cheapest(start, end)
        start = end
    total += score * int(subs[:-1])

print(total)