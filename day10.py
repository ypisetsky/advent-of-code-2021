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
INVMAP = {v: k for k,v in MAP.items()}

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


# THIS IS BAD :-()
def get_next_chunk(line, pos):
    startchar = line[pos]
    cursor = pos + 1
    #print(f"{line} {pos} {startchar}")
    score = 0
    while cursor < len(line) and line[cursor] != MAP[startchar]:
        if line[cursor] in MAP:
            score , cursor = get_next_chunk(line, cursor)
        else:
            raise BadError(line[cursor])
        cursor += 1
    if cursor >= len(line):
        return (score * 5 + SCORE[startchar], cursor)
    elif cursor != len(line) - 1:
        return get_next_chunk(line, cursor + 1)
    else:
        return (0, cursor)

def score(line):
    stack = []
    for i, c in enumerate(line):
        if c in MAP:
            stack.append(c)
        elif c != MAP[stack.pop()]:
            print(f"{line} unexpected {c} at {i}")
            raise BadError(c)
    score = 0
    for item in reversed(stack):
        score = 5 * score + SCORE[item]
    print(f"Remain from {line} is {reversed(stack)}")
    return score

ret = 0
scores = []
for line in getlines(file):
    try:
        #score, _ = get_next_chunk(line, 0)
        s = score(line)
        scores.append(s)
        print(f"{line} score is {s}")
    except BadError as e:
        ret += e.score()
print(f"part1 is {ret}. Part 2 is {sorted(scores)[len(scores)//2]}")
