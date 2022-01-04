from util import tokenedlines
file = "14"

def mask_address(mask, address):
    chars = list(mask)[::-1]
    for i in range(len(chars)):
        if chars[i] != '0':
            continue
        if address & (1 << i) != 0:
            chars[i] = '1'
    return "".join(chars[::-1])

def handle_value(memory, new_address, new_value):
    old_addresses = list(memory.keys())
    for old_address in old_addresses:
        old_x_positions = []
        has_incompatibility = False
        for i in range(len(old_address)):
            if old_address[i] != 'X':
                if new_address[i] != 'X' and old_address[i] != new_address[i]:
                    has_incompatibility = True
            elif new_address[i] != 'X':
                old_x_positions.append(i)
        if has_incompatibility:
            continue
        old_value = memory[old_address]
        del memory[old_address]
        current_address = list(old_address)
        for x_position in old_x_positions:
            replacement_address = current_address.copy()
            replacement_address[x_position] = '1' if new_address[x_position] == '0' else '0'
            memory["".join(replacement_address)] = old_value
            current_address[x_position] = new_address[x_position]
    memory[new_address] = new_value

memory = {}
mask = ""
for line in tokenedlines(file):
    if line[0] == 'mask':
        mask = line[2]
    else:
        pos = mask_address(mask, int(line[0][4:-1]))
        handle_value(memory, pos, int(line[2]))
print(memory)

sum = 0
for address, value in memory.items():
    mul = 1
    for c in address:
        if c == 'X':
            mul *= 2
    sum += mul * value
    print(f"{mul} {value} {address}")
print(sum)
