from util import getlines, tokenedlines

#lines = getlines("5small")
lines = getlines("5")
coord_pairs = []
for line in lines:
    parts = line.split()
    def to_int_pair(s):
        toks = s.split(',')
        return [int(tok) for tok in toks]

    coord_pairs.append(sorted([to_int_pair(parts[0]), to_int_pair(parts[2])]))


max_x = 0
max_y = 0
for s,d in coord_pairs:
    if s[0] > max_x:
        max_x = s[0]
    if d[0] > max_x:
        max_x = d[0]
    if s[1] > max_y:
        max_y = s[1]
    if d[1] > max_y:
        max_y = d[1]

data = [[0 for i in range(max_y + 1)] for j in range(max_x + 1) ]

def my_range(low, high):
    return range(high - low + 1)

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
    elif s[1] - d[1] == d[0] - s[0]:
        for i in my_range(s[0], d[0]):
            data[s[0] + i][s[1] - i] += 1

ret = 0
for row in data:
    for value in row:
        if value > 1:
            ret += 1
print(f"Part 2 is {ret}")