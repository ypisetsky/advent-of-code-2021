from util import tokenedlines
file = "14"


def apply_mask(mask_str: str, num):
    for i, val in enumerate(mask_str[::-1]):
        if val == '1':
            num |= 1 << i
        elif val == '0':
            num &= ~(1 << i)
    return num

mask = ''
data = {}
for line in tokenedlines(file):
    if line[0] == 'mask':
        mask = line[2]
    else:
        pos = int(line[0][4:-1])
        data[pos] = apply_mask(mask, int(line[2]))

print(data)
print(sum(data.values()))
