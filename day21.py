from collections import defaultdict
from itertools import permutations, product
import string
import numpy
from enum import Enum
import sys
import heapq
import math
from util import getlines, getblankseparated, tokenedlines, neighbors4
import io
file = "21"
file = "21small"

def detdie():
    i = 1
    while True:
        yield (i, i % 100)
        i += 1

def runturn(initial_score, initial_pos, die):
    _, pos = next(die)
    _, pos2 = next(die)
    final, pos3 = next(die)
    final_pos = (initial_pos + pos + pos2 + pos3 - 1) % 10 + 1
    return final, initial_score + final_pos, final_pos

MEMO = {}
def getpossibilities(curplayerscore, otherscore, curplayerpos, otherplayerpos):
    if otherscore >= 21:
        return 0, 1
    if (curplayerscore, otherscore, curplayerpos, otherplayerpos) in MEMO:
        return MEMO[curplayerscore, otherscore, curplayerpos, otherplayerpos]
    wins, losses = 0, 0
    ROLLS = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    for roll, freq in ROLLS.items():
        newpos = (curplayerpos + roll - 1) % 10 + 1
        newlosses, newwins = getpossibilities(otherscore, curplayerscore + newpos, otherplayerpos, newpos) 
        wins += newwins * freq
        losses += newlosses * freq
    MEMO[curplayerscore, otherscore, curplayerpos, otherplayerpos] = wins, losses
    return wins, losses
p1pos = 10
p1score = 0
p2pos = 3
p2score = 0
die = detdie()
while True:
    final1, p1score, p1pos = runturn(p1score, p1pos, die)
    if p1score >= 1000:
        print(f"Player 1 wins {final1 * p2score}")
        break
    final2, p2score, p2pos = runturn(p2score, p2pos, die)
    if p2score >= 1000:
        print(f"Player 2 wins {final2 * p1score}")
        break
    
poss = getpossibilities(0, 0, 10, 3)
print(f"part 2 {poss} {poss[1] - poss[0]}")
