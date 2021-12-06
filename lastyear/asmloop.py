from util import getlines, tokenedlines

data = tokenedlines("old8")
def getnumber(row):
    return row[1]

def checkit(data, i):
    visited = set()
    ip = 0
    acc = 0
    while ip not in visited:
        if ip == len(data):
            return acc
        elif ip < 0 or ip > len(data):
            return None
        visited.add(ip)
        if data[ip][0] == 'acc':
            acc += getnumber(data[ip])
            ip += 1
        elif (data[ip][0] == 'nop') ^ (ip == i):
            ip += 1
        else:
            ip += getnumber(data[ip])
    return None

for i in range(len(data)):
    x = checkit(data, i)
    if x is not None:
        print(f"{x} is the acc. {i} is i")
        break