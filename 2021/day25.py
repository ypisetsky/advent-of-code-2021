from util import getlines
file = "25"
#file = "25small"

def parse(lines):
    south = set()
    east = set()
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '>':
                east.add((i, j))
            elif char == 'v':
                south.add((i, j))
    return south, east    

def pos(i, j, lines):
    if i >= len(lines):
        i -= len(lines)
    if j >= len(lines[0]):
        j -= len(lines[0])
    return i, j

def step(south, east, lines):
    new_east = set()
    for i, j in east:
        newpos = pos(i, j + 1, lines)
        if newpos in east or newpos in south:
            new_east.add((i, j))
        else:
            new_east.add(newpos)
    new_south = set()
    for i, j in south:
        newpos = pos(i + 1, j, lines)
        if newpos in new_east or newpos in south:
            new_south.add((i, j))
        else:
            new_south.add(newpos)
    return new_south, new_east

lines = getlines(file)
i = 0
south, east = parse(lines)
while True:
    newsouth, neweast = step(south, east, lines)
    i += 1
    if newsouth == south and neweast == east:
        print(f"Fixed point at {i}")
        break
    south = newsouth
    east = neweast
