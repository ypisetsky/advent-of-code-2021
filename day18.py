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
file = "18"
#file = "18small"

class NodeType(Enum):
    LEAF = 1
    PAIR = 2

class Node:
    def __init__(self, f):
        self.parent = None
        if isinstance(f, int):
            self.type = NodeType.LEAF
            self.value = f
            return
        elif isinstance(f, tuple):
            self.type = NodeType.PAIR
            self.left = f[0]
            self.right = f[1]
            self.left.parent = self
            self.right.parent = self
            return
        self.parent = None
        c = f.read(1)
        if c == '[':
            self.type = NodeType.PAIR
            self.left = Node(f)
            self.left.parent = self
            assert f.read(1) == ','
            self.right = Node(f)
            self.right.parent = self
            assert f.read(1) == ']'
        else:
            self.type = NodeType.LEAF
            self.value = int(c)
            self.left = None
            self.right = None

    def __str__(self) -> str:
        if self.type == NodeType.PAIR:
            return f'[{self.left},{self.right}]'
        else:
            return f'{self.value}'

    def __repr__(self) -> str:
        return str(self)

    def perform_inorder(self):
        if self.type == NodeType.LEAF:
            yield self
        else:
            for node in self.left.perform_inorder():
                yield node
            yield self
            for node in self.right.perform_inorder():
                yield node
    
    def depth(self):
        ret = -1
        node = self
        while node != None:
            node = node.parent
            ret += 1
        return ret

    def magnitude(self):
        if self.type == NodeType.LEAF:
            return self.value
        return self.left.magnitude() * 3 + 2 * self.right.magnitude()

def maybe_explode(root):
    node_list = list(root.perform_inorder())
    #print(f"In explode: {node_list}, {len(node_list)}")
    for i in range(len(node_list)):
        if node_list[i].depth() >= 4 and node_list[i].type == NodeType.PAIR:
            node_list[i].type = NodeType.LEAF
            node_list[i].value = 0
            for j in range(i - 2, -1, -1):
                if node_list[j].type == NodeType.LEAF:
                    node_list[j].value += node_list[i].left.value
                    break
            for j in range(i + 2, len(node_list)):
                if node_list[j].type == NodeType.LEAF:
                    node_list[j].value += node_list[i].right.value
                    break
            return True

def maybe_split(root):
    for node in root.perform_inorder():
        if node.type == NodeType.LEAF and node.value >= 10:
            node.type = NodeType.PAIR
            left = node.value // 2
            node.left = Node(left)
            node.left.parent = node
            node.right = Node(node.value - left)
            node.right.parent = node
            return True
    return False

def reduce(root):
    while maybe_explode(root) or maybe_split(root):
        pass
    return root

def parse_line(line):
    f = io.StringIO(line)
    root = Node(f)
    assert f.read() == ''
    return root

lines = getlines(file)
current = reduce(parse_line(lines[0]))
print(current)
for i in range(1, len(lines)):
    next = reduce(parse_line(lines[i]))
    current = reduce(Node((current, next)))
    print(current)
print(current.magnitude())

best = 0
for i in lines:
    for j in lines:
        if i == j:
            continue
        line = f'[{i},{j}]'
        sum = reduce(parse_line(line)).magnitude()
        if sum > best:
            best = sum
print(best)
