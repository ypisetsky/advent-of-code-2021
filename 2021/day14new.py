from collections import defaultdict
from itertools import permutations, product
import string
import numpy
import sys
from util import getlines, getblankseparated, tokenedlines, neighbors4
file = "14"
#file = "13small"


data = tokenedlines(file)

def get_transform_matrix(data):
    ret_map = {}
    for i, row in enumerate(data[1:]):
        # map a pair to the two new pairs it spawns (i.e. CH -> B means CH: CB + BH)
        ret_map[row[0]] = (row[0][0] + row[2], row[2] + row[0][1])

    pair_to_int = {pair: pos for pos, pair in enumerate(ret_map.keys())}

    transform_matrix = numpy.zeros([len(ret_map), len(ret_map)], dtype=int)
    for s, (d1, d2) in ret_map.items():
        transform_matrix[pair_to_int[s], pair_to_int[d1]] = 1
        transform_matrix[pair_to_int[s], pair_to_int[d2]] = 1
    return transform_matrix, pair_to_int

numpy.set_printoptions(threshold=sys.maxsize)
transform, pair_map = get_transform_matrix(data)

row = numpy.zeros(len(pair_map), dtype=int)
for i in range(len(data[0][0]) - 1):
    row[pair_map[data[0][0][i:i+2]]] += 1

# Take the original * the transform ^ 40th power
for i in range(40):
    row = row @ transform

counts = defaultdict(int)
# Each character appears as a first character of a pair (except the last char which we add in directly)
int_to_first_char = {v:k[0] for k,v in pair_map.items()}
for i, val in enumerate(row):
    counts[int_to_first_char[i]] += val
counts[data[0][0][-1]] += 1
print(max(counts.values()) - min(counts.values()))
