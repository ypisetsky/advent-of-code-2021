
from collections import defaultdict
from util import getblankseparated

def dosurvey(responses):
    x = defaultdict(int)
    responsecount = len(responses.split())
    for c in responses:
        if c >= 'a' and c <= 'z':
            x[c] += 1
    ret = 0
    for count in x.values():
        if count == responsecount:
            ret += 1
    return ret


print(f"sum is {sum(dosurvey(item) for item in getblankseparated('old6'))}")