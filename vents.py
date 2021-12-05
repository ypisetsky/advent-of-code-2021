from util import getlines, tokenedlines
from collections import defaultdict

def to_int_pair(s):
    return [int(tok) for tok in s.split(',')]
def my_range(low, high):
    return range(high - low + 1)

#lines = getlines("5small")
lines = getlines("5")

coord_pairs = []
for line in lines:
    parts = line.split()
    coord_pairs.append(sorted([to_int_pair(parts[0]), to_int_pair(parts[2])]))

data = defaultdict(lambda: defaultdict(int))

for s, d in coord_pairs:
    if s[0] == d[0]:
        for i in my_range(s[1], d[1]):
            data[s[0]][s[1] + i] += 1
    elif s[1] == d[1]:
        for i in my_range(s[0], d[0]):
            data[s[0] + i][s[1]] += 1
    # skip these for part 1
    elif s[1] - d[1] == s[0] - d[0]:
        for i in my_range(s[0], d[0]):
            data[s[0] + i][s[1] + i] += 1
            pass
    elif s[1] - d[1] == d[0] - s[0]:
        for i in my_range(s[0], d[0]):
            data[s[0] + i][s[1] - i] += 1
            pass

ret = 0
for row in data.values():
    for value in row.values():
        if value > 1:
            ret += 1
print(f"Part 2 is {ret}")