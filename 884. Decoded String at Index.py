import bisect
import collections
import cProfile
import heapq
import itertools
import math
import re
import unittest
from pprint import pprint

import numpy as np

'''

'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def tree_deserialize(string):
    """
    author: @StefanPochmann
    """
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def tree_height(root):
    """
    author: @StefanPochmann
    """
    return 1 + max(tree_height(root.left), tree_height(root.right)) if root else -1


def tree_draw(root):
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)
    import turtle
    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = tree_height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        d = []
        for l in S:
            if l.isdigit():
                d *= int(l)
            else:
                d.append(l)
            if K <= len(d):
                break
        # print(d)
        return d[K-1]

    def decodeAtIndex(self, S, K):
        pairs = []
        letter_count = 0
        for i,l in enumerate(S):
            if l.isdigit():
                if len(pairs) == 0:
                    pairs = [0, int(l), letter_count, S[:i]]
                else:
                    last_i = sum([p[2] for p in pairs]) + len(pairs)
                    pairs.append([pairs[-1][0] * pairs[-1][1] + letter_count, int(l), letter_count, S[last_i:i]])
                letter_count = 0
            else:
                letter_count += 1
            if (letter_count >= K) or (pairs and pairs[-1][0] * pairs[-1][1] + letter_count >= K):
                if not l.isdigit():
                    return S[i]
                break
        
        K %= pairs[-1][0]
        pairs_idx = -1
        while K <= pairs[pairs_idx][0]:
            pairs_idx -= 1
            K %= pairs[pairs_idx][0]
        return pairs[pairs_idx][3][K-pairs[pairs_idx][0]-1]





class Test(unittest.TestCase):

    def test(self):
        cases = [
            [dict(S = "leet2code3", K = 10), 'o'],
            [dict(S = "ha22", K = 5), 'h'],
            [dict(S = "a2345678999999999999999", K = 1), 'a'],
            [dict(S = "y959q969u3hb22odq595", K=222280369), 'y']
        ]
        for ci, co in cases:
            tmp = Solution().decodeAtIndex(**ci)
            print(tmp)
            assert tmp == co
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))

if __name__ == '__main__':
    unittest.main(exit=False)
