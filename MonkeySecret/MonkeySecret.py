from collections import Counter

file = open('input.txt')
total = 0
score_map = Counter()
for line in file:
    curr = int(line.strip())
    vals = [curr % 10]
    last = curr
    seen = set()
    for _ in range(2000):
        curr = (curr ^ curr * 64) % 16777216
        curr = (curr ^ curr //32) % 16777216
        curr = (curr ^ curr * 2048) % 16777216
        vals.append(curr % 10)
        last = curr
    for i in range(len(vals) - 5):
        window = vals[i: i+6]
        diffs = [str(window[1] - window[0])]
        for j in range(1, 4):
            d_win = str(window[j+1] - window[j])
            diffs.append(d_win)
        hash = ",".join(diffs)
        if hash not in seen:
            seen.add(hash)
            score_map[hash] += window[-2]

    total += curr

print(score_map.most_common(1))