from util import getlines, getblankseparated, tokenedlines
from collections import defaultdict


data = getlines("6")
fish = data[0].split(',')
fish_by_day = defaultdict(int)

for f in fish:
    fish_by_day[int(f)] += 1

def step(fish_by_day):
    new = {}
    for i in range(1, 9):
        new[i-1] = fish_by_day.get(i, 0)
    new[8] = fish_by_day[0]
    new[6] += fish_by_day[0]
    return new

ret = 0

for i in range(256):
    fish_by_day = step(fish_by_day)
    print(f"{i + 1}: {sum(fish_by_day.values())}")
