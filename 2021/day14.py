from collections import defaultdict
from itertools import permutations, product
import string
from util import getlines, getblankseparated, tokenedlines, neighbors4
file = "14"
#file = "14small"


data = tokenedlines(file)



pattern = data[0][0]
map = {}
for row in data[1:]:
    map[row[0]] = row[2]
print(map)

def step(pattern):
    '''Runs a step of doubling'''
    new_chars = []
    for i in range(len(pattern) - 1):
        new_chars.append(map[pattern[i:i+2]])
    new_chars.append('')
    #print(pattern, new_chars)
    return ''.join(f'{pattern[i]}{new_chars[i]}' for i in range(len(pattern)))


TENMEMO = {}
def tenstep(pair):
    '''Memoized run 10 steps of the algorithm for a pair, returning the added characters'''
    if pair in TENMEMO:
        return TENMEMO[pair]
    p = pair
    for i in range(10):
        p = step(p)
    TENMEMO[pair] = p[1:-1]
    return TENMEMO[pair]

def stepby10(pattern):
    '''Steps the pattern forward 10 steps, taking advantage of tenstep's memoization'''
    new_chars = []
    for i in range(len(pattern) - 1):
        new_chars.append(tenstep(pattern[i:i+2]))
    new_chars.append('')
    #print(pattern, new_chars)
    return ''.join(f'{pattern[i]}{new_chars[i]}' for i in range(len(pattern)))

pattern = stepby10(stepby10(pattern))

MEMO = {}
def getcounts(pair):
    '''Get the counts of characters when applying 20 steps to the given pair, memoized'''
    if pair in MEMO:
        return MEMO[pair]
    p = stepby10(stepby10(pair))
    counts = get_countdict()
    for c in p:
        counts[c] += 1
    MEMO[pair] = counts
    print(f"Computing {pair}: {counts}")
    return counts

def get_countdict():
    return {c: 0 for c in string.ascii_uppercase}


counts = get_countdict()
for i in range(len(pattern) - 1):
    '''For each pair in the 20 step output, add the counts on applying it for 20 more steps'''
    for c,n in getcounts(pattern[i:i+2]).items():
        counts[c] += n
    if i > 0:
        counts[pattern[i]] -= 1

counts = {x:y for x,y in counts.items() if y > 0}
print(f"max is {max(counts.values())} min is {min(counts.values())} diff is {max(counts.values()) - min(counts.values())}")
