from util import getlines
from collections import defaultdict
data = getlines("old7")

def strip(desc):
    if desc[-1] == '.':
        desc = desc[:-1]
    if desc[-1] == 's':
        desc = desc[:-1]
    return desc

def parse_line(line):
    outer, inner = line.split("s contain ")
    if inner == 'no other bags.':
        return (strip(outer), {})
    inner_parts = inner.split(', ')
    inners = {}
    for inner in inner_parts:
        num, bag = inner.split(' ', 1)
        inners[strip(bag)] = num
    return (strip(outer), inners)

contains_graphx = [parse_line(line) for line in data]
contains_graph = {x: y for x,y in contains_graphx}

contained_in = defaultdict(list)
for outer, inners in contains_graph.items():
    for inner in inners:
        contained_in[inner].append(outer)

def dfs(node):
    if node not in contained_in:
        return {node}
    ret = {node}
    for child in contained_in[node]:
        ret = ret.union(dfs(child))
    return ret

print(f"contained_in: {contained_in}\nsolution: {len(dfs('shiny gold bag')) - 1}")

def dfs2(node):
    if node not in contains_graph:
        return 1
    ret = 1
    for child, count in contains_graph[node].items():
        ret += int(count) * dfs2(child)
    return ret

print(f"Part 2 solution is {dfs2('shiny gold bag') - 1}")