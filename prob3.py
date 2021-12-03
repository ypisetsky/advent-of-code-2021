from util import getlines

data = getlines("3")

linelen = len(data[0]) - 1
datalen = len(data)

gamma = 0
epsilon = 0

lines = []

for i in range(linelen):
    count = 0
    for j in data:
        if len(j) < linelen:
            continue
        if i == 0: lines.append(j.strip())
        if j[i] == '1':
            count += 1
    gamma *= 2
    epsilon *= 2
    if count > datalen / 2:
        gamma += 1
    else:
        epsilon += 1

print(f"Solution 1 is {gamma} {epsilon} {gamma * epsilon}")


def partition(strings, position):
    ret = dict({'0': [], '1': []})
    for string in strings:
        ret[string[position]].append(string)
    if len(ret['0']) > len(ret['1']):
        return (ret['0'], ret['1'])
    else:
        return (ret['1'], ret['0'])

orig_lines = lines
cursor = 0
while len(lines) > 1:
    lines,_ = partition(lines, cursor)
    cursor += 1
oxygen = int(lines[0], 2)

lines = orig_lines
cursor = 0
while len(lines) > 1:
    _, lines = partition(lines, cursor)
    cursor += 1
scrubber = int(lines[0], 2)

print(f"Solution 2 {oxygen} {scrubber} {oxygen * scrubber}")
