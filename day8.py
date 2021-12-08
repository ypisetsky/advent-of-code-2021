from collections import defaultdict
from util import getlines, getblankseparated, tokenedlines
file = "8"
#file = "8small"
ret = 0


NUMS = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
NUMS_LOOKUP = {pattern: i for i, pattern in enumerate(NUMS)}

all = list("abcdefg")
def generate_permutations(remain=all):
    if remain == []:
        return ['']
    ret = []
    for i in range(len(remain)):
        children = generate_permutations(remain[:i] + remain[i+1:])
        for c in children:
            ret.append(remain[i] + c)
    return ret

def transform(s, perm):
    ret = []
    for c in s:
        ret.append(perm[ord(c) - ord('a')])
    return ''.join(sorted(ret))

def check_permutation(permutation, nums):
    for num in nums:
        if transform(num, permutation) not in NUMS:
            return False
    return True


lines = tokenedlines(file)

for line in lines:
    for permutation in generate_permutations():
        if check_permutation(permutation, line[:10]):
            x = 0
            for i in range(11, 15):
                x = 10 * x + NUMS_LOOKUP[transform(line[i], permutation)]
            ret += x


#print(f"all perms are {generate_permutations()}")
print(f"Answer is {ret}")
