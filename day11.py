from collections import defaultdict
from itertools import permutations, product
from util import getlines, getblankseparated, tokenedlines, neighbors8
file = "11"
#file = "11small"

data = getlines(file)
print(f"data is {data}")

def step(prev):
    current = []
    allflashers = []
    for i, row in enumerate(prev):
        newrow = []
        for j, cell in enumerate(row):
            newrow.append(cell + 1)
        current.append(newrow)
    while True:
        flashers = []
        for i, row in enumerate(current):
            for j, cell in enumerate(row):
                if cell > 9:
                    flashers.append((i,j))
                    allflashers.append((i, j))
                    row[j] = 0
        if not flashers:
            break
        for i,j in flashers:
            for x,y in neighbors8(i, j, current):
                current[x][y] += 1
    for i, j in allflashers:
        current[i][j] = 0
    return len(allflashers), current

board = []
for row in data:
    board.append([int(c) for c in row])

x = 0
i = 0
while True:
    f, board = step(board)
    x += f
    i += 1
    print(f"step {i}: {f} flashers, {x} total")
    if f == 100:
        break
