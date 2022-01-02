from collections import defaultdict
from itertools import permutations, product
import string
from enum import Enum
import sys
import heapq
import math
from util import getlines, getblankseparated, tokenedlines, as_ints, neighbors8
import io
file = "20"
#file = "20small"

data = getlines(file)
transform = data[0]
points = set()
for i,row in enumerate(data[1:]):
    for j,cell in enumerate(row):
        if cell == '#':
            points.add((i + 10000,j + 10000))
default = False

def compute(x, y, points, default, transform):
    idx = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            idx *= 2
            if ((x + i,y + j) in points) ^ default:
                idx += 1
    return transform[idx] == '#'

def step(points, transform, default):
    newpoints = set()
    new_default = default ^ (transform[0] == '#')
    for i,j in points:
        for x,y in neighbors8(i, j, 10000000, 1000000):
            new_val = compute(x, y, points, default, transform)
            #print(f"{x, y} {new_val}")
            
            if new_val != new_default:
                newpoints.add((x,y))
    return newpoints, new_default

def printimage(points):
    min_x = min(a[0] for a in points)
    min_y = min(a[1] for a in points)
    max_x = max(a[0] for a in points)
    max_y = max(a[1] for a in points)

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x,y) in points:
                print('#', end='')
            else:
                print(' ', end='')
        print('')
    print('')

printimage(points)
for i in range(50):
    points, default = step(points, transform, default)
    printimage(points)
print(len(points))