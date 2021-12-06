from util import getlines

data = getlines("old3")


def getcount(data, stride, rowcount=1):
    y = 0
    trees = 0
    for i, row in enumerate(data):
        if i % rowcount != 0:
            continue
        if row[y] == '#':
            trees += 1
        y += stride
        if y >= len(row):
            y -= len(row)
    return trees

result = getcount(data, 1) * getcount(data, 3) * getcount(data, 5) * getcount(data, 7) * getcount(data, 1, 2)

print(f"Tree count is {result}")