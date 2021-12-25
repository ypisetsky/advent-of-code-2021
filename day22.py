from collections import defaultdict
from itertools import permutations, product
import string
import numpy
from enum import Enum
import sys
import heapq
import math
from util import getlines, getblankseparated, tokenedlines, as_ints
import io
import itertools
from functools import cache
file = "22"
#file = "22small"

def to_cuboid(line):
    on, coords = line.split(' ')
    coord_pairs = coords.split(',')
    def split_coord(part):
        parts = part[2:].split('.')
        return as_ints([parts[0], parts[2]])
    return on, [split_coord(dim) for dim in coord_pairs]


def cuboid_contains(point, cuboid):
    for i, c in enumerate(point):
        cube_parts = cuboid[1][i]
        if c < cube_parts[0] or c > cube_parts[1]:
            return False
    return True

def check_point(point, cuboids):
    state = 'off'
    for cuboid in cuboids:
        if cuboid_contains(point, cuboid):
            #print(f"Yes {cuboid} {point}")
            state = cuboid[0]
    return state
cuboids = [to_cuboid(line) for line in getlines(file)]


def push(l, low, high):
    if high < low:
        return
    l.add((low, high))

def split(existing_cuboid, new_cuboid):
    dims = []
    dims2 = []
    for dim in range(3):
        e_parts = set()
        n_parts = set()
        a = existing_cuboid[1][dim][0]
        b = existing_cuboid[1][dim][1]
        c = new_cuboid[1][dim][0]
        d = new_cuboid[1][dim][1]
        if b < c or d < a:
            return [existing_cuboid]
        
        push(e_parts, a, min(c - 1, b))
        push(e_parts, max(a, c), min(b, d))
        push(e_parts, max(d + 1, a), b)
        push(n_parts, c, min(a - 1, d))
        push(n_parts, max(a, c), min(b, d))
        push(n_parts, max(b+1, c), d)
        
        dims.append(e_parts)
        dims2.append(n_parts)
    ret = set()
    for v in itertools.product(*dims):
        ret.add((existing_cuboid[0], tuple(v)))
    for coords in itertools.product(*dims2):
        if ('on', coords) in ret:
            ret.remove(('on', coords))
            print(f"Removing {v}")
        elif ('off', coords) in ret:
            ret.remove(('off', coords))

    return ret




existing_cuboids = []
for cuboid in cuboids:
    updated_cuboids = []
    for old_cuboid in existing_cuboids:
        updated_cuboids.extend(split(old_cuboid, cuboid))
        
    existing_cuboids = updated_cuboids + [cuboid]
    #print(f"added {cuboid}")
    #print(f"existing {updated_cuboids}")
    #print("")

ret1 = 0
for cuboid in existing_cuboids:
    if cuboid[0] == 'on':
        volume = 1
        for dim in range(3):
            volume *= cuboid[1][dim][1] - cuboid[1][dim][0] + 1
        print(f"{cuboid} {volume}")
        ret1 += volume

#print(cuboids)
#print(f"volume {ret1}")
num_on = 0
for i in range(-50, 51):
    for j in range(-50, 51):
        for k in range(-50, 51):
            if check_point((i,j,k), cuboids) == 'on':
                num_on += 1
    print(i)
print(num_on)

print(f"volume {ret1}")
