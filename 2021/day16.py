from collections import defaultdict
from itertools import permutations, product
import string
import numpy
from enum import Enum
import sys
import heapq
from util import getlines, getblankseparated, tokenedlines, neighbors4
file = "16"
#file = "16small"

def idx(bitstring, pos):
    if pos >= len(bitstring):
        return None
    return bitstring[pos]

def nbits_to_num(bitstring, pos, n):
    num = 0
    for i in range(n):
        num *= 2
        num += idx(bitstring, pos) == '1'
        pos += 1
    return num

def parse_literal(bitstring, pos):
    num = 0
    while True:
        num *= 16
        num += nbits_to_num(bitstring, pos + 1, 4)
        if idx(bitstring, pos) != '1':
            break
        pos += 5
    return (pos + 5, num)

class EndType(Enum):
    SOLO = 0
    PACKETS = 1
    BITS = 2

class OpCode(Enum):
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    LITERAL = 4
    GT = 5
    LT = 6
    EQUAL = 7

class Packet:
    def __init__(self, version, type, endtype, num, pos, endpos):
        self.version = version
        self.type = OpCode(type)
        self.endtype = endtype
        self.num = num
        self.pos = pos
        self.endpos = endpos

    def eval(self, packetlist):
        if self.type == OpCode.LITERAL:
            return self.num, self.endpos

        pos = self.endpos
        args = []
        if self.endtype == EndType.BITS:
            while pos < self.endpos + self.num:
                new_arg, pos = packetlist[pos].eval(packetlist)
                args.append(new_arg)
        elif self.endtype == EndType.PACKETS:
            for i in range(self.num):
                new_arg, pos = packetlist[pos].eval(packetlist)
                args.append(new_arg)
        print(f"Evaling {self.__dict__} with args {args}")
        if self.type == OpCode.SUM:
            return sum(args), pos
        elif self.type == OpCode.PRODUCT:
            ret = 1
            for arg in args:
                ret *= arg
            return ret, pos
        elif self.type == OpCode.MAXIMUM:
            return max(args), pos
        elif self.type == OpCode.MINIMUM:
            return min(args), pos
        elif self.type == OpCode.GT:
            return args[0] > args[1], pos
        elif self.type == OpCode.LT:
            return args[0] < args[1], pos
        elif self.type == OpCode.EQUAL:
            return args[0] == args[1], pos
        else:
            print(f"Wat {self.__dict__}")
            


def getpacket(bitstring, pos):
    version = nbits_to_num(bitstring, pos, 3)
    type = OpCode(nbits_to_num(bitstring, pos + 3, 3))
    endtype = EndType.SOLO
    startpos = pos
    num = 0
    if type == OpCode.LITERAL:
        pos, num = parse_literal(bitstring, pos + 6)
    elif idx(bitstring, pos + 6) == '1':
        num = nbits_to_num(bitstring, pos + 7, 11)
        endtype = EndType.PACKETS
        pos += 7 + 11
    else:
        num = nbits_to_num(bitstring, pos + 7, 15)
        endtype = EndType.BITS
        pos += 7 + 15
    return Packet(version, type, endtype, num, startpos, pos)

data = bin(int(getlines(file)[0], 16))[2:] # 2: to strip 0b prefix
while len(data) % 4 != 0: # hex string contains sequences of 4 bits. bin() strips leading 0s though
    data = '0' + data

pos = 0
packetlist = {}
while pos < len(data) - 6:
    packet = getpacket(data, pos)
    packetlist[pos] = packet
    pos = packet.endpos

print(f"part 1 is {sum(packet.version for packet in packetlist.values())}")
for i, packet in packetlist.items():
    print(f"At {i} packet is {packet.__dict__}")
print(f"Value of first packet is {packetlist[0].eval(packetlist)[0]}")
