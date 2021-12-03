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
    vals = list(ret.values())
    if len(ret['0']) <= len(ret['1']):
        vals.reverse()
    return vals

oxygen_lines = data
cursor = 0
while len(oxygen_lines) > 1:
    oxygen_lines,_ = partition(oxygen_lines, cursor)
    cursor += 1
oxygen = int(oxygen_lines[0], 2)

scrubber_lines = data
cursor = 0
while len(scrubber_lines) > 1:
    _, scrubber_lines = partition(scrubber_lines, cursor)
    cursor += 1
scrubber = int(scrubber_lines[0], 2)

print(f"Solution 2 {oxygen} {scrubber} {oxygen * scrubber}")
