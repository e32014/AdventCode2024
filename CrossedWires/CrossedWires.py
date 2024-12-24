import copy
from itertools import combinations

file = open('input.txt')

def back_track(node, memory, back_graph, visited):
    if node in memory:
        return memory[node]
    if node in visited:
        return None
    left, op, right = back_graph[node]
    eval_left = back_track(left, memory, back_graph, visited.union({node}))
    eval_right = back_track(right, memory, back_graph, visited.union({node}))
    if eval_left is None or eval_right is None:
        return None
    if op == 'AND':
        return eval_left & eval_right
    if op == 'OR':
        return eval_left | eval_right
    if op == 'XOR':
        return eval_left ^ eval_right

def evaluate(memory, back_graph:dict[str, tuple[str, str, str]]):
    zs = dict()
    for key in back_graph.keys():
        if key.startswith('z'):
            zs[key] = back_track(key, memory, back_graph, set())
    i = 0
    formatted = 'z{:02d}'.format(i)
    result = 0
    while formatted in zs:
        result += zs[formatted] << i
        i += 1
        formatted = 'z{:02d}'.format(i)
    return result

vals = dict()
back_graph = dict()
mode = 0
for line in file:
    if line == '\n':
        mode = 1
        continue
    if mode == 0:
        var, val = line.strip().split(': ')[:2]
        vals[var] = int(val)
    else:
        left, op, right, _, result = line.strip().split()[:5]
        back_graph[result] = (left, op, right)

i = 0
formatted = 'x{:02d}'.format(i)
x = 0
while formatted in vals:
    x += vals[formatted] << i
    i += 1
    formatted = 'x{:02d}'.format(i)

i = 0
formatted = 'y{:02d}'.format(i)
y = 0
while formatted in vals:
    y += vals[formatted] << i
    i += 1
    formatted = 'y{:02d}'.format(i)

print(x, y)
goal = x + y
print(bin(x))
print(bin(y))
print(bin(goal))
print(bin(evaluate(vals, back_graph)))
print(evaluate(vals, back_graph))