from util import getlines

data = getlines("3")

linelen = len(data[0])
datalen = len(data)

gamma = 0
epsilon = 0

lines = []

for i in range(linelen):
    count = 0
    for line in data:
        if line[i] == '1':
            count += 1
    if count > datalen / 2:
        gamma += 2 ** (linelen - i - 1)
    else:
        epsilon += 2 ** (linelen - i - 1)

print(f"Solution 1 is {gamma} {epsilon} {gamma * epsilon}")


def partition(strings, position):
    ret = dict({'0': [], '1': []})
    for string in strings:
        ret[string[position]].append(string)
    vals = list(ret.values())
    if len(ret['0']) <= len(ret['1']):
        vals.reverse()
    return vals

oxygen_lines = data
for i in range(linelen):
    oxygen_lines,_ = partition(oxygen_lines, i)
    if len(oxygen_lines) == 1: break
oxygen = int(oxygen_lines[0], 2)

scrubber_lines = data
for i in range(linelen):
    _, scrubber_lines = partition(scrubber_lines, i)
    if len(scrubber_lines) == 1: break
scrubber = int(scrubber_lines[0], 2)

print(f"Solution 2 {oxygen} {scrubber} {oxygen * scrubber}")
