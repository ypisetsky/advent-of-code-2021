from collections import defaultdict
import functools
from itertools import permutations, product
import string
import numpy
from enum import Enum, auto
import sys
import heapq
import math
from util import getlines, getblankseparated, tokenedlines, neighbors4
import io
from functools import cache, cached_property
from dataclasses import dataclass
file = "21"
file = "21small"

class S(Enum):
    lefti= auto()
    lefto= auto()
    midleft= auto()
    mid= auto()
    midright= auto()
    righti= auto()
    righto= auto()
    alow= auto()
    ahigh= auto()
    blow= auto()
    bhigh= auto()
    clow= auto()
    chigh= auto()
    dlow= auto()
    dhigh= auto()
    amh = auto()
    bmh = auto()
    cmh = auto()
    dmh = auto()
    aml = auto()
    bml = auto()
    cml = auto()
    dml = auto()


adjacencies = {
    S.lefti: {S.lefto: 1, S.ahigh: 2, S.midleft: 2},
    S.midleft: {S.lefti: 2, S.ahigh: 2, S.bhigh: 2, S.mid: 2},
    S.mid: {S.midright: 2, S.bhigh: 2, S.chigh: 2},
    S.midright: {S.righti: 2, S.chigh: 2, S.dhigh: 2, S.righti: 2},
    S.righti: {S.dhigh: 2, S.righto: 1},
    S.alow: {S.aml: 1},
    S.blow: {S.bml: 1},
    S.clow: {S.cml: 1},
    S.dlow: {S.dml: 1},
    S.ahigh: {},
    S.bhigh: {},
    S.chigh: {},
    S.dhigh: {},
    S.amh: {S.aml: 1, S.ahigh: 1},
    S.bmh: {S.bml: 1, S.bhigh: 1},
    S.cmh: {S.cml: 1, S.chigh: 1},
    S.dmh: {S.dml: 1, S.dhigh: 1},
    S.aml: {},
    S.bml: {},
    S.cml: {},
    S.dml: {},
    S.lefto: {},
    S.righto: {},
}

for node, neighbors in adjacencies.items():
    adjacencies[node][node] = 0
    for neighbor, cost in neighbors.items():
        adjacencies[neighbor][node] = cost

#print(adjacencies)

for k in adjacencies:
    for i in adjacencies:
        for j in adjacencies:
            if k in adjacencies[i] and j in adjacencies[k]:
                new_cost = adjacencies[i][k] + adjacencies[k][j]
                if j not in adjacencies[i] or new_cost < adjacencies[i][j]:
                    adjacencies[i][j] = new_cost
print(adjacencies[S.chigh])

def move_cost(type, src, dest):
    multipliers = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    return multipliers[type] * adjacencies[src][dest]

ASTACK = [S.ahigh, S.amh, S.aml, S.alow]
BSTACK = [S.bhigh, S.bmh, S.bml, S.blow]
CSTACK = [S.chigh, S.cmh, S.cml, S.clow]
DSTACK = [S.dhigh, S.dmh, S.dml, S.dlow]
@functools.total_ordering
class State:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.str

    @cached_property
    def str(self):
        lines = []
        lines.append('#############')
        lines.append(f'#{self.s(S.lefto)}{self.s(S.lefti)} {self.s(S.midleft)} {self.s(S.mid)} {self.s(S.midright)} {self.s(S.righti)}{self.s(S.righto)}#')
        lines.append(f'###{self.s(S.ahigh)}#{self.s(S.bhigh)}#{self.s(S.chigh)}#{self.s(S.dhigh)}###')
        lines.append(f'  #{self.s(S.amh)}#{self.s(S.bmh)}#{self.s(S.cmh)}#{self.s(S.dmh)}#')
        lines.append(f'  #{self.s(S.aml)}#{self.s(S.bml)}#{self.s(S.cml)}#{self.s(S.dml)}#')
        lines.append(f'  #{self.s(S.alow)}#{self.s(S.blow)}#{self.s(S.clow)}#{self.s(S.dlow)}#')
        lines.append('  #########')
        return "\n".join(lines)

    def __repr__(self) -> str:
        return str(self)

    def get(self, pos):
        return self.data.get(pos)

    def s(self, pos):
        return self.data.get(pos, ' ')

    def neighbors(self):
        neighbors = {}
        if self.get(S.lefti) is None:
            neighbors.update(self.move_to_left(False))
            if self.get(S.lefto) is None:
                neighbors.update(self.move_to_left(True))
        if self.get(S.midleft) is None:
            neighbors.update(self.move_to_midleft())
        if self.get(S.mid) is None:
            neighbors.update(self.move_to_mid())
        if self.get(S.midright) is None:
            neighbors.update(self.move_to_midright())
        if self.get(S.righti) is None:
            neighbors.update(self.move_to_right(False))
            if self.get(S.righto) is None:
                neighbors.update(self.move_to_right(True))

        neighbors.update(self.move_to_a())
        neighbors.update(self.move_to_b())
        neighbors.update(self.move_to_c())
        neighbors.update(self.move_to_d())

        return neighbors
    
    def move_to_left(self, is_outer):
        ret = {}
        target = S.lefto if is_outer else S.lefti
        ret.update(self.move_from_stack(ASTACK, [], target, 'A'))
        ret.update(self.move_from_stack(BSTACK, [S.midleft], target, 'B'))
        ret.update(self.move_from_stack(CSTACK, [S.midleft, S.mid], target, 'C'))
        ret.update(self.move_from_stack(DSTACK, [S.midleft, S.mid, S.midright], target, 'D'))
        return ret

    def move_to_midleft(self):
        ret = {}
        ret.update(self.move_from_stack(ASTACK, [], S.midleft, 'A'))
        ret.update(self.move_from_stack(BSTACK, [], S.midleft, 'B'))
        ret.update(self.move_from_stack(CSTACK, [S.mid], S.midleft, 'C'))
        ret.update(self.move_from_stack(DSTACK, [S.mid, S.midright], S.midleft, 'D'))
        return ret
    
    def move_to_mid(self):
        ret = {}
        ret.update(self.move_from_stack(ASTACK, [S.midleft], S.mid, 'A'))
        ret.update(self.move_from_stack(BSTACK, [], S.mid, 'B'))
        ret.update(self.move_from_stack(CSTACK, [], S.mid, 'C'))
        ret.update(self.move_from_stack(DSTACK, [S.midright], S.mid, 'D'))
        return ret

    def move_to_midright(self):
        ret = {}
        ret.update(self.move_from_stack(ASTACK, [S.mid, S.midleft], S.midright, 'A'))
        ret.update(self.move_from_stack(BSTACK, [S.mid], S.midright, 'B'))
        ret.update(self.move_from_stack(CSTACK, [], S.midright, 'C'))
        ret.update(self.move_from_stack(DSTACK, [], S.midright, 'D'))
        return ret

    def move_to_right(self, is_outer):
        ret = {}
        target = S.righto if is_outer else S.righti
        ret.update(self.move_from_stack(ASTACK, [S.midleft, S.mid, S.midright], target, 'A'))
        ret.update(self.move_from_stack(BSTACK, [S.mid, S.midright], target, 'B'))
        ret.update(self.move_from_stack(CSTACK, [S.midright], target, 'C'))
        ret.update(self.move_from_stack(DSTACK, [], target, 'D'))
        return ret

    def move_from_stack(self, stack, prereqs, target, ok_val):
        for node in prereqs:
            if self.get(node) is not None:
                return {}
        for node in stack:
            if self.get(node) != None:
                return {self.move(node, target): move_cost(self.get(node), node, target)}
        
        return {}

    def move_to_a(self):
        ret = {}
        target = None
        v = 'A'
        stack = ASTACK
        values = [self.get(pos) for pos in stack]
        if values == [None, None, None, None]:
            target = stack[3]
        elif values == [None, None, None, v]:
            target = stack[2]
        elif values == [None, None, v, v]:
            target = stack[1]
        elif values == [None, v, v, v]:
            target = stack[0]
        else:
            return {}
        ret.update(self.move_to_stack('A', target, S.lefti, []))
        ret.update(self.move_to_stack('A', target, S.lefto, [S.lefti]))
        ret.update(self.move_to_stack('A', target, S.midleft, []))
        ret.update(self.move_to_stack('A', target, S.mid, [S.midleft]))
        ret.update(self.move_to_stack('A', target, S.midright, [S.midleft, S.mid]))
        ret.update(self.move_to_stack('A', target, S.righti, [S.midleft, S.mid, S.midright]))
        ret.update(self.move_to_stack('A', target, S.righto, [S.midleft, S.mid, S.midright, S.righti]))
        return ret

    def move_to_b(self):
        ret = {}
        target = None
        v = 'B'
        stack = BSTACK
        values = [self.get(pos) for pos in stack]
        if values == [None, None, None, None]:
            target = stack[3]
        elif values == [None, None, None, v]:
            target = stack[2]
        elif values == [None, None, v, v]:
            target = stack[1]
        elif values == [None, v, v, v]:
            target = stack[0]
        else:
            return {}
        ret.update(self.move_to_stack('B', target, S.lefti, [S.midleft]))
        ret.update(self.move_to_stack('B', target, S.lefto, [S.midleft, S.lefti]))
        ret.update(self.move_to_stack('B', target, S.midleft, []))
        ret.update(self.move_to_stack('B', target, S.mid, []))
        ret.update(self.move_to_stack('B', target, S.midright, [S.mid]))
        ret.update(self.move_to_stack('B', target, S.righti, [S.mid, S.midright]))
        ret.update(self.move_to_stack('B', target, S.righto, [S.mid, S.midright, S.righti]))
        return ret

    def move_to_c(self):
        ret = {}
        target = None
        v = 'C'
        stack = CSTACK
        values = [self.get(pos) for pos in stack]
        if values == [None, None, None, None]:
            target = stack[3]
        elif values == [None, None, None, v]:
            target = stack[2]
        elif values == [None, None, v, v]:
            target = stack[1]
        elif values == [None, v, v, v]:
            target = stack[0]
        else:
            return {}
        ret.update(self.move_to_stack('C', target, S.lefti, [S.mid, S.midleft]))
        ret.update(self.move_to_stack('C', target, S.lefto, [S.mid, S.midleft, S.lefti]))
        ret.update(self.move_to_stack('C', target, S.midleft, [S.mid]))
        ret.update(self.move_to_stack('C', target, S.mid, []))
        ret.update(self.move_to_stack('C', target, S.midright, []))
        ret.update(self.move_to_stack('C', target, S.righti, [S.midright]))
        ret.update(self.move_to_stack('C', target, S.righto, [S.midright, S.righti]))
        return ret

    def move_to_d(self):
        ret = {}
        target = None
        v = 'D'
        stack = DSTACK
        values = [self.get(pos) for pos in stack]
        if values == [None, None, None, None]:
            target = stack[3]
        elif values == [None, None, None, v]:
            target = stack[2]
        elif values == [None, None, v, v]:
            target = stack[1]
        elif values == [None, v, v, v]:
            target = stack[0]
        else:
            return {}
        ret.update(self.move_to_stack('D', target, S.lefti, [S.midright, S.mid, S.midleft]))
        ret.update(self.move_to_stack('D', target, S.lefto, [S.midright, S.mid, S.midleft, S.lefti]))
        ret.update(self.move_to_stack('D', target, S.midleft, [S.midright, S.mid]))
        ret.update(self.move_to_stack('D', target, S.mid, [S.midright, ]))
        ret.update(self.move_to_stack('D', target, S.midright, []))
        ret.update(self.move_to_stack('D', target, S.righti, []))
        ret.update(self.move_to_stack('D', target, S.righto, [S.righti]))
        return ret

    def move_to_stack(self, ok_val, target, source, prereqs):
        for node in prereqs:
            if self.get(node) is not None:
                return {}
        if self.get(source) is None:
            return {}
        if self.get(source) != ok_val:
            return {}
        if self.get(target) != None:
            print(f"WTF TARGET NOT NONE")
        return {self.move(source, target): move_cost(self.get(source), source, target)}

    def move(self, source, target):
        new_dict = self.data.copy()
        value = self.data[source]
        del new_dict[source]
        new_dict[target] = value
        return State(new_dict)
    
    def __eq__(self, other) -> bool:
        return self.data == other.data
    
    def __hash__(self):
        return str(self).__hash__()

    def __lt__(self, other):
        self.__hash__() < other.__hash__()

    def is_insane(self):
        for val in ['A', 'B', 'C', 'D']:
            if sum(x == val for x in self.data.values()) != 4:
                return True

#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########

    #D#C#B#A#
  #D#B#A#C#

initial_state = State({
    S.alow: 'A',
    S.ahigh: 'B',
    S.blow: 'D',
    S.bhigh: 'C',
    S.clow: 'C',
    S.chigh: 'B',
    S.dlow: 'A',
    S.dhigh: 'D',
    S.amh: 'D',
    S.aml: 'D',
    S.bmh: 'C',
    S.bml: 'B',
    S.cmh: 'B',
    S.cml: 'A',
    S.dmh: 'A',
    S.dml: 'C',
})

#############
#AA   C B BD#
###B#C# # ###
  #D#C# # #
  #D#B# #C#
  #A#D# #A#
  #########     3588

# initial_state = State({
#     S.lefto: 'A',
#     S.lefti: 'A',
#     S.mid: 'C',
#     S.midright: 'B',
#     S.righti: 'B',
#     S.righto: 'D',
#     S.alow: 'A',
#     S.ahigh: 'B',
#     S.blow: 'D',
#     S.bhigh: 'C',
#     S.dlow: 'A',
#     S.amh: 'D',
#     S.aml: 'D',
#     S.bmh: 'C',
#     S.bml: 'B',
#     S.dml: 'C',
# })

#############
#...........#
###D#D#C#C###
  #B#A#B#A#
  #########
initial_state = State({
    S.alow: 'B',
    S.ahigh: 'D',
    S.blow: 'A',
    S.bhigh: 'D',
    S.clow: 'B',
    S.chigh: 'C',
    S.dlow: 'A',
    S.dhigh: 'C',
    S.amh: 'D',
    S.aml: 'D',
    S.bmh: 'C',
    S.bml: 'B',
    S.cmh: 'B',
    S.cml: 'A',
    S.dmh: 'A',
    S.dml: 'C',
})
target_state = State({
    S.alow: 'A',
    S.ahigh: 'A',
    S.blow: 'B',
    S.bhigh: 'B',
    S.clow: 'C',
    S.chigh: 'C',
    S.dlow: 'D',
    S.dhigh: 'D',
    S.amh: 'A',
    S.aml: 'A',
    S.bmh: 'B',
    S.bml: 'B',
    S.cmh: 'C',
    S.cml: 'C',
    S.dmh: 'D',
    S.dml: 'D',
    
})

#print(f'{State(initial_state)}')
def dijkstra():
    global initial_state
    scores = {str(initial_state): 0}
    queue = [(0, initial_state)]
    i = 0
    while len(queue) > 0:
        curscore, state = heapq.heappop(queue)
        if curscore > scores[str(state)]:
            continue
        i += 1
        if i % 1000 == 0:
            print(f"Dijkstra {i} {len(scores)} {len(queue)}")
        for neighbor, cost in state.neighbors().items():
            if neighbor.is_insane() and not state.is_insane():
                print(f"INSANE NEIGHBOR\n{neighbor}\n{state}")
            prev_score = scores.get(str(neighbor))
            new_score = curscore + cost
            if prev_score is None or new_score < prev_score:
                scores[str(neighbor)] = new_score
                heapq.heappush(queue, (new_score, neighbor))
    return scores

for state, cost in dijkstra().items():
    if state == str(target_state):
        print(f'{state}     {cost}')
        break
