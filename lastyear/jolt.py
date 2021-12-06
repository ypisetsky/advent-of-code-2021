from util import tokenedlines
from collections import defaultdict

data = [0] + sorted([x[0] for x in tokenedlines("old10")])
print(data)

dist = defaultdict(int)

for i in range(1, len(data)):
    dist[data[i] - data[i-1]] += 1

dist[3] += 1
print(f"dist is {dist} {dist[3] * dist[1]}")

memo = {}
def numpaths(i, arr):
    if i in memo:
        return memo[i]
    if len(arr) == 1:
        return 1
    ret = 0
    if len(arr) > 3 and arr[3] - arr[0] <= 3:
        ret += numpaths(i + 3, arr[3:])
    if len(arr) > 2 and arr[2] - arr[0] <= 3:
        ret += numpaths(i + 2, arr[2:])
    if arr[1] - arr[0] <= 3:
        ret += numpaths(i + 1, arr[1:])
    memo[i] = ret
    return ret
print(f"path count is {numpaths(0, data)}")