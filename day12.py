from collections import defaultdict
from itertools import permutations, product
from util import getlines, getblankseparated, tokenedlines, neighbors4
file = "12"
#file = "12small"

def parse_paths(data):
    nodes = defaultdict(list)
    for path in data:
        s,d = path.split("-")
        nodes[s].append(d)
        nodes[d].append(s)
    return nodes

def is_bad(node, sofar):
    if node.upper() == node:
        return 0
    if not node in sofar:
        return 0
    if node in ["start", "end"]:
        return 1
    return 2

def get_path_count(node, nodes, sofar, doubled=False):
    if node == 'end':
        #print(f'found path {", ".join(sofar)}')
        return 1
    ret = 0
    #print(f"Checking {node} with {sofar}")
    for neighbor in nodes[node]:
        badness = is_bad(neighbor, sofar)
        if badness == 1 or (badness == 2 and doubled):
            continue
        new_doubled = doubled or (badness == 2)
        sofar.append(neighbor)
        ret += get_path_count(neighbor, nodes, sofar, new_doubled)
        sofar.pop()
    return ret

print(get_path_count("start", parse_paths(getlines(file)), ['start']))
