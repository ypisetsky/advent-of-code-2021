from util import getlines
def tonum(s):
    return int(s.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2)

seats = list(tonum(line) for line in getlines("old5"))
for i in range(min(seats), max(seats)):
    if i not in seats:
        print(f"Missing seat {i}")
print(f"Best seat is {max(seats)}")