from typing import Counter

file = open("input.txt")

def step(state: Counter[int]) -> Counter[int]:
    new_state = Counter[int]()
    for rock, count in state.items():
        str_rock = str(rock)
        if rock == 0:
            new_state[1] += count
        elif len(str_rock) % 2 == 0:
            new_state[int(str_rock[0:len(str_rock)//2])] += count
            new_state[int(str_rock[len(str_rock)//2:])] += count
        else:
            new_state[rock * 2024] += count
    return new_state

rocks = Counter[int]()
for line in file:
    rocks = Counter[int]([int(i) for i in line.split()])

for i in range(75):
    rocks = step(rocks)

print(rocks.total())