from collections import defaultdict
from itertools import permutations, product
import string
import numpy
from enum import Enum
import sys
import heapq
import math
from util import getlines, getblankseparated, tokenedlines, neighbors4
file = "17"
#file = "17small"

def binsearch(func, minval, maxval, target):
    pivot = (minval + maxval) / 2
    if maxval - minval < 1: return pivot
    if func(pivot) > target:
        return binsearch(func, minval, pivot, target)
    else:
        return binsearch(func, pivot, maxval, target)

def get_dx_range(num_steps, min_x, max_x):
    def dist(velocity):
        ret = 0
        for i in range(min(num_steps, math.ceil(velocity))):
            ret += velocity - i
        return ret
    lower = math.floor(binsearch(dist, 0, 1000, min_x))
    higher = math.ceil(binsearch(dist, 0, 1000, max_x))
    ret = []
    for i in range(lower, higher + 1):
        if dist(i) >= min_x and dist(i) <= max_x:
            ret.append(i)
    return ret

def get_dy_range(num_steps, min_y, max_y):
    def dist(velocity):
        ret = 0
        for i in range(num_steps):
            ret += velocity - i
        return ret
    lower = math.floor(binsearch(dist, -1000, 1000, min_y))
    higher = math.ceil(binsearch(dist, -1000, 1000, max_y))
    ys = []
    for i in range(lower, higher + 1):
        if dist(i) >= min_y and dist(i) <= max_y:
            ys.append(i)
    return ys

data = tokenedlines(file)[0]
x_parts = data[2][2:-1]
y_parts = data[3][2:]
min_x, max_x = (int(a) for a in x_parts.split(".."))
min_y, max_y = (int(a) for a in y_parts.split(".."))
best = 0
seen = set()
for num_steps in range(500):
    xs = get_dx_range(num_steps, min_x, max_x)
    if len(xs) == 0:
        #print(f"Skipping {num_steps} because not feasible horizontally")
        continue
    ys = get_dy_range(num_steps, min_y, max_y)
    if len(ys) == 0:
        #print(f"Skipping {num_steps} because no valid dy")
        continue
    if max(ys) > best:
        #print(f"Found a good {max(ys)} at {num_steps}")
        best = max(ys)
    for x in xs:
        for y in ys:
            seen.add((x, y))

print(f"Best dy is {best} for score of {(best) * (best + 1) // 2}")
print(f"count is {len(seen)}")
