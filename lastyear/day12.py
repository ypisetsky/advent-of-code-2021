from util import getlines
file = "12"

dx = 1
dy = 0


x = 0
y = 0

def parseline(line):
    return line[0], int(line[1:])

for line in getlines(file):
    cmd, mag = parseline(line)
    if cmd == 'F':
        x += mag * dx
        y += mag * dy
    elif cmd == 'N':
        y += mag
    elif cmd == 'S':
        y -= mag
    elif cmd == 'E':
        x += mag
    elif cmd == 'W':
        x -= mag
    elif cmd == 'L' or cmd == 'R':
        mag = int(mag / 90)
        if cmd == 'R':
            mag = 4 - mag
        for i in range(mag):
            new_dy = dx
            dx = -dy
            dy = new_dy

dist = abs(x) + abs(y)
print(f"{x} {y} {dist}")


dx = 10
dy = 1
x = 0
y = 0
for line in getlines(file):
    cmd, mag = parseline(line)
    if cmd == 'F':
        x += mag * dx
        y += mag * dy
    elif cmd == 'N':
        dy += mag
    elif cmd == 'S':
        dy -= mag
    elif cmd == 'E':
        dx += mag
    elif cmd == 'W':
        dx -= mag
    elif cmd == 'L' or cmd == 'R':
        mag = int(mag / 90)
        if cmd == 'R':
            mag = 4 - mag
        for i in range(mag):
            new_dy = dx
            dx = -dy
            dy = new_dy
dist = abs(x) + abs(y)
print(f"{x} {y} {dist}")
