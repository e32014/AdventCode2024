import itertools

file = open('input.txt')

antennas = dict()
max_y = 0
max_x = 0
for i, line in enumerate(file):
    max_y += 1
    max_x = len(line.strip())
    for j, char in enumerate(line.strip()):
        if char != '.':
            if char in antennas:
                antennas[char].append((j, i))
            else:
                antennas[char] = [(j, i)]

antinodes = set()
for _, points in antennas.items():
    for p1, p2 in itertools.permutations(points, 2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        for i in range(max_x):
            an_x = p2[0] - dx * i
            an_y = p2[1] - dy * i
            if 0 <= an_x < max_x and 0 <= an_y < max_y:
                antinodes.add((an_x, an_y))

print(len(antinodes))