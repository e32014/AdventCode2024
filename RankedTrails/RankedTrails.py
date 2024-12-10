file = open('input.txt')

dirs = [(0,1), (1, 0), (0, -1), (-1, 0)]

def hash_path(path: list[tuple[int, int]]) -> str:
    out = ""
    for x, y in path:
        out += "(" + str(x) + "," + str(y)+ ")"
    return out


def dfs(start: tuple[int, int], graph: list[list[int]]) -> int:
    stack = [(start, [])]
    goals = set()
    while len(stack) > 0:
        curr = stack.pop(-1)
        path = curr[1]
        curr_x, curr_y = curr[0]
        curr_val = graph[curr_y][curr_x]
        if curr_val == 9:
            goals.add((curr_x, curr_y, hash_path(path)))
            continue

        for dx, dy in dirs:
            conn_x = curr_x + dx
            conn_y = curr_y + dy
            if conn_x < 0 or conn_x >= len(graph[0]) or conn_y < 0 or conn_y >= len(graph):
                continue
            if (conn_x, conn_y) not in path and graph[conn_y][conn_x] == curr_val + 1:
                stack.append(((conn_x, conn_y), path + [(conn_x, conn_y)]))
    return len(goals)


graph = []
starts = []
for i,line in enumerate(file):
    row = []
    for j, char in enumerate(line.strip()):
        row.append(int(char))
        if char == '0':
            starts.append((j, i))
    graph.append(row)

total = 0
for start in starts:
    total += dfs(start, graph)

print(total)