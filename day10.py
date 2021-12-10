from collections import defaultdict
from itertools import permutations, product
from util import getlines, getblankseparated, tokenedlines, neighbors4
file = "10"
#file = "10small"

MAP = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

class BadError(Exception):
    def __init__(self, c):
        self.c = c
    
    def score(self):
        LOOKUP = {')': 3,']': 57, '}': 1197, '>': 25137}
        return LOOKUP[self.c]

SCORE = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}


def score(line):
    stack = []
    for i, c in enumerate(line):
        if c in MAP:
            stack.append(c)
        elif c != MAP[stack.pop()]:
            raise BadError(c)
    score = 0
    for item in reversed(stack):
        score = 5 * score + SCORE[item]
    return score

ret = 0
scores = []
for line in getlines(file):
    try:
        scores.append(score(line))
    except BadError as e:
        ret += e.score()
print(f"part1 is {ret}. Part 2 is {sorted(scores)[len(scores)//2]}")
