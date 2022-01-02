from collections import defaultdict
from itertools import permutations, product
from util import getlines, printgrid
file = "13"
#file = "13small"

def parse(lines):
    points = set()
    for line in lines:
        parts = line.split(',')
        points.add((int(parts[0]), int(parts[1])))
    return points

def foldX(points, fold_x):
    newpoints = set()
    for x,y in points:
        if x < fold_x:
            newpoints.add((x,y))
        else:
            delta = x - fold_x
            newpoints.add((fold_x - delta, y))
    return newpoints

def foldY(points, fold_y):
    newpoints = set()
    for x,y in points:
        if y < fold_y:
            newpoints.add((x,y))
        else:
            delta = y - fold_y
            newpoints.add((x, fold_y - delta))
    return newpoints

all_lines = getlines(file)
coords = [line for line in all_lines if "fold" not in line]
folds = [line for line in all_lines if "fold" in line]

def dofold(points, fold):
    side, val = fold.split(' ')[2].split('=')
    if side == 'x':
        return foldX(points, int(val))
    else:
        return foldY(points, int(val))

points = parse(coords)
print(f"coords after {folds[0]} are {len(dofold(points, folds[0]))}")

for fold in folds:
    points = dofold(points, fold)

printgrid(points)