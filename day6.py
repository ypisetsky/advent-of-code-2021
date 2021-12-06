from util import getlines, getblankseparated, tokenedlines
from collections import defaultdict


data = getlines("6")
fish = data[0].split(',')
bucketed = defaultdict(int)

for f in fish:
    bucketed[int(f)] += 1
def step(fish):
    new = {}
    for i in range(1, 9):
        new[i-1] = fish.get(i, 0)
    new[8] = fish[0]
    new[6] += fish[0]
    return new

ret = 0

for i in range(256):
    bucketed = step(bucketed)
    print(f"{i + 1}: {sum(bucketed.values())}")
