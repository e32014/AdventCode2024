from functools import lru_cache
from linecache import cache

file = open('input.txt')

towels = file.readline().strip().split(', ')

cache = {"": 1}
def find_towels(pattern):
    if pattern in cache:
        return cache[pattern]
    result = 0
    for towel in towels:
        if pattern.startswith(towel):
            result += find_towels(pattern[len(towel):])
    cache[pattern] = result
    return result

file.readline()

next_pattern = file.readline().strip()
valid = 0
while next_pattern:
    result = find_towels(next_pattern)
    next_pattern = file.readline().strip()
    valid += result
print(valid)