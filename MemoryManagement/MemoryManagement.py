file = open('input.txt')

memory = []
for line in file:
    on = True
    id = 0
    for char in line.strip():
        if on and char != '0':
            memory.append((id, int(char)))
        elif char != '0':
            memory.append((-1, int(char)))
        if on:
            id += 1
        on = not on
print(memory)

pos = len(memory) - 1
while pos > 0:
    consider = memory[pos]
    if consider[0] == -1:
        pos -= 1
        continue
    print(consider)
    f_pos = 0
    while f_pos < pos:
        if memory[f_pos][0] != -1 or memory[f_pos][1] < consider[1]:
            f_pos += 1
        elif memory[f_pos][1] == consider[1]:
            memory[pos] = memory[f_pos]
            memory[f_pos] = consider
            break
        else:
            memory[pos] = (-1, consider[1])
            removed = memory.pop(f_pos)
            memory.insert(f_pos, consider)
            memory.insert(f_pos + 1, (-1, removed[1] - consider[1]))
            pos += 1
            break
    pos -= 1
flat_mem = []
total = 0
for val, size in memory:
    for _ in range(size):
        flat_mem.append(val)
        if val != -1:
            total += val * (len(flat_mem) - 1)
print(total)