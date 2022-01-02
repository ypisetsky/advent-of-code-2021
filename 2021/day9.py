from collections import defaultdict
from itertools import permutations, product
from util import getlines, getblankseparated, tokenedlines, neighbors4
file = "9"
#file = "9small"

rawdata = getlines(file)
data = [[int(c) for c in row] for row in rawdata]

def is_low(data, i, j):
    for x,y in neighbors4(i, j, data):
        if data[i][j] >= data[x][y]:
            return False
    return True


def neighbors(data, i, j):
    ret = []
    for x,y in neighbors4(i, j, data):
        if data[x][y] < 9:
            ret.append((x,y))
    return ret

def find_basin(data, i, j):
    queue = [(i, j)]
    visited = set()
    while queue:
        x,y = queue.pop(0)
        if (x,y) in visited:
            continue
        for neighbor in neighbors(data, x, y):
            queue.append(neighbor)
        visited.add((x,y))
    return len(visited)

ret = 0
candidates = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if is_low(data, i, j):
            ret += data[i][j] + 1
            candidates.append(find_basin(data, i, j))
print(f"Part 1 is {ret}")
best = sorted(candidates, reverse=True)[:3]
print(f"Best basins are {best} {best[0] * best[1] * best[2]}")