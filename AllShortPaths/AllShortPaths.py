import math
import heapq

file = open('input.txt')

dirs = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
turns = {'N': ('W', 'E'), 'E': ('N', 'S'), 'S': ('E', 'W'), 'W': ('S', 'N')}
opps = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}

def djikstra(grid, starts, stops):
    dists = dict()
    best = math.inf
    heap = []
    visited = set()
    for start in starts:
        dists[start] = 0
        heapq.heappush(heap, (0, start))
    while heap:
        dist, curr = heapq.heappop(heap)
        if curr in visited:
            continue
        visited.add(curr)
        px, py, dir = curr
        if (px, py, dir) not in dists:
            dists[(px, py, dir)] = dist
        if (px, py, dir) in stops and dist < best:
            best = dist

        dx, dy = dirs[dir]
        if grid[py + dy][px + dx] != '#':
            heapq.heappush(heap, (dist + 1, (px + dx, py + dy, dir)))

        for rot in turns[dir]:
            heapq.heappush(heap, (dist + 1000, (px, py, rot)))
    return best, dists

grid = []
start = ()
end = ()
for i, line in enumerate(file):
    if 'S' in line:
        start = (line.index('S'), i, 'E')
        line = line.replace('S', '.').strip()
    elif 'E' in line:
        end = (line.index('E'), i)
        line = line.replace('E', '.').strip()
    grid.append(line.strip())

best_for, dist_for = djikstra(grid, [start], [(end[0], end[1], dir) for dir in dirs.keys()])
best_back, dist_back = djikstra(grid, [(end[0], end[1], dir) for dir in dirs.keys()], [start])
good = set()
for x, y, dir in dist_for:
    if (x, y, opps[dir]) in dist_back and dist_for[(x, y, dir)] + dist_back[(x, y, opps[dir])] == best_for:

        good.add((x, y))
print(best_for, best_back)
print(len(good))