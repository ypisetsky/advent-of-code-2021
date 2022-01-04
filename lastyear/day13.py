from typing import Dict
from util import getlines
file = "13"

data = getlines(file)
arrival = int(data[0])
buses = [int(x) for x in data[1].split(',') if x != 'x']

def delta(arrival, bus):
    remainder = arrival % bus
    if remainder == 0:
        return 0
    print(f"bus {bus} {arrival + (bus - remainder)} {remainder}")
    return bus - remainder, bus


crt_problem = {}
for i, val in enumerate(data[1].split(',')):
    if val != 'x':
        crt_problem[int(val)] = (int(val) - i) % int(val)

def solve_crt(constraints: Dict):
    print(f"Solving CRT: {constraints}")
    constraint_keys = sorted(constraints.keys())
    current_val = constraints[constraint_keys[0]]
    step = 1
    for i in range(len(constraints) - 1):
        step *= constraint_keys[i]
        while current_val % constraint_keys[i + 1] != constraints[constraint_keys[i + 1]]:
            current_val += step
    return current_val

print(solve_crt({3: 0, 4: 3, 5: 4}))

wait, bus = min(delta(arrival, bus) for bus in buses)
print(f"{wait} {bus} {wait * bus}")
print(solve_crt(crt_problem))
