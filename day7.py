from collections import defaultdict
from util import getlines, getblankseparated, tokenedlines
file = "7"
#file = "7small"

data = sorted([int(x) for x in getlines(file)[0].split(',')])
best = None

def getcost(data, pos):
    ret = 0
    for el in data:
        d = abs(el - pos)
        ret += d
        #ret += d * (d+1) / 2
    return int(ret)

bestpos = 0
for i in range(data[0], data[-1] + 1):
    cost = getcost(data, i)
    #print(f"cost at {i} is {cost}")
    if (best is None) or best > cost:
        best = cost
        bestpos = i

print(f"Cost is {getcost(data, data[len(data) // 2])}")

print(f"Best is {best} at {bestpos}")

def part1simple(data):
    pivotpos = len(data) // 2
    pivot = data[pivotpos]
    return sum(pivot - x for x in data[:pivotpos]) + sum(x - pivot for x in data[pivotpos:])

print(f"Part 1 simple solution is {part1simple(data)}")
