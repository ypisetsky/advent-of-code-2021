from util import getlines
data = getlines("old11")

def count_neighbors_slow(board, i, j):
    ret = 0
    def safeval(dx, dy):
        x = i
        y = j
        while True:
            x += dx
            y += dy
            if x < 0 or x >= len(board):
                return '-'
            if y < 0 or y >= len(board[0]):
                return '-'
            if board[x][y] != '.':
                return board[x][y]
    ret += safeval( - 1,  - 1) == '#'
    ret += safeval( - 1,  + 0) == '#'
    ret += safeval( - 1,  + 1) == '#'
    ret += safeval( + 1,  - 1) == '#'
    ret += safeval( + 1,  + 0) == '#'
    ret += safeval( + 1,  + 1) == '#'
    ret += safeval( + 0,  - 1) == '#'
    ret += safeval( + 0,  + 1) == '#'
    return ret

def find_neighbors(board, i, j):
    def safeval(dx, dy):
        x = i
        y = j
        while True:
            x += dx
            y += dy
            if x < 0 or x >= len(board):
                return None
            if y < 0 or y >= len(board[0]):
                return None
            if board[x][y] != '.':
                return (x,y)
    ret = []
    ret.append(safeval(-1, -1))
    ret.append(safeval(-1, 0))
    ret.append(safeval(-1, 1))
    ret.append(safeval(0, -1))
    ret.append(safeval(0, 1))
    ret.append(safeval(1, -1))
    ret.append(safeval(1, 0))
    ret.append(safeval(1, 1))
    return [x for x in ret if x != None]



lookups = {}
for i in range(len(data)):
    for j in range(len(data[i])):
        lookups[(i,j)] = find_neighbors(data, i, j)


def count_neighbors(board, i, j):
    return sum(1 for x,y in lookups[(i,j)] if board[x][y] == '#')

def nextstep(board):
    new_rows = []
    dirty = 0
    for i in range(len(board)):
        new_row = []
        for j in range(len(board[i])):
            neighborcount = count_neighbors(board, i, j)
            if board[i][j] == 'L' and neighborcount == 0:
                new_row.append('#')
                dirty += 1
            elif board[i][j] == '#' and neighborcount >= 5:
                new_row.append('L')
                dirty += 1
            else:
                new_row.append(board[i][j])
        new_rows.append(new_row)
    return new_rows, dirty

stepcount = 0

def printboard(board):
    print("----------------- BOARD ----------")
    for row in board:
        print(''.join(row))

while True:
    stepcount += 1
    newdata, dirty = nextstep(data)
    if not dirty:
        break
    if stepcount % 99 == 0:
        print(f"Step count {stepcount}. dirty: {dirty}")
        printboard(data)
        printboard(newdata)
    data = newdata

ret = 0
for row in data:
    for val in row:
        if val == '#':
            ret += 1
print(f"{ret} seats occupied")
