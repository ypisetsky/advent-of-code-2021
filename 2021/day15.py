from collections import defaultdict
from itertools import permutations, product
import string
import numpy
import sys
import heapq
from util import getlines, getblankseparated, tokenedlines, neighbors4
file = "15"
#file = "15small"

data = getlines(file)
maxX = len(data) * 5
maxY = len(data[0]) * 5

def getpathcost(path):
    return sum(data[x][y] for x,y in path)

def data_idx(x, y):
    score = int(data[x % len(data)][y % len(data[0])])
    score += x // len(data) + y // len(data[0])
    return (score - 1) % 9 + 1

def dijkstra(data):
    scores = {(0, 0): 0}
    queue = [(0, 0, 0)]
    while len(queue) > 0:
        curscore, i, j = heapq.heappop(queue)
        if curscore > scores[(i, j)]:
            #
            continue
        for x, y in neighbors4(i, j, maxX, maxY ):
            prev_score = scores.get((x, y))
            new_score = curscore + int(data_idx(x, y))
            if prev_score is None or new_score < prev_score:
                scores[(x, y)] = new_score
                heapq.heappush(queue, (new_score, x, y))
    return scores

ret = dijkstra(data)
print(f"ret is {maxX - 1} {maxY - 1} {ret[(maxX - 1, maxY - 1)]}")
