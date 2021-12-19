from collections import defaultdict
from itertools import permutations, product
import string
from enum import Enum
import sys
import heapq
import math
from util import getlines, getblankseparated, tokenedlines, as_ints
import io
file = "19"
#file = "19small"

def transform_rot(point, type):
    x,y,z = point
    if type == 0:
        return point
    if type == 1:
        return (-y,x,z)
    if type == 2:
        return (-x, -y, z)
    if type == 3:
        return (y, -x, z)

def transform_pointing(point, type):
    x,y,z = point
    if type == 0:
        return point
    if type == 1:
        return (z,y,-x)
    if type == 2:
        return (x,z,-y)
    if type == 3:
        return (x,-z,y)
    if type == 4:
        return (x, -y, -z)
    if type == 5:
        return (z,-y,x)

def transform(point, type):
    rot = type % 4
    pointing = type // 4
    return transform_rot(transform_pointing(point, pointing), rot)

class Scanner:
    def __init__(self, points, position):
        self.points = set(points)
        self.position = position

    def rotate(self,type):
        return Scanner((transform(point, type) for point in self.points), self.position)
    
    def translate(self, position):
        return Scanner([add(point, position) for point in self.points], add(position, self.position))

    def __str__(self):
        return f"Scanner at {self.position}: {sorted(self.points)}"

    def __repr__(self) -> str:
        return str(self)
    
def scanner_from_lines(lines):
    points = []
    for line in lines:
        points.append(as_ints(line.split(',')))
    #print(f"Parsing {lines} {points}")
    return Scanner(points, (0,0,0))

def add(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1], p1[2] + p2[2]

def diff(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2]

scanners = []
current_lines = []
for line in getlines(file):
    if line[1] == '-':
        if current_lines:
            scanners.append(scanner_from_lines(current_lines))
            current_lines = []
    else:
        current_lines.append(line)
scanners.append(scanner_from_lines(current_lines))

def try_align(scanner1: Scanner, scanner2: Scanner):
    visited_points = set()
    for p1 in scanner1.points:
        for rotation in range(24):
            s2 = scanner2.rotate(rotation)
            for i, p2 in enumerate(s2.points):
                if i > len(s2.points) - 10:
                    break
                key = (diff(p1, p2), rotation)
                if key in visited_points:
                    continue
                visited_points.add(key)
                s2a = s2.translate(diff(p1, p2))
                #print(f"Scanner 1: {scanner1}\nScanner 2: {s2a}\n{p1} {p2} {diff(p1, p2)} {key}\n")
                intersect_count = len(scanner1.points.intersection(s2a.points))
                if intersect_count >= 12:
                    print(f"Key is {key}, intersect count is {intersect_count}")
                    print(scanner1)
                    print(s2a)
                    return s2a
    return None

matched_scanners = [scanners[0]]
remaining_scanners = scanners[1:]
next_scanners = [scanners[0]]
while len(remaining_scanners) > 0 and len(next_scanners) > 0:
    to_remove = []
    to_add_as_matched = []
    for old_scanner in next_scanners:
        for i, new_scanner in enumerate(remaining_scanners):
            alignment = try_align(old_scanner, new_scanner)
            if alignment:
                to_add_as_matched.append(alignment)
                to_remove.append(i)
    remaining_scanners = [scanner for i, scanner in enumerate(remaining_scanners) if i not in to_remove]
    next_scanners = to_add_as_matched
    matched_scanners.extend(to_add_as_matched)

    
print(matched_scanners)
print(len(set().union(*(s.points for s in matched_scanners))))
max_dist = 0
for s1 in matched_scanners:
    for s2 in matched_scanners:
        dist = sum(abs(a) for a in diff(s2.position, s1.position))
        if dist > max_dist:
            max_dist = dist
print(max_dist)